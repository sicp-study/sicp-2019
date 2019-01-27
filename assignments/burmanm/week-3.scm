;; Exercise 1.29

;; TODO Somewhere a bug..

;; n must be even
(define h (/ (- b a) n))
(define y (f (+ a (* k h))))
(define (multiplier c n)
  (cond ((= c n) 1)
	((= c 1) 1)
	((even? c) 4)
	(else 2)))
(define (integ f a b n)
  (define (integ-iter f a b c n sum)
    (if (> c n)
	sum
	(integ-iter f a b (+ c 1) n (+ sum (* (multiplier c n) (y c f a (h a b c)))))))
  (integ-iter f a b 1 n 0))
(define (integral f a b n)
  (* (/ (h a b n) 3) (integ f a b n)))

;; Exercise 1.30
(define (inc n) (+ n 1))

(define (sum term a next b)
  (define (iter a result)
    (if (> a b)
	result
	(iter (next a) (+ result (term a)))))
  (iter a 0))

;; Exercise 1.31

(define (product term a next b)
  (define (iter a result)
    (if (> a b)
	result
	(iter (next a) (* result (term a)))))
  (iter a 1))

(define (product-recursive term a next b)
  (if (> a b)
      1
      (+ (term a)
	 (product-recursive term (next a) next b))))

;; define factorial
;; define approx-pi

;; (define approx-pi 
;; (product 

;; Exercise 1.32

;; (accumulate combiner null-value term a next b)
(define (accumulate-recursive combiner null-value term a next b)
  (if (> a b)
      null-value
      (combiner (term a)
	 (accumulate-recursive combiner null-value term (next a) next b))))

(define (accumulate combiner null-value term a next b)
  (define (iter a result)
    (if (> a b)
	result
	(iter (next a) (combiner result (term a)))))
  (iter a null-value))

(define (sum term a next b)
  (accumulate + 0 term a next b))

(define (product term a next b)
  (accumulate * 1 term a next b))

;; Exercise 1.33

(define (filtered-accumulate filter combiner null-value term a next b)
  (define (iter a result filter)
    (if (> a b)
	result
	(iter (next a) (combiner (if (filter a) (term a) null-value)))))
  (iter a null-value filter))

(define (sum-square-prime a b)
  (filtered-accumulate prime? + 0 square a inc b))

(define (coprime? x) (= (gcd x n) 0))
(define (sum-coprime n)
  (filtered-accumulate coprime? * 1 identity 1 inc n))

;; Exercise 1.34

;; scheme@(guile-user)>(define (f g) (g 2))
;; scheme@(guile-user)> ,trace (f f)
;; trace: (f #<procedure f (g)>)
;; trace: (f 2)
;; trace: (_ 2)
;; trace: (throw wrong-type-arg #f "Wrong type to apply: ~S" (2) (2))


;; We end up with evaluation (2 2) which can't be applied as 2 isn't a defined function

;; Exercise 1.35

;; x^2 = x + 1
;; Solving to x gives us x = (1 +- sqrt(5))/2
(fixed-point (lambda (x) (+ 1 (/ 1 x))) 1.0)

;;]=> (fixed-point (lambda (x) (+ 1 (/ 1 x))) 1.0)
;Value: 1.6180327868852458
;; Which is close enough..

;; Exercise 1.36

(define (fixed-point f first-guess)
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2))
       tolerance))
  (define (try guess)
    (let ((next (f guess)))
      (newline)
      (display guess)
      (if (close-enough? guess next)
	  next
	  (try next))))
  (try first-guess))

(fixed-point (lambda (x) (/ (log 1000) (log x))) 2.0)

;; Takes 34 guesses to reach 4.555532270803653

;; With average-damping:

(define (average x y) (/ (+ x y) 2))
(fixed-point (lambda (x) (average x (/ (log 1000) (log x)))) 2.0)

;; We get 9 iterations to reach 4.555537551999825
;; If we select different initial guess, then it may take different amount of iterations (such as 10.0 requiring 10 iterations)

;; Exercise 1.37

(define (count-fract-recursive n d k)
  (define (frac-r i)
    (if (< i k)
	(/ (n i) (+ (d i) (frac-r (+ i 1))))
	(/ (n i) (d i))))
  (frac-r 1))

;; 11 iterations is enough to get 4 decimal places

(define (cont-fract n d k)
   (define (frac-iter i sum)
       (if (= i 0)
           sum
           (frac-iter (- i 1) (/ (n i) (+ (d i) sum)))))
   (frac-iter (- k 1) (/ (n k) (d k))))

;; Exercise 1.38
;; d(i) = 2(i + 1) / 3

(define (d i)
   (if (= 0 (remainder (+ i 1) 3))
       (/ (* 2 (+ i 1)) 3)
       1))

(define (euler-number k)
   (+ 2 (cont-fract (lambda (i) 1) d k)))

(euler-number 10)
;; Value: 2721/1001


;; Exercise 1.39

(define (tan-cf x k)
  (cont-fract
   (lambda (i)
     (if (= i 1)
	 x
	 (- (square x))))
   (lambda (i) (- (* 2 i) 1))
   k))

;; Exercise 1.40

(define (cubic a b c)
  (lambda (x) (+ (* x x x) (* a (* x x)) (* b x) c)))

;; Exercise 1.41

(define (double f)
  (lambda (x) (f (f x))))

;; scheme@(guile-user)> (define (inc x) (+ x 1))
;; scheme@(guile-user)> ((double inc) 1)

;; Exercise 1.42

(define (compose f g)
  (lambda (x) (f (g x))))

;; scheme@(guile-user)> ((compose square inc) 6)
;; $3 = 49

;; Exercise 1.43

(define (repeated f n)
  (if (= n 1)
      f
      (repeated (lambda (x) (f (f x))) (- n 1))))

;; Could use compose from above instead of repeating..

;; scheme@(guile-user)> ((repeated square 2) 5)
;; $6 = 625

;; Exercise 1.44

(define dx 0.00001)

(define (smooth f)
  (lambda (x) (/ (+ (f (+ x dx)) (f x) (f (- x dx))) 3)))

(define (nfold-smooth f n)
  ((repeated smooth n) f dx))

;; Exercise 1.45

;; ...

;; Exercise 1.46
;; From old exercices..
(define (improve guess x)
  (average guess (/ x guess)))

(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))

(define (average x y)
  (/ (+ x y) 2))

(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))

;; Redo the same sqrt-iter with generic implementation

(define (iterative-improve gn ig)
  (lambda (x)
    (define (iter-guess guess)
      (if (gn guess x)
	  guess
	  (iter-guess (ig guess x))))
    (iter-guess x)))

(define (sqrt x)
  ((iterative-improve good-enough? improve) x))


;; From old fixed-point
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

;; Redo .. and something's not working (wrong number of arguments.. to what?)

(define (fixed-point f first-guess)
  ((iterative-improve
    (lambda (v1)
      (< (abs (- (f v1) v1)) tolerance))
    f) first-guess))
