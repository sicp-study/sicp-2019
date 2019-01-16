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
        self.load(fpath)

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
        self.load(fpath)

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

    def eval_1_11(self, fpath):
        # Load provided code
        self.load(fpath)

        # Eval some test
        errors = []
        for test, result in (
                (0, 0), (1, 1), (2, 2), (3, 4), (4, 11), (5, 25), (6, 59)):
            for exp in ("f-recursive", "f-iterative"):
                f = "(%s %s)" % (exp, test)
                ret = self.eval(f).split()

                if ret[0] != ";Value:":
                    return "%s should have returned a value instead of %s" % (
                        f, " ".join(ret))
                val = int(ret[1])
                if val != result:
                    errors.append("%s is not the correct answer for %s" % (
                        val, f
                    ))
        return ", ".join(errors)

    def eval_1_12(self, fpath):
        # Load provided code
        self.load(fpath)

        errors = []
        for row, col, result in (
                (1, 1, 1), (1, 2, 1), (2, 2, 1),
                (1, 3, 1), (2, 3, 2), (3, 3, 1),
                (1, 4, 1), (2, 4, 3), (3, 4, 3), (4, 4, 1),
                (1, 5, 1), (2, 5, 4), (3, 5, 6), (4, 5, 4), (5, 5, 1),
                (2, 6, 5), (3, 6, 10), (4, 6, 10), (5, 6, 5),
                (2, 7, 6), (3, 7, 15), (4, 7, 20),
                (0, 0, -1), (0, 3, -1), (-1, 1, -1), (1, -1, -1)):
            f = "(pascal %d %d)" % (row, col)
            ret = self.eval(f).split()
            if ret[0] != ";Value:":
                return "%s should have returned a value instead of %s" % (
                    f, " ".join(ret))
            if int(ret[1]) != result:
                errors.append("%s is not the correct answer for %s" % (
                    ret[1], f
                ))
        return ", ".join(errors)

    def eval_1_16(self, fpath):
        # Load provided code
        self.load(fpath)

        errors = []
        for x, y in ((2, 2), (8, 9), (3, 3), (3, 4), (1, 0), (2, 0), (0, 0)):
            for b, n in ((x, y), (y, x)):
                f = "(fast-expt-iterative %d %d)" % (b, n)
                ret = self.eval(f).split()
                if ret[0] != ";Value:":
                    return "%s should have returned a value instead of %s" % (
                        f, " ".join(ret))
                if int(ret[1]) != b ** n:
                    errors.append("%s is not the correct answer for %s" % (
                        ret[1], f
                    ))
        return ", ".join(errors)

    def eval_1_17(self, fpath):
        # Load provided code
        self.load(fpath)

        errors = []
        for x, y in ((2, 2), (8, 9), (3, 3), (3, 4), (1, 0), (2, 0), (0, 0)):
            for a, b in ((x, y), (y, x)):
                f = "(fast-mult %d %d)" % (a, b)
                ret = self.eval(f).split()
                if ret[0] != ";Value:":
                    return "%s should have returned a value instead of %s" % (
                        f, " ".join(ret))
                if int(ret[1]) != a * b:
                    errors.append("%s is not the correct answer for %s" % (
                        ret[1], f
                    ))
        return ", ".join(errors)

    def eval_1_18(self, fpath):
        # Load provided code
        self.eval("(define (even? n) (= (remainder n 2) 0))")
        self.eval("(define (double x) (+ x x))")
        self.eval("(define (halve x) (/ x 2))")
        self.load(fpath)

        errors = []
        for x, y in ((2, 2), (8, 9), (3, 3), (3, 4), (1, 0), (2, 0), (0, 0)):
            for a, b in ((x, y), (y, x)):
                f = "(fast-mult-iterative %d %d)" % (a, b)
                ret = self.eval(f).split()
                if ret[0] != ";Value:":
                    return "%s should have returned a value instead of %s" % (
                        f, " ".join(ret))
                if int(ret[1]) != a * b:
                    errors.append("%s is not the correct answer for %s" % (
                        ret[1], f
                    ))
        return ", ".join(errors)

    def eval_1_19(self, fpath):
        # Load provided code
        self.eval("(define (even? n) (= (remainder n 2) 0))")
        self.eval("(define (double x) (+ x x))")
        self.eval("(define (halve x) (/ x 2))")
        self.load(fpath)

        def fib(n):
            return int(
                ((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (
                    2 ** n * math.sqrt(5)))

        errors = []
        for n in range(15):
            f = "(fib %d)" % n
            ret = self.eval(f).split()
            if ret[0] != ";Value:":
                return "%s should have returned a value instead of %s" % (
                    f, " ".join(ret))
            if int(ret[1]) != fib(n):
                errors.append("%s is not the correct answer for %s" % (
                    ret[1], f
                ))
        return ", ".join(errors)
