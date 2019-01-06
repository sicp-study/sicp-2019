# Copyright (c) 2019 Red Hat
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import logging
import os
import re


class EvaluateScheme:
    log = logging.getLogger("EvaluateScheme")

    def __init__(self):
        self.argv = ["mit-scheme"]
        mem = 1024 * 1024 * 64
        self.limits = {
            "data": mem * 5,
            "as": mem * 5,
            "rss": mem,
            "stack": mem,
            "fsize": 1024 * 1024,
            "nofile": 24,
            "cpu": 3,
            "nproc": 1,
        }
        self.scheme = None

    def open(self):
        if self.scheme:
            raise RuntimeError("Already running mit-scheme...")
        argv = ["prlimit"]
        for k, v in self.limits.items():
            argv.append("--%s=%s" % (k, str(v)))
        argv += self.argv
        self.log.debug("Starting %s", " ".join(argv))
        self.scheme = subprocess.Popen(
            argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # Sink header
        for i in range(10):
            self.scheme.stdout.readline()

    def __del__(self):
        self.close()

    def close(self):
        if self.scheme:
            try:
                self.scheme.kill()
            except OSError:
                pass
        self.scheme = None

    def iter_statements(self, fpath):
        """Yield sexp in the file content"""
        with open(fpath) as obj:
            content = obj.read()
        if not content.endswith('\n'):
            content += '\n'
        # Remove comments
        content = re.subn(r' *;;.*\n', '\n', content)[0]
        # idx is parser position, state is the () count, exp is current s-exp
        idx, state, sexp = 0, 0, ""
        while idx < len(content):
            if content[idx] not in ('(', ')') and state == 0:
                # Special case for value expression
                new_line_idx = idx + content[idx:].index('\n')
                sexp += content[idx:new_line_idx]
                idx = new_line_idx
            else:
                sexp += content[idx]
            if content[idx] == '(':
                state += 1
            elif content[idx] == ')':
                state -= 1
            if sexp and state <= 0:
                yield sexp
                sexp = ''
            idx += 1

    def get_statement(self, fpath):
        statements = list(self.iter_statements(fpath))
        if len(statements) != 1:
            raise RuntimeError("Only one statement is expected")
        return statements[0]

    def validate(self, fpath):
        """Run the validation method associated with the file"""
        exercise = re.subn(r'[-.]', '_',
                           os.path.basename(fpath).replace('.scm', ''))[0]
        exercise = re.subn(r'[^0-9_]', '', exercise)[0]
        func = getattr(self, "eval_%s" % exercise, None)
        if not func:
            return "Unknown exercise %s" % exercise
        self.log.debug("Using %s to validate %s", "eval_%s" % exercise, fpath)
        try:
            result = func(fpath)
        finally:
            self.close()
        if result:
            raise RuntimeError(result)
        return "SUCCESS"

    def eval(self, statement):
        """Send statement to mit-scheme, except a new line output"""
        if not self.scheme:
            self.open()
        if not statement.endswith('\n'):
            statement += '\n'
        self.log.debug("-> Sending to mit-scheme [%s]", statement[:-1])
        self.scheme.stdin.write(statement)
        r = ""
        while not r:
            r = self.scheme.stdout.readline().strip()
        if r != "1 ]=>":
            raise RuntimeError("Oops, something went wrong: %s" % r)
        result = self.scheme.stdout.readline().strip()
        self.log.debug("Received [%s]", result)
        return result
