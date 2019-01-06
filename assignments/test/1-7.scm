(define (average x y) (/ (+ x y) 2))
(define (improve guess x) (average guess (/ x guess)))
(define (goodenough? guess old-guess x)
  (<= (abs (- old-guess guess)) (* guess .001)))
(define (sqrt-iter guess old-guess x)
  (if (goodenough? guess old-guess x)
      guess
      (sqrt-iter (improve guess x) guess x)))
(define (sqrt x) (sqrt-iter 1.0 2.0 x))
