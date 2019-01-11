(define (sum-of-squares-bigger a b c) (cond ((and (>= a c) (>= b c)) (+ (* a a) (* b b))) ((and (>= b a) (>= c a)) (+ (* b b) (* c c))) ((and (>= c b) (>= a b)) (+ (* a a) (* c c))))) 
