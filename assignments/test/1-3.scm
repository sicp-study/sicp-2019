(define (square x) (* x x))
(define (square-sum x y) (+ (square x) (square y)))
(define (square-sum-larger a b c)
  (cond
   ((and (> a c) (> b c)) (square-sum a b))
   ((and (> a b) (> c b)) (square-sum a c))
   (else (square-sum b c))))
