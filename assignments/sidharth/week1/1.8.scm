(define (cube guess) (* guess guess guess))
(define (cubert-iter guess prev-guess x)
 (if (goodenough? guess prev-guess)
  guess
   (cubert-iter (improve guess x) guess x)))

(define (improve guess x)
 (/ (+ (/ x (* guess guess)) (* 2 guess)) 3))
(define (goodenough? guess prev-guess)
 (<= (abs (- prev-guess guess)) (/ guess 100)))
(define (cube-root x)
 (cubert-iter 1.0 0 x))

