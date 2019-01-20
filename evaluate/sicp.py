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

    common_1_3 = """
(define (inc x) (+ x 1))
(define (sum term a next b)
  (if (> a b)
      0
      (+ (term a)
         (sum term (next a) next b))))
(define (cube x) (* x x x))
(define (even? n) (= (remainder n 2) 0))
(define (identity x) x)
(define (smallest-divisor n)
  (define (find-divisor n test-divisor)
    (cond ((> (square test-divisor) n) n)
          ((divides? test-divisor n) test-divisor)
          (else (find-divisor n (+ test-divisor 1)))))
  (define (divides? a b)
    (= (remainder b a) 0))
  (find-divisor n 2))
(define (prime? n)
  (= n (smallest-divisor n)))
(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))
(define dx 0.00001)
(define (average a b) (/ (+ a b) 2))
    """

    def eval_1_29(self, fpath):
        # Load provided code
        self.load(self.common_1_3)
        self.load(fpath)

        errors = []
        for n, expected in ((100, 0.2499), (1000, 0.25)):
            f = "(simpson-integral cube 0 1.0 %d)" % n
            ret = self.eval(f).split()
            if ret[0] != ";Value:":
                return "%s should have returned a value instead of %s" % (
                    f, " ".join(ret))
            if abs(float(ret[1]) - n) < 0.001:
                errors.append("%s is not the correct answer for %s" % (
                    ret[1], f))
        return ", ".join(errors)

    def eval_1_30(self, fpath):
        self.load(fpath)
        errors = []
        f = "(sum (lambda (x) x) 1 1+ 10)"
        ret = self.eval_value(f, int)
        if ret != 55:
            errors.append("%s is not the correct answer for %s" % (
                ret, f))
        return ", ".join(errors)

    def eval_1_31(self, fpath):
        self.load(self.common_1_3)
        self.load(fpath)
        errors = []
        for p in ("product", "product-recursive"):
            f = "(%s identity 1 1+ 5)" % p
            try:
                ret = self.eval_value(f, int)
                if ret != 120:
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))

        for n in (0, 1, 5, 10):
            f = "(factorial %d)" % n
            try:
                ret = self.eval_value(f, int)
                if ret != math.factorial(n):
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))

        for n, expected in ((6, 3.3), (12, 3.2), (32, 3.1)):
            f = "(john-wallis-pi %d)" % n
            try:
                ret = self.eval_value(f, float)
                if abs(ret - expected) > 0.1:
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_32(self, fpath):
        self.load(fpath)
        errors = []
        for p in ("accumulate", "accumulate-recursive"):
            for op in ("+", "*"):
                if op == "+":
                    nv = 0
                    res = 15
                else:
                    nv = 1
                    res = 120
                f = "(%s %s %s (lambda (x) x) 1 1+ 5)" % (p, op, nv)
                try:
                    ret = self.eval_value(f, int)
                    if ret != res:
                        errors.append("%s is not the correct answer for %s" % (
                            ret, f))
                except RuntimeError as e:
                    errors.append(str(e))
        return ", ".join(errors)

    def eval_1_33(self, fpath):
        self.load(self.common_1_3)
        self.load(fpath)
        errors = []
        for f, expected in (("(sum-square-prime 1 10)", 88),
                            ("(sum-coprime 10)", 20)):
            try:
                ret = self.eval_value(f, int)
                if ret != expected:
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_37(self, fpath):
        self.load(fpath)
        errors = []
        for o in ("cont-frac-recursive", "cont-frac"):
            f = "(%s (lambda (i) 1.0) (lambda (i) 1.0) 10)" % o
            try:
                ret = self.eval_value(f, float)
                if (abs(ret - 1 / ((math.sqrt(5) + 1) / 2)) > 0.001):
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    cont_frac = """
(define (cont-frac n d k)
  (define (iter x result)
    (if (= x 0)
        result
        (iter (- x 1) (/ (n x)
                         (+ (d x) result)))))
  (iter k 0))
"""

    def eval_1_38(self, fpath):
        self.load(self.cont_frac)
        self.load(fpath)
        errors = []
        idx = 1
        for n in (1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8):
            f = "(euler-sequence %d)" % idx
            idx += 1
            try:
                ret = int(self.eval_value(f, float))
                if ret != n:
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))
        f = "(euler-number 20)"
        ret = self.eval_value(f, float)
        if (abs(ret - (math.e - 2)) > 0.001):
            errors.append("%s is not the correct answer for %s" % (ret, f))
        return ", ".join(errors)

    def eval_1_39(self, fpath):
        self.load(self.common_1_3)
        self.load(self.cont_frac)
        self.load(fpath)
        errors = []
        for rad in (0, 1, 2, 10, -5, 0.5):
            f = "(tan-cf %f 20)" % rad
            try:
                ret = self.eval_value(f, float)
                if abs(ret - math.tan(rad)) > 0.001:
                    errors.append("%s is not the correct answer for %s" % (
                        ret, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    newton_method = """
(define tolerance 0.00001)
(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2)) tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
          next
          (try next))))
  (try first-guess))

(define dx 0.00001)
(define (deriv g)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x))
       dx)))
(define (newton-transform g)
  (lambda (x)
    (- x (/ (g x) ((deriv g) x)))))

(define (newtons-method g guess)
  (fixed-point (newton-transform g) guess))
"""

    def eval_1_40(self, fpath):
        self.load(self.common_1_3)
        self.load(self.newton_method)
        self.load(fpath)
        errors = []
        for a, b, c in ((0, 0, 0), (0, 0, 1), (1, 2, 3), (4, 5, 1)):
            f = "(newtons-method (cubic %f %f %f) 1)" % (a, b, c)
            try:
                x = self.eval_value(f, float)
                fp = x**3 + a * x ** 2 + b * x + c
                if fp > 0.001:
                    errors.append("%s is not the correct answer for %s" % (
                        x, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_41(self, fpath):
        self.load(self.common_1_3)
        self.load(fpath)
        errors = []
        for f, res in (("((double square) 2)", 16),
                       ("(((double (double double)) inc) 5)", 21)):
            try:
                r = self.eval_value(f, int)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_42(self, fpath):
        self.load(self.common_1_3)
        self.load(fpath)
        errors = []
        for f, res in (("((compose square inc) 6)", 49),
                       ("((compose cube square) 42)", 5489031744)):
            try:
                r = self.eval_value(f, int)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_43(self, fpath):
        self.load(self.common_1_3)
        self.load("(define (compose f g) (lambda (x) (f (g x))))")
        self.load(fpath)
        errors = []
        for f, res in (("((repeated square 2) 5)", 625),
                       ("((repeated inc 16) 5)", 21)):
            try:
                r = self.eval_value(f, int)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    repeated = """
(define (compose f g) (lambda (x) (f (g x))))
(define (repeated f n)
              (if (= n 1)
                  (lambda (x) (f x))
                  (compose f (repeated f (- n 1)))))
    """

    def eval_1_44(self, fpath):
        self.load(self.common_1_3)
        self.load(self.repeated)
        self.load(fpath)
        errors = []
        for f, res in (("((smooth square) 5)", 25),
                       ("((nfold-smooth square 5) 5)", 25)):
            try:
                r = round(self.eval_value(f, float))
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_45(self, fpath):
        self.load(self.common_1_3)
        self.load(self.newton_method)
        self.load(self.repeated)
        self.load(fpath)
        errors = []
        for n in range(1, 10):
            f = "(nroot %d 42)" % n
            try:
                r = self.eval_value(f, float)
                if abs(r - 42 ** (1./n)) > 0.01:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_1_46(self, fpath):
        self.load(self.common_1_3)
        self.load(fpath)
        errors = []
        for f, res in (("(sqrt 26)", 5),
                       ("(fixed-point (lambda (x) x) 10)", 10)):
            try:
                r = round(self.eval_value(f, float))
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)
