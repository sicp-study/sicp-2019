#|
The problem with finding square root of very small numbers using this method is that The logic prevents the improvement of the guess past the 0.001 hardcoded threshold since the radicant itself is much smaller than this threshold.

The problem with finding square root of very large numbers is that the code never stops running. This is because floats have a fixed precision. After a certain point, the guesses are unable to guess the square root of a number within 0.001 of the answer. At that point, they alternate between the two guesses, both of whose squares are more than 0.001 away from the argument.
|#

(define (average x y) (/ (+ x y) 2))
(define (improve guess x) (average guess (/ x guess)))
(define (goodenough? guess prev-guess)
  (<= (abs (- prev-guess guess)) (/ guess 100)))
(define (sqrt-iter guess prev-guess x)
  (if (goodenough? guess prev-guess)
      guess
      (sqrt-iter (improve guess x) guess x)))
(define (sqrt x) (sqrt-iter 1.0 0 x))
