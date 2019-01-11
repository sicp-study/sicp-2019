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

"""SPOILER ALERT: below are the solutions to the exercices..."""

import math

from scheme import EvaluateScheme


class EvaluateSICP(EvaluateScheme):
    def eval_1_1(self, fpath):
        expect = ["10", "12", "8", "3", "6", "19", "#f", "4", "16", "6", "16"]
        errors = []
        for statement, result in zip(self.iter_statements(fpath), expect):
            if statement != result:
                errors.append("%s isn't correct" % statement)
        return ",".join(errors)

    def eval_1_2(self, fpath):
        result = self.eval(self.get_statement(fpath))
        if result != ";Value: -37/150":
            return "Invalid output %s" % result

    def eval_1_3(self, fpath):
        for statement in self.iter_statements(fpath):
            ret = self.eval(statement)
            if ret != ";Unspecified return value":
                return "[%s] output %s" % (statement, ret)
        for test, expected in (("1 2 3", "13"),
                               ("1 1 1", "2"),
                               ("0 0 1", "1")):
            f = "(square-sum-larger %s)" % test
            ret = self.eval(f)
            if ret != ";Value: %s" % expected:
                return "%s should have returned %s instead of %s" % (
                    f, expected, ret)

    def eval_1_7(self, fpath):
        # Load provided code
        for statement in self.iter_statements(fpath):
            ret = self.eval(statement)
            if ret != ";Unspecified return value":
                return "[%s] output %s" % (statement, ret)
        # Eval some test and check the precision
        for test, precision in ((1e-3, 1e-5), (1e9, 1e-2), (2**53, 1e-1)):
            f = "(sqrt %s)" % test
            ret = self.eval(f).split()

            if ret[0] != ";Value:":
                return "%s should have returned a value instead of %s" % (
                    f, " ".join(ret))
            val = float(ret[1])
            if abs(math.sqrt(test) - val) > precision:
                return "%s is not precise enough (%s != %s)" % (
                    f, math.sqrt(test), val)

    def eval_1_8(self, fpath):
        # Load provided code
        for statement in self.iter_statements(fpath):
            ret = self.eval(statement)
            if ret != ";Unspecified return value":
                return "[%s] output %s" % (statement, ret)
        # Eval some test and check the precision
        for test, precision in ((1e-3, 1e-5), (1e9, 1e-2), (2**53, 1e-1)):
            f = "(cube-root %s)" % test
            ret = self.eval(f).split()

            if ret[0] != ";Value:":
                return "%s should have returned a value instead of %s" % (
                    f, " ".join(ret))
            val = float(ret[1])
            if abs(test**(1/3.) - val) > precision:
                return "%s is not precise enough (%s != %s)" % (
                    f, test**(1/3.), val)
