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
import os

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

    common_2_1 = """
(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))
(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (denom x) (denom y))))
(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))
(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (denom x) (numer y))))
(define (equal-rat? x y)
  (= (* (numer x) (denom y))
     (* (numer y) (denom x))))
;; abstraction layer
(define (make-rat n d) (cons n d))
(define (numer x) (car x))
(define (denom x) (cdr x))
(define (print-rat x)
  (newline)
  (display (numer x))
  (display "/")
  (display (denom x)))

(define (average a b) (/ (+ a b) 2))
(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))
"""

    def eval_2_1(self, fpath):
        self.load(self.common_2_1)
        self.load(fpath)
        errors = []
        for n, d, res in ((3, 4, "3/4"), (-3, 4, "-3/4"), (3, -4, "-3/4"),
                          (-3, -4, "3/4")):
            f = "(print-rat (make-rat %d %d))" % (n, d)
            try:
                r = self.eval(f)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_2_2(self, fpath):
        self.load(self.common_2_1)
        self.load(fpath)
        errors = []
        for p1, p2, res in (("0 0", "2 2", "(1,1)"), ):
            f = "(print-point (midpoint-segment (make-segment %s %s)))" % (
                "(make-point %s)" % p1, "(make-point %s)" % p2)
            try:
                r = self.eval(f)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_2_3(self, fpath):
        self.load("""
(define (make-segment x y) (cons x y))
(define (start-segment s) (car s))
(define (end-segment s) (cdr s))

(define (make-point x y) (cons x y))
(define (x-point p) (car p))
(define (y-point p) (cdr p))

(define (midpoint-segment s)
  (make-point
    (average (x-point (start-segment s))
             (x-point (end-segment s)))
    (average (y-point (start-segment s))
             (y-point (end-segment s)))))
""")
        self.load(fpath)
        errors = []
        for p1, p2, perim, area in (("1 1", "5 2", 10, 4), ):
            for func, res in (("perimeter", perim), ("area", area)):
                f = "(%s-rectangle (make-rectangle %s %s))" % (
                    func, "(make-point %s)" % p1, "(make-point %s)" % p2)
                try:
                    r = self.eval_value(f, int)
                    if r != res:
                        errors.append("%s is not the correct answer for %s" % (
                            r, f))
                except RuntimeError as e:
                    errors.append(str(e))
        return ", ".join(errors)

    def eval_2_5(self, fpath):
        self.load(fpath)
        errors = []
        for a, b in ((0, 1), (1, 0), (4, 2), (2, 3)):
            f = "(cons %d %d)" % (a, b)
            res = (2**a) * (3**b)
            try:
                r = self.eval_value(f, int)
                if r != res:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
            f = "(cdr %d)" % res
            try:
                r = self.eval_value(f, int)
                if r != b:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
            f = "(car %d)" % res
            try:
                r = self.eval_value(f, int)
                if r != a:
                    errors.append("%s is not the correct answer for %s" % (
                        r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    common_interval = """
(define (make-interval a b) (cons a b))
(define (add-interval x y)
  (make-interval (+ (lower-bound x) (lower-bound y))
                 (+ (upper-bound x) (upper-bound y))))
(define (mul-interval x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))
(define (div-interval x y)
  (mul-interval x
                (make-interval (/ 1.0 (upper-bound y))
                               (/ 1.0 (lower-bound y)))))
"""

    def eval_2_7(self, fpath):
        self.load(self.common_interval)
        self.load(fpath)
        errors = []
        for lower, upper in ((-1, 2), (1, 3), (0, 5)):
            for f, expected in (("lower", lower), ("upper", upper)):
                f = "(%s-bound (make-interval %d %d))" % (f, lower, upper)
                try:
                    r = self.eval_value(f, int)
                    if r != expected:
                        errors.append("%s is not the correct answer for %s" % (
                            r, f))
                except RuntimeError as e:
                    errors.append(str(e))

        return ", ".join(errors)

    def eval_2_8(self, fpath):
        # TODO...
        return

    def eval_2_10(self, fpath):
        # TODO
        return

    def eval_2_11(self, fpath):
        self.load("""
(define (make-interval x y) (cons x y))
(define (upper-bound i) ((if (> (car i) (cdr i)) car cdr) i))
(define (lower-bound i) ((if (> (car i) (cdr i)) cdr car) i))
(define (original-mul x y)
  (let ((p1 (* (lower-bound x) (lower-bound y)))
        (p2 (* (lower-bound x) (upper-bound y)))
        (p3 (* (upper-bound x) (lower-bound y)))
        (p4 (* (upper-bound x) (upper-bound y))))
    (make-interval (min p1 p2 p3 p4)
                   (max p1 p2 p3 p4))))
""")
        self.load(fpath)
        errors = []
        cases = ((-2, -1), (-1, 0), (-2, 2), (0, 0), (0, 1), (1, 2))
        for x in cases:
            for y in cases:
                op = "(make-interval %d %d) (make-interval %d %d)" % (
                    x[0], x[1], y[0], y[1])
                expected_lower = self.eval_value(
                    "(lower-bound (original-mul %s))" % op, int)
                expected_upper = self.eval_value(
                    "(upper-bound (original-mul %s))" % op, int)
                try:
                    lower = self.eval_value(
                        "(lower-bound (mul-interval %s))" % op, int)
                    upper = self.eval_value(
                        "(upper-bound (mul-interval %s))" % op, int)
                    if lower != expected_lower or upper != expected_upper:
                        errors.append(
                            "(%s %s) is not the correct answer for %s" % (
                                lower, upper, "(mul-interval %s)" % op))
                except RuntimeError as e:
                    errors.append(str(e))
        return ", ".join(errors)

    def eval_2_12(self, fpath):
        self.load(self.common_interval)
        self.load("""
(define (upper-bound i) ((if (> (car i) (cdr i)) car cdr) i))
(define (lower-bound i) ((if (> (car i) (cdr i)) cdr car) i))
(define (make-center-width c w)
  (make-interval (- c w) (+ c w)))
(define (center i)
  (/ (+ (lower-bound i) (upper-bound i)) 2))
(define (width i)
  (/ (- (upper-bound i) (lower-bound i)) 2))
""")
        self.load(fpath)
        errors = []
        for center, percent in ((100, 10.), (42, 10.), (1, .5)):
            op = "(percent (make-center-percent %d %f))" % (center, percent)
            try:
                r = round(self.eval_value(op, float), 3)
                if r != percent:
                    errors.append("%s is not the correct answer for %s" % (
                        r, op))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_2_17(self, fpath):
        self.load(fpath)
        f = "(last-pair (list 44 43 42))"
        try:
            r = self.eval_value(f, list)
            if r != [42]:
                return "%s is not the correct answer for %s" % (r, f)
        except RuntimeError as e:
            return str(e)

    def eval_2_18(self, fpath):
        self.load(fpath)
        f = "(reverse (list 4 3 2 1))"
        try:
            r = self.eval_value(f, list)
            if r != [1, 2, 3, 4]:
                return "%s is not the correct answer for %s" % (r, f)
        except RuntimeError as e:
            return str(e)

    def eval_2_19(self, fpath):
        self.load("""
(define us-coins (list 50 25 10 5 1))
(define uk-coins (list 100 50 20 10 5 2 1 0.5))
(define (cc amount coin-values)
  (cond ((= amount 0) 1)
        ((or (< amount 0) (no-more? coin-values)) 0)
        (else
         (+ (cc amount
                (except-first-denomination coin-values))
            (cc (- amount
                   (first-denomination coin-values))
                coin-values)))))
""")
        self.load(fpath)
        f = "(cc 100 us-coins)"
        try:
            r = self.eval_value(f, int)
            if r != 292:
                return "%s is not the correct answer for %s" % (r, f)
        except RuntimeError as e:
            return str(e)

    def eval_2_20(self, fpath):
        self.load(fpath)
        errors = []
        for f, e in (("(same-parity 1 2 3 4 5 6 7)", [1, 3, 5, 7]),
                     ("(same-parity 2 3 4 5 6 7)", [2, 4, 6])):
            try:
                r = self.eval_value(f, list)
                if r != e:
                    errors.append(
                        "%s is not the correct answer for %s" % (r, f))
            except RuntimeError as e:
                errors.append(str(e))
        return ", ".join(errors)

    def eval_2_28(self, fpath):
        self.load(fpath)
        f = "(fringe (list (list 1 2) (list 3 4)))"
        r = self.eval_value(f, list)
        if r != [1, 2, 3, 4]:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_29(self, fpath):
        self.load("""
(define (make-mobile left right) (list left right))
(define (make-branch length structure) (list length structure))
""")
        self.load(fpath)
        f = """
(total-weight (make-mobile (make-branch 1 1)
                           (make-branch 1 (make-mobile (make-branch 1 21)
                                                       (make-branch 1 22)))))
"""
        r = self.eval_value(f, int)
        if r != 44:
            return "%s is not the correct answer for %s" % (r, f)

        f = """
(balanced? (make-mobile (make-branch 5 1)
                        (make-branch 1 (make-mobile (make-branch 1 4)
                                                    (make-branch 1 1)))))
"""
        r = self.eval_value(f, str)
        if r != "#t":
            return "%s is not the correct answer for %s" % (r, f)

        f = "(balanced? (make-mobile (make-branch 5 1) (make-branch 5 5)))"
        r = self.eval_value(f, str)
        if r != "#f":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_30(self, fpath):
        self.load("""(define nil '())""")
        self.load(fpath)
        for test in ("square-tree", "square-tree-with-map"):
            f = "(%s (list 1 (list 2 (list 3 4) 5) (list 6 7)))" % test
            r = self.eval_value(f, str)
            if r != "(1 (4 (9 16) 25) (36 49))":
                return "%s is not the correct answer for %s" % (r, f)

    def eval_2_31(self, fpath):
        self.load(fpath)
        self.load("(define (square-tree tree) (tree-map square tree))")
        f = "(square-tree (list 1 (list 2 (list 3 4) 5) (list 6 7)))"
        r = self.eval_value(f, str)
        if r != "(1 (4 (9 16) 25) (36 49))":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_32(self, fpath):
        self.load(fpath)
        f = "(subsets (list 1 2 3))"
        r = self.eval_value(f, str)
        if r != "(() (3) #0=(2) #1=(2 3) (1) (1 3) (1 . #0#) (1 . #1#))":
            return "%s is not the correct answer for %s" % (r, f)

    seq_common = """
(define nil '())
(define (filter predicate sequence)
  (cond ((null? sequence) nil)
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))
(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))
(define (enumerate-interval low high)
  (if (> low high)
      nil
      (cons low (enumerate-interval (+ low 1) high))))
"""

    def eval_2_33(self, fpath):
        self.load(self.seq_common)
        self.load(fpath)
        errors = []
        f = "(map square (list 1 2 3))"
        r = self.eval_value(f, list)
        if r != [1, 4, 9]:
            errors.append("%s is not the correct answer for %s" % (r, f))
        f = "(append (list 1 2) (list 3 4))"
        r = self.eval_value(f, list)
        if r != [1, 2, 3, 4]:
            errors.append("%s is not the correct answer for %s" % (r, f))
        f = "(length (list 1 2 3 4))"
        r = self.eval_value(f, int)
        if r != 4:
            errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    def eval_2_34(self, fpath):
        self.load(self.seq_common)
        self.load(fpath)
        f = "(horner-eval 2 (list 1 3 0 5 0 1))"
        r = self.eval_value(f, int)
        if r != 79:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_35(self, fpath):
        self.load(self.seq_common)
        self.load(fpath)
        f = "(count-leaves (list 1 (list 2 (list 3 4) 5) (list 6 7)))"
        r = self.eval_value(f, int)
        if r != 7:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_36(self, fpath):
        self.load(self.seq_common)
        self.load(fpath)
        f = "(accumulate-n + 0 (list (list 1 2 3) (list 4 5 6) (list 7 8 9)))"
        r = self.eval_value(f, list)
        if r != [12, 15, 18]:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_37(self, fpath):
        self.load(self.seq_common)
        self.load("""
(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      nil
      (cons (accumulate op init (map (lambda (x) (car x)) seqs))
            (accumulate-n op init (map (lambda (x) (cdr x)) seqs)))))
""")
        self.load(fpath)
        m = "(list '(1 2 3 4) '(4 5 6 6) '(6 7 8 9))"
        v = "'(3 4 5 6)"
        errors = []
        f = "(matrix-*-vector %s %s)" % (m, v)
        r = self.eval_value(f, list)
        if r != [50, 98, 140]:
            errors.append("%s is not the correct answer for %s" % (r, f))
        f = "(transpose %s)" % m
        r = self.eval_value(f, str)
        if r != "((1 4 6) (2 5 7) (3 6 8) (4 6 9))":
            errors.append("%s is not the correct answer for %s" % (r, f))
        m = "(list '(1 2 3) '(4 5 6) '(7 8 9))"
        f = "(matrix-*-matrix %s %s)" % (m, m)
        r = self.eval_value(f, str)
        if r != "((30 36 42) (66 81 96) (102 126 150))":
            errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    def eval_2_39(self, fpath):
        self.load(self.seq_common)
        self.load("""
(define fold-right accumulate)
(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
        result
        (iter (op result (car rest))
              (cdr rest))))
  (iter initial sequence))
""")
        f = "(reverse (list 1 2 3 4))"
        r = self.eval_value(f, list)
        if r != [4, 3, 2, 1]:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_40(self, fpath):
        self.load(self.seq_common)
        self.load("""
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
(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))
(define (make-pair-sum pair)
  (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))
""")
        self.load(fpath)
        f = "(unique-pairs 3)"
        r = self.eval_value(f, str)
        if r != "((2 1) (3 1) (3 2))":
            return "%s is not the correct answer for %s" % (r, f)
        f = "(prime-sum-pairs 3)"
        r = self.eval_value(f, str)
        if r != "((2 1 3) (3 2 5))":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_41(self, fpath):
        self.load(self.seq_common)
        self.load(fpath)
        f = "(ord-triples-sum 16 42)"
        r = self.eval_value(f, str)
        if r != "((15 14 13) (16 14 12) (16 15 11))":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_54(self, fpath):
        self.load(fpath)
        errors = []
        for l1, l2, r in (("'(1 2 3)", "'(1 2 3)", True),
                          ("'(1 4 2)", "'(1 2 3)", False),
                          ("'(1 2)", "'(1 2 3)", False),
                          ("'()", "'(1 2 3)", False),
                          ("'(1 2 3 (4 5))", "'(1 2 3 (4 5))", True),
                          ("'(1 2 3 (4 6))", "'(1 2 3 (4 5))", False),
                          ("'((1 2) (3 8) (4 5))",
                           "'((1 2) (3 8) (4 5))", True)):
            for v1, v2 in ((l1, l2), (l2, l1)):
                f = "(equal? %s %s)" % (v1, v2)
                res = self.eval_value(f, bool)
                if res != r:
                    errors.append(
                        "%s is not the correct answer for %s" % (res, f))
        return "\n".join(errors)

    deriv_common = """
(define (memq item x)
  (cond ((null? x) false)
        ((eq? item (car x)) x)
        (else (memq item (cdr x)))))
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))
(define (sum? x)
  (and (pair? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))
(define (product? x)
  (and (pair? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))
(define (=number? exp num)
  (and (number? exp) (= exp num)))
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (deriv exp var)
  (cond ((number? exp) 0)
        ((variable? exp)
         (if (same-variable? exp var) 1 0))
        ((sum? exp)
         (make-sum (deriv (addend exp) var)
                   (deriv (augend exp) var)))
        ((product? exp)
         (make-sum
           (make-product (multiplier exp)
                         (deriv (multiplicand exp) var))
           (make-product (deriv (multiplier exp) var)
                         (multiplicand exp))))
        (else
         (error "unknown expression type -- DERIV" exp))))
"""

    def eval_2_56(self, fpath):
        self.load(self.deriv_common)
        self.load(fpath)
        f = "(deriv '(** x c) 'x)"
        r = self.eval_value(f, str)
        if r != "(* c (** x (+ c -1)))":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_57(self, fpath):
        self.load(self.deriv_common)
        self.load(fpath)
        errors = []
        expected = "(+ (* x y) (* y (+ x 3)))"
        for i in ("'(* (* x y) (+ x 3))", "'(* x y (+ x 3))"):
            f = "(deriv %s 'x)" % i
            r = self.eval_value(f, str)
            if r != expected:
                errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    def eval_2_58(self, fpath):
        self.load(self.deriv_common)
        self.load(fpath)
        errors = []
        for d, res in (
                ("(x * (y * (x + 4 + 2)))", "((x * y) + (y * (x + 4 + 2)))"),
                ("((x * y) * (x + 3))", "((x * y) + (y * (x + 3)))")):
            f = "(deriv '%s 'x)" % (d)
            r = self.eval_value(f, str)
            if r != res:
                errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    set_unordered_common = """
(define (element-of-set? x set)
  (cond ((null? set) false)
        ((equal? x (car set)) true)
        (else (element-of-set? x (cdr set)))))
(define (adjoin-set x set)
  (if (element-of-set? x set)
      set
      (cons x set)))
(define (intersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
        ((element-of-set? (car set1) set2)
         (cons (car set1)
               (intersection-set (cdr set1) set2)))
        (else (intersection-set (cdr set1) set2))))
"""

    def eval_2_59(self, fpath):
        self.load(self.set_unordered_common)
        self.load(fpath)
        errors = []
        for s1, s2 in [(set(), set()), (set(), {1, 2}), ({1, 2}, set()),
                       ({1, 2, 3}, {2, 3, 4})]:
            f = "(union-set (list %s) (list %s))" % (
                " ".join(map(str, s1)), " ".join(map(str, s2)))
            r = set(self.eval_value(f, list))
            if r != s1.union(s2):
                errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    def eval_2_62(self, fpath):
        self.load(fpath)
        errors = []
        for s1, s2 in [([], []), ([], [1, 2]), ([1, 2, 4], [1, 2, 3])]:
            for t1, t2 in ((s1, s2), (s2, s1)):
                f = "(union-set (list %s) (list %s))" % (
                    " ".join(map(str, s1)), " ".join(map(str, s2)))
                r = self.eval_value(f, list)
                l = sorted(list(set(s1).union(set(s2))))
                if r != l:
                    errors.append(
                        "%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    set_tree_common = """
(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right)
  (list entry left right))
(define (element-of-set? x set)
  (cond ((null? set) false)
        ((= x (entry set)) true)
        ((< x (entry set))
         (element-of-set? x (left-branch set)))
        ((> x (entry set))
         (element-of-set? x (right-branch set)))))
(define (adjoin-set x set)
  (cond ((null? set) (make-tree x '() '()))
        ((= x (entry set)) set)
        ((< x (entry set))
         (make-tree (entry set)
                    (adjoin-set x (left-branch set))
                    (right-branch set)))
        ((> x (entry set))
         (make-tree (entry set)
                    (left-branch set)
                    (adjoin-set x (right-branch set))))))
(define (tree->list tree)
  (define (copy-to-list tree result-list)
    (if (null? tree)
        result-list
        (copy-to-list (left-branch tree)
                      (cons (entry tree)
                            (copy-to-list (right-branch tree)
                                          result-list)))))
  (copy-to-list tree '()))
(define (list->tree elements)
  (car (partial-tree elements (length elements))))

(define (partial-tree elts n)
  (if (= n 0)
      (cons '() elts)
      (let ((left-size (quotient (- n 1) 2)))
        (let ((left-result (partial-tree elts left-size)))
          (let ((left-tree (car left-result))
                (non-left-elts (cdr left-result))
                (right-size (- n (+ left-size 1))))
            (let ((this-entry (car non-left-elts))
                  (right-result (partial-tree (cdr non-left-elts)
                                              right-size)))
              (let ((right-tree (car right-result))
                    (remaining-elts (cdr right-result)))
                (cons (make-tree this-entry left-tree right-tree)
                      remaining-elts))))))))
(define (union-set set1 set2)
  (cond ((null? set1) set2)
        ((null? set2) set1)
        (else (let ((x (car set1)) (y (car set2)))
          (cond ((= x y) (cons x (union-set (cdr set1) (cdr set2))))
                ((< x y) (cons x (union-set (cdr set1) set2)))
                (else (cons y (union-set set1 (cdr set2)))))))))
(define (intersection-set set1 set2)
  (if (or (null? set1) (null? set2))
      '()
      (let ((x1 (car set1)) (x2 (car set2)))
        (cond ((= x1 x2)
               (cons x1
                     (intersection-set (cdr set1)
                                       (cdr set2))))
              ((< x1 x2)
               (intersection-set (cdr set1) set2))
              ((< x2 x1)
               (intersection-set set1 (cdr set2)))))))
"""

    def eval_2_65(self, fpath):
        self.load(self.set_tree_common)
        self.load(fpath)
        errors = []
        for s1, s2 in [([], []), ([], [1, 2]), ([1, 2, 4], [1, 2, 3])]:
            for t1, t2 in ((s1, s2), (s2, s1)):
                f = ("(tree->list (union-set-tree "
                     "(list->tree '(%s)) (list->tree '(%s))))" % (
                         " ".join(map(str, s1)), " ".join(map(str, s2))))
                r = self.eval_value(f, list)
                l = sorted(list(set(s1).union(set(s2))))
                if r != l:
                    errors.append(
                        "%s is not the correct answer for %s" % (r, f))
                f = ("(tree->list (intersection-set-tree "
                     "(list->tree '(%s)) (list->tree '(%s))))" % (
                         " ".join(map(str, s1)), " ".join(map(str, s2))))
                r = self.eval_value(f, list)
                l = sorted(list(set(s1).intersection(set(s2))))
                if r != l:
                    errors.append(
                        "%s is not the correct answer for %s" % (r, f))
                return ", ".join(errors)

    def eval_2_66(self, fpath):
        self.load("""
(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right)
  (list entry left right))
(define (make-item key value) (cons key value))
(define (key entry) (car entry))
(define (value entry) (cdr entry))
(define tree (make-tree (make-item 7 'g)
                         (make-tree (make-item 3 'c)
                                    (make-tree (make-item 1 'a) '() '())
                                    (make-tree (make-item 5 'e) '() '()))
                         (make-tree (make-item 9 'i) '()
                                    (make-tree (make-item 11 'k) '() '()))))
""")
        self.load(fpath)
        errors = []
        for k, v in ([7, "g"], [5, "e"], [11, "k"]):
            f = "(lookup %s tree)" % k
            r = self.eval_value(f, str)
            if r != "(%s . %s)" % (k, v):
                errors.append(
                    "%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    common_huffman_tree = """

(define (make-leaf symbol weight)
  (list 'leaf symbol weight))
(define (leaf? object)
  (eq? (car object) 'leaf))
(define (symbol-leaf x) (cadr x))
(define (weight-leaf x) (caddr x))
(define (make-code-tree left right)
  (list left
        right
        (append (symbols left)
                (symbols right))
        (+ (weight left) (weight right))))

(define (left-branch tree) (car tree))
(define (right-branch tree) (cadr tree))

(define (symbols tree)
  (if (leaf? tree)
      (list (symbol-leaf tree))
      (caddr tree)))

(define (weight tree)
  (if (leaf? tree)
      (weight-leaf tree)
      (cadddr tree)))

(define (decode bits tree)
  (define (decode-1 bits current-branch)
    (if (null? bits)
        '()
        (let ((next-branch
               (choose-branch
                (car bits)
                current-branch)))
          (if (leaf? next-branch)
              (cons
               (symbol-leaf next-branch)
               (decode-1 (cdr bits) tree))
              (decode-1 (cdr bits)
                        next-branch)))))
  (decode-1 bits tree))

(define (choose-branch bit branch)
  (cond ((= bit 0) (left-branch branch))
        ((= bit 1) (right-branch branch))
        (else (error "bad bit:
               CHOOSE-BRANCH" bit))))

(define (adjoin-set x set)
  (cond ((null? set) (list x))
        ((< (weight x) (weight (car set)))
         (cons x set))
        (else
         (cons (car set)
               (adjoin-set x (cdr set))))))

(define (make-leaf-set pairs)
  (if (null? pairs)
      '()
      (let ((pair (car pairs)))
        (adjoin-set
         (make-leaf (car pair)    ; symbol
                    (cadr pair))  ; frequency
         (make-leaf-set (cdr pairs))))))

(define sample-tree
  (make-code-tree
   (make-leaf 'A 4)
   (make-code-tree
    (make-leaf 'B 2)
    (make-code-tree
     (make-leaf 'D 1)
     (make-leaf 'C 1)))))

(define sample-message
  '(0 1 1 0 0 1 0 1 0 1 1 1 0))


(define (encode message tree)
  (if (null? message)
      '()
      (append
       (encode-symbol (car message)
                      tree)
       (encode (cdr message) tree))))

(define (element-of-set? x set)
  (cond ((null? set) false)
        ((= x (entry set)) true)
        ((< x (entry set))
         (element-of-set?
          x
          (left-branch set)))
        ((> x (entry set))
         (element-of-set?
          x
          (right-branch set)))))

"""

    def eval_2_68(self, fpath):
        self.load(self.common_huffman_tree)
        self.load(fpath)
        f = "(encode '(a d a b b c a) sample-tree)"
        r = self.eval_value(f, str)
        if r != "(0 1 1 0 0 1 0 1 0 1 1 1 0)":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_69(self, fpath):
        self.load(self.common_huffman_tree)
        self.load("""
(define (encode-symbol symbol tree)
  (define (element-of-set? x set)
    (cond ((null? set) false)
          ((equal? x (car set)) true)
          (else (element-of-set? x (cdr set)))))

  (define (iter branch result)
    (cond ((leaf? branch)
           (if (eq? symbol (symbol-leaf branch))
               (reverse result)
               (error "symbol not found: " symbol)))
          ((element-of-set? symbol (symbols (right-branch branch)))
           (iter (right-branch branch) (cons 1 result)))
          ((element-of-set? symbol (symbols (left-branch branch)))
           (iter (left-branch branch) (cons 0 result)))
          (else (error "symbol not found: " symbol))))
  (iter tree '()))

(define (generate-huffman-tree pairs)
  (successive-merge
   (make-leaf-set pairs)))
""")
        self.load(fpath)
        t = "(define test-tree " \
            "(generate-huffman-tree '((S 4) (I 2) (C 1) (P 1))))"
        self.eval(t)
        f = "(decode (encode '(s i c p) test-tree) test-tree)"
        r = self.eval_value(f, str)
        if r != "(s i c p)":
            return "%s is not the correct answer for %s %s" % (r, t, f)

    generic_operations_common = """
(define *op-table* (make-hash-table))

(define (put op type proc)
  (hash-table/put! *op-table* (list op type) proc))

(define (get op type)
  (hash-table/get *op-table* (list op type) #f))

(define (put-coercion source-type target-type proc)
  (put 'coercion (list source-type target-type) proc))

(define (get-coercion source-type target-type)
  (get 'coercion (list source-type target-type)))

(define (attach-tag type-tag contents)
  (cons type-tag contents))

(define (type-tag datum)
  (if (pair? datum)
      (car datum)
      (error "Bad tagged datum:
              TYPE-TAG" datum)))

(define (contents datum)
  (if (pair? datum)
      (cdr datum)
      (error "Bad tagged datum:
              CONTENTS" datum)))

(define (apply-generic op . args)
  (let ((type-tags (map type-tag args)))
    (let ((proc (get op type-tags)))
      (if proc
          (apply proc (map contents args))
          (error
            "No method for these types:
             APPLY-GENERIC"
            (list op type-tags))))))

(define (add x y) (apply-generic 'add x y))
(define (sub x y) (apply-generic 'sub x y))
(define (mul x y) (apply-generic 'mul x y))
(define (div x y) (apply-generic 'div x y))

(define (install-scheme-number-package)
  (define (tag x)
    (attach-tag 'scheme-number x))
  (put 'add '(scheme-number scheme-number)
       (lambda (x y) (tag (+ x y))))
  (put 'sub '(scheme-number scheme-number)
       (lambda (x y) (tag (- x y))))
  (put 'mul '(scheme-number scheme-number)
       (lambda (x y) (tag (* x y))))
  (put 'div '(scheme-number scheme-number)
       (lambda (x y) (tag (/ x y))))
  (put 'make 'scheme-number
       (lambda (x) (tag x)))
  'done)
(install-scheme-number-package)
(define (make-scheme-number n)
  ((get 'make 'scheme-number) n))

(define (install-rational-package)
  ;; internal procedures
  (define (numer x) (car x))
  (define (denom x) (cdr x))
  (define (make-rat n d)
    (let ((g (gcd n d)))
      (cons (/ n g) (/ d g))))
  (define (add-rat x y)
    (make-rat (+ (* (numer x) (denom y))
                 (* (numer y) (denom x)))
              (* (denom x) (denom y))))
  (define (sub-rat x y)
    (make-rat (- (* (numer x) (denom y))
                 (* (numer y) (denom x)))
              (* (denom x) (denom y))))
  (define (mul-rat x y)
    (make-rat (* (numer x) (numer y))
              (* (denom x) (denom y))))
  (define (div-rat x y)
    (make-rat (* (numer x) (denom y))
              (* (denom x) (numer y))))
  ;; interface to rest of the system
  (define (tag x) (attach-tag 'rational x))
  (put 'add '(rational rational)
       (lambda (x y) (tag (add-rat x y))))
  (put 'sub '(rational rational)
       (lambda (x y) (tag (sub-rat x y))))
  (put 'mul '(rational rational)
       (lambda (x y) (tag (mul-rat x y))))
  (put 'div '(rational rational)
       (lambda (x y) (tag (div-rat x y))))
  (put 'make 'rational
       (lambda (n d) (tag (make-rat n d))))
  'done)
(install-rational-package)
(define (make-rational n d)
  ((get 'make 'rational) n d))

(define (install-rectangular-package)
  ;; internal procedures
  (define (real-part z) (car z))
  (define (imag-part z) (cdr z))
  (define (make-from-real-imag x y)
    (cons x y))
  (define (magnitude z)
    (sqrt (+ (square (real-part z))
             (square (imag-part z)))))
  (define (angle z)
    (atan (imag-part z) (real-part z)))
  (define (make-from-mag-ang r a)
    (cons (* r (cos a)) (* r (sin a))))
  ;; interface to the rest of the system
  (define (tag x)
    (attach-tag 'rectangular x))
  (put 'real-part '(rectangular) real-part)
  (put 'imag-part '(rectangular) imag-part)
  (put 'magnitude '(rectangular) magnitude)
  (put 'angle '(rectangular) angle)
  (put 'make-from-real-imag 'rectangular
       (lambda (x y)
         (tag (make-from-real-imag x y))))
  (put 'make-from-mag-ang 'rectangular
       (lambda (r a)
         (tag (make-from-mag-ang r a))))
  'done)
(install-rectangular-package)

(define (install-complex-package)
  ;; imported procedures from rectangular
  ;; and polar packages
  (define (make-from-real-imag x y)
    ((get 'make-from-real-imag
          'rectangular)
     x y))
  (define (make-from-mag-ang r a)
    ((get 'make-from-mag-ang 'polar)
     r a))
  ;; internal procedures
  (define (add-complex z1 z2)
    (make-from-real-imag
     (+ (real-part z1) (real-part z2))
     (+ (imag-part z1) (imag-part z2))))
  (define (sub-complex z1 z2)
    (make-from-real-imag
     (- (real-part z1) (real-part z2))
     (- (imag-part z1) (imag-part z2))))
  (define (mul-complex z1 z2)
    (make-from-mag-ang
     (* (magnitude z1) (magnitude z2))
     (+ (angle z1) (angle z2))))
  (define (div-complex z1 z2)
    (make-from-mag-ang
     (/ (magnitude z1) (magnitude z2))
     (- (angle z1) (angle z2))))
  ;; interface to rest of the system
  (define (tag z) (attach-tag 'complex z))
  (put 'add '(complex complex)
       (lambda (z1 z2)
         (tag (add-complex z1 z2))))
  (put 'sub '(complex complex)
       (lambda (z1 z2)
         (tag (sub-complex z1 z2))))
  (put 'mul '(complex complex)
       (lambda (z1 z2)
         (tag (mul-complex z1 z2))))
  (put 'div '(complex complex)
       (lambda (z1 z2)
         (tag (div-complex z1 z2))))
  (put 'make-from-real-imag 'complex
       (lambda (x y)
         (tag (make-from-real-imag x y))))
  (put 'make-from-mag-ang 'complex
       (lambda (r a)
         (tag (make-from-mag-ang r a))))
  (define (real-part z)
    (apply-generic 'real-part z))
  (define (imag-part z)
    (apply-generic 'imag-part z))
  (define (magnitude z)
    (apply-generic 'magnitude z))
  (define (angle z)
    (apply-generic 'angle z))
  (put 'real-part '(complex) real-part)
  (put 'imag-part '(complex) imag-part)
  (put 'magnitude '(complex) magnitude)
  (put 'angle '(complex) angle)
  'done)
(install-complex-package)
(define (make-complex-from-real-imag x y)
  ((get 'make-from-real-imag 'complex) x y))
(define (make-complex-from-mag-ang r a)
  ((get 'make-from-mag-ang 'complex) r a))
(define (real-part x)
  ((get 'real-part '(complex)) x))
(define (imag-part x)
  ((get 'imag-part '(complex)) x))
(define (make-real x)
  (attach-tag 'real x))

(define (attach-tag type-tag contents)
  (if (eq? type-tag 'scheme-number)
      contents
      (cons type-tag contents)))
(define (type-tag datum)
  (cond ((number? datum) 'scheme-number)
        ((pair? datum) (car datum))
        (else (error "Bad tagged datum: TYPE-TAG" datum))))
(define (contents datum)
  (cond ((number? datum) datum)
        ((pair? datum) (cdr datum))
        (else (error "Bad tagged datum: CONTENTS" datum))))

(define (numer x) (car x))
(define (denom x) (cdr x))

(define (scheme-number->complex n) (make-complex-from-real-imag (contents n) 0))
(put-coercion 'scheme-number 'complex scheme-number->complex)

"""

    def eval_2_78(self, fpath):
        self.load(self.generic_operations_common)
        self.load(fpath)
        f = "(add 40 2)"
        r = self.eval_value(f, int)
        if r != 42:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_79(self, fpath):
        self.load(self.generic_operations_common)
        self.load(fpath)
        o = "(make-rational (make-scheme-number 4) (make-scheme-number 2))"
        f = "(equ? %s %s)" % (o, o)
        r = self.eval_value(f, str)
        if r != "#t":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_80(self, fpath):
        self.load(self.generic_operations_common)
        self.load(fpath)
        f = "(=zero? (make-complex-from-real-imag 0 0))"
        r = self.eval_value(f, str)
        if r != "#t":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_82(self, fpath):
        self.load(self.generic_operations_common)
        self.load(fpath)
        f = "(apply-generic 'add 1 (make-complex-from-real-imag 1 2))"
        r = self.eval_value(f, str)
        if r != "(complex rectangular 2 . 2)":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_83(self, fpath):
        self.load(self.generic_operations_common)
        self.load(fpath)
        f = "(raise 42)"
        r = self.eval_value(f, str)
        if r != "(rational 42 . 1)":
            return "%s is not the correct answer for %s" % (r, f)

    common_raise = """
(put 'raise '(scheme-number) (lambda (x) (make-rational x 1)))
(put 'raise '(rational) (lambda (x) (make-real (/ (numer x) (denom x)))))
(put 'raise '(real) (lambda (x) (make-complex-from-real-imag x 0)))
(define (raise x) (apply-generic 'raise x))
"""

    def eval_2_84(self, fpath):
        self.load(self.generic_operations_common)
        self.load(self.common_raise)
        self.load(fpath)
        f = "(apply-generic 'add 1 (make-rational 4 2))"
        r = self.eval_value(f, str)
        if r != "(rational 3 . 1)":
            return "%s is not the correct answer for %s" % (r, f)

    common_equ = """
(define (equ? x y) (apply-generic 'equ? x y))
(put 'equ? '(scheme-number scheme-number) equal?)
(put 'equ? '(rational rational)
     (lambda (x y) (and (equ? (denom x) (denom y)) (equ? (numer x) (numer y)))))
(put 'equ? '(complex complex)
     (lambda (x y) (and (equ? (real-part x) (real-part y))
                   (equ? (imag-part x) (imag-part y)))))
"""

    def eval_2_85(self, fpath):
        self.load(self.generic_operations_common)
        self.load(self.common_raise)
        self.load(self.common_equ)
        if os.path.exists(fpath.replace('85', '84')):
            self.load(fpath.replace('85', '84'))
        self.load(fpath)
        f = "(apply-generic 'add 1 (make-rational 4 1))"
        r = self.eval_value(f, int)
        if r != 5:
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_86(self, fpath):
        self.load(self.generic_operations_common)
        self.load(self.common_raise)
        self.load(self.common_equ)
        if os.path.exists(fpath.replace('86', '84')):
            self.load(fpath.replace('86', '84'))
        if os.path.exists(fpath.replace('86', '85')):
            self.load(fpath.replace('86', '85'))
        self.load(fpath)
        c = "(make-rational 4 1)"
        f = "(apply-generic 'add 3 (make-complex-from-real-imag %s 2))" % c
        r = self.eval_value(f, str)
        if r != "(complex rectangular 7 . 2)":
            return "%s is not the correct answer for %s" % (r, f)

    poly_common = """
(define (add-poly p1 p2)
  (if (same-variable? (variable p1)
                      (variable p2))
      (make-poly
       (variable p1)
       (add-terms (term-list p1)
                  (term-list p2)))
      (error "Polys not in same var:
              ADD-POLY"
             (list p1 p2))))

(define (mul-poly p1 p2)
  (if (same-variable? (variable p1)
                      (variable p2))
      (make-poly
       (variable p1)
       (mul-terms (term-list p1)
                  (term-list p2)))
      (error "Polys not in same var:
              MUL-POLY"
             (list p1 p2))))

(define (add-terms L1 L2)
  (cond ((empty-termlist? L1) L2)
        ((empty-termlist? L2) L1)
        (else
         (let ((t1 (first-term L1))
               (t2 (first-term L2)))
           (cond ((> (order t1) (order t2))
                  (adjoin-term
                   t1
                   (add-terms (rest-terms L1)
                              L2)))
                 ((< (order t1) (order t2))
                  (adjoin-term
                   t2
                   (add-terms
                    L1
                    (rest-terms L2))))
                 (else
                  (adjoin-term
                   (make-term
                    (order t1)
                    (add (coeff t1)
                         (coeff t2)))
                   (add-terms
                    (rest-terms L1)
                    (rest-terms L2)))))))))

(define (mul-terms L1 L2)
  (if (empty-termlist? L1)
      (the-empty-termlist)
      (add-terms
       (mul-term-by-all-terms
        (first-term L1) L2)
       (mul-terms (rest-terms L1) L2))))

(define (mul-term-by-all-terms t1 L)
  (if (empty-termlist? L)
      (the-empty-termlist)
      (let ((t2 (first-term L)))
        (adjoin-term
         (make-term
          (+ (order t1) (order t2))
          (mul (coeff t1) (coeff t2)))
         (mul-term-by-all-terms
          t1
          (rest-terms L))))))


(define (adjoin-term term term-list)
  (if (=zero? (coeff term))
      term-list
      (cons term term-list)))
(define (the-empty-termlist) '())
(define (first-term term-list) (car term-list))
(define (rest-terms term-list) (cdr term-list))
(define (empty-termlist? term-list)
  (null? term-list))
(define (make-term order coeff)
  (list order coeff))
(define (order term) (car term))
(define (coeff term) (cadr term))
(define (make-poly variable term-list)
  (cons variable term-list))
(define (variable p) (car p))
(define (term-list p) (cdr p))

(define (install-polynomial-package)
  ;; interface to rest of the system
  (define (tag p) (attach-tag 'polynomial p))
  (put 'add '(polynomial polynomial)
       (lambda (p1 p2)
         (tag (add-poly p1 p2))))
  (put 'mul '(polynomial polynomial)
       (lambda (p1 p2)
         (tag (mul-poly p1 p2))))
  (put 'make 'polynomial
       (lambda (var terms)
         (tag (make-poly var terms))))
  'done)
(install-polynomial-package)
(define (make-polynomial var terms)
  ((get 'make 'polynomial) var terms))
"""
    zero_common = """
(define (=zero? x) (apply-generic '=zero? x))
(put '=zero? '(scheme-number) zero?)
(put '=zero? '(rational) (lambda (x) (=zero? (numer x))))
(put '=zero? '(complex) (lambda (x) (and (=zero? (real-part x))
                                    (=zero? (imag-part x)))))
"""

    symbol_algebra = (deriv_common +
                      generic_operations_common +
                      common_equ +
                      zero_common +
                      poly_common)

    def eval_2_87(self, fpath):
        self.load(self.symbol_algebra)
        self.load(fpath)
        f = "(=zero? (make-polynomial 'x '((2 1))))"
        r = self.eval_value(f, str)
        if r != "#f":
            return "%s is not the correct answer for %s" % (r, f)
        f = "(=zero? (make-polynomial 'x '()))"
        r = self.eval_value(f, str)
        if r != "#t":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_88(self, fpath):
        self.load(self.symbol_algebra)
        self.load(fpath)
        errors = []
        for t1, t2, res in (("((1 1))", "((2 2))", "(2 2) (1 1)"),
                            ("((1 1))", "((1 2))", "(1 -1)")):
            f = "(sub (make-polynomial 'x '%s) (make-polynomial 'x '%s))" % (
                t1, t2)
            r = self.eval_value(f, str)
            if r != "(polynomial x %s)" % res:
                errors.append("%s is not the correct answer for %s" % (r, f))
        return ", ".join(errors)

    symbol_algebra_2 = symbol_algebra + """
(put '=zero? '(polynomial) (lambda (x) (empty-termlist? (term-list x))))
"""

    def eval_2_89(self, fpath):
        self.load(self.symbol_algebra_2)
        self.load(fpath)
        f = "(add (make-polynomial 'x '(2 1 0 0 0)) " + \
            "(make-polynomial 'x '(3 0 0 1 0)))"
        r = self.eval_value(f, str)
        if r != "(polynomial x 5 1 0 1 0)":
            return "%s is not the correct answer for %s" % (r, f)

    def eval_2_90(self, fpath):
        self.load(self.symbol_algebra_2)
        self.load(fpath)
        f = "(add (make-polynomial 'x '(2 1 0 0 0)) " + \
            "(make-polynomial 'x '((5 3) (1 1))))"
        r = self.eval_value(f, str)
        if r != "(polynomial x (5 5) (4 1) (1 1)":
            return "%s is not the correct answer for %s" % (r, f)
