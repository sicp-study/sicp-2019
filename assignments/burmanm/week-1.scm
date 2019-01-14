; The Orgmode was so buggy that I had to revert to something else. No time to fight with it right now
;; Exercise 1.1
10
12
8
3
6
a
b
19
#f
4
16
6
16

;; Exercise 1.2
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 2 7) (- 6 2)))

;; Exercise 1.3
;; My Scheme "leaflet/syntax notes" had the cond answer, so I wanted to use something a bit different
(define (bigger a b) (if (> a b) a b))
(define (square x) (* x x))
(define (sum-squares x y) (+ (square x) (square y)))
;; The following actually has 4 different output possibilities, with two permutations being the same (y x), (x y)
(define (square-sum-larger x y z)
  (if (> y x)
      (sum-squares y (bigger x z))
      (sum-squares x (bigger y z))))

;; Exercise 1.4
;; Since each expression can return a new expression, the code will always return a + |b| since negative b will use operand that creates a double negative operation.

;; Exercise 1.5
;; The difference is that applicative order would evaluate the subparts first, in which case
;; the (p) would be the first to be expanded. That causes a never ending loop.
;; With normal order, the (test 0 (p)) is first evaluated to:
;; (if (= 0 0) 0 (p)) which is then executed and 0 is returned as (p) is never expanded.

;; Exercise 1.6
; The if is a special form function because it evaluates the "then" and "else" parts only after the value of the conditional is known. However, with the cond this isn't true and the "then" and "else" parts are evaluated first and only then the actual conditional. Alissa program will enter an indefinite loop since it will always evaluate sqrt-iter (which evaluates sqrt-iter, etc), even if the estimate is good enough.

;; Exercise 1.7
;; The error boundary for small numbers is too large, thus the difference of 0.001 is enough to cause
;; significant error to the end result. For example, (sqrt 0.00001) outputs 0.0313564 when the real
;; answer is close to 0.00316. The difference is already a magnitude.

;; With large numbers, the algorithm suffers from lack of exactness, since changes will return the
;; same value but this is beyond the allowed error rate. Any extra calculations will return the same
;; number and thus the loop needes re-evaluation again and again.. For example:
;; scheme@(guile-user) [1]> (sqrt 1234567890123)
;; $17 = 1111111.1061109055
;; scheme@(guile-user) [1]> (sqrt 12345678901234)
;; < will never return >

(define (sqrt x)
  (define (good-enough? guess prevguess)
    (< (abs (- guess prevguess)) 0.001))
  (define (improve guess x)
    (average guess (/ x guess)))
  (define (sqrt-iter guess prevguess x)
    (if (good-enough? guess prevguess)
        guess
        (sqrt-iter (improve guess x) guess x)))
  (sqrt-iter 1.0 0 x))

;; This works better for small numbers with the same precision. It also works better for large numbers;; as the change of 0 (when precision runs out) would then make it return.

;; Exercise 1.8

;; Calculate next approximation with a given guess.
;; x is the value which' cube-root we want and y is the initial guess required by the algo
(define (cube-root x y)
  (define (cube-next x y)
    (/ (+ (* 2 y) (/ x (square y))) 3))
  (define (good-enough? y prevy)
    (< (abs (- y prevy)) 0.001))
  (define (cube-iter x y prevy)
    (if (good-enough? y prevy)
	y
	(cube-iter x (cube-next x y) y)))
  (cube-iter x y 0))
