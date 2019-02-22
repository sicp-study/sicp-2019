;; Exercise 2.1

(define (make-rat numer denumer)
  (cond ((or (and (< denumer 0) (> numer 0)) (and (< denumer 0) (< numer 0))) (cons (* -1 numer) (* -1 denumer)))
	(else (cons numer denumer))))

;; Exercise 2.2

(define (make-segment p1 p2)
  (cons p1 p2))

(define (start-segment segment)
  (car segment))

(define (end-segment segment)
  (cdr segment))

(define (make-point x y)
  (cons x y))

(define (x-point p)
  (car p))

(define (y-point p)
  (cdr p))

(define (midpoint-segment segment)
  (make-point
   (/ (+ (x-point (start-segment segment)) (x-point (end-segment segment))) 2)
   (/ (+ (y-point (start-segment segment)) (y-point (end-segment segment))) 2)))

(define (print-point p)
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

;; Test:

(print-point
 (midpoint-segment (make-segment (make-point 0 0) (make-point 4 4))))

;; (2,2)

;; Exercise 2.3

;; Use segments above, two opposite segments
(define (make-rectangle seg1 seg2)
  (cons seg1 seg2))

(define (calc-lengths rec)
  (cons
   (- (x-point (start-segment (car rec))) (x-point (start-segment (cdr rec))))
   (- (y-point (start-segment (car rec))) (y-point (end-segment (car rec))))))

(define (perimeter-rectangle rec)
  (let* ((lengths (calc-lengths rec))
	 (x (car lengths))
	 (y (cdr lengths))
	 (calc-rectangle
	  (* 2 (+ x y))))
  (if (< calc-rectangle 0)
      (* -1 calc-rectangle)
      calc-rectangle)))

;; Test
(perimeter-rectangle
 (make-rectangle (make-segment (make-point 0 0) (make-point 0 4)) (make-segment (make-point 10 0) (make-point 10 4))))

;; $21 = 28

(define (area-rectangle rec)
  (let* ((lengths (calc-lengths rec))
	 (x (car lengths))
	 (y (cdr lengths))
	 (calc-area (* x y)))
    calc-area))

;; Test
(area-rectangle
 (make-rectangle (make-segment (make-point 0 0) (make-point 0 4)) (make-segment (make-point 10 0) (make-point 10 4))))

;; $23 = 40

;; Exercise 2.4

(define (cdr z)
  (z (lambda (p q) q)))

;; (define (cons x y)
;;   (lambda (m) (m x y)))
;; (define (car z)
;;   (z (lambda (p q) p)))
;; (car (cons x y))
;;
;; (car ((lambda (m) (m x y) x y)))
;; ((z (lambda (p q) p)) ((lambda (m) (m x y) x y)))
;; ((lambda (m) (m x y) x y) (lambda (p q) p))
;; m is substituted with the (lambda (p q) p) which returns first argument of (x y)

;; Exercise 2.5

;; Math question again.. meh. 

;; Exercise 2.6

;; (define zero (lambda (f) (lambda (x) x)))
;; (define (add-1 n)
;;   (lambda (f) (lambda (x) (f ((n f) x)))))


;; (add-1 zero)

(define one (lambda (f) (lambda (x) (f ((lambda (x) x) x)))))

;; call the last one, outer lambda with x returns x..
(define one (lambda (f) (lambda (x) (f x))))

;; (add-1 one) same idea
(define two (lambda (f) (lambda (x) (f (f x)))))

;; +

;; Is basically calling add-1 n-times. That is, (f ((n f) x)) * n-times. Since n is used, use m:

(define + (x y) (lambda (f) (lambda (x) ((m f) ((n f) x)))))

;; Exercise 2.7

(define (upper-bound interval) (car interval))
(define (lower-bound interval) (cdr interval))

;; Exercise 2.8

(define (sub-interval x y)
  (make-interval (- (lower-bound x) (lower-bound y))
		 (- (upper-bound x) (upper-bound y))))

;; Exercise 2.9

;; More math..

;; w = (x - y)/2
;; [x,y] ; [z,v]
;; wC = ((x + z) - (y + v))/2
;; w2 = (z - v)/2

;; Prove that those are equal.. that is:

;; w + w2 = wC

;; Easier to read from paper, but it transforms to:

;; ((z-v) + (x-y)) / 2 = ((x+z) - (y+v))/2
;; * 2 on each side, open parentheses:

;; z-v+x-y = x+z-y-v
;; Reorder and see that 0 = 0

;; Exercise 2.10

(define (div-interval x y)
  (if (and
       (<= 0 (lower-bound y))
       (>= 0 (upper-bound y)))
      (error "Intervals spans zero")

      (mul-interval
       x
       (make-interval (/ 1.0 (upper-bound y))
		      (/ 1.0 (lower-bound y))))))

;; Exercise 2.11

;; Insanely complex code, which is bad.

;; Exercise 2.12

;; center and width from SICP

(define (make-center-percent center tolerance)
  (make-center-width center
		     (* center (/ 100.0 tolerance))))

(define (percent interval)
  (* 100.0 (/ (width interval) (center interval))))

;; Exercise 2.13

;; The floating point approximations are the source of issues, as 1/(1/R1 + 1/R2) does require significantly more digits to retain the same amount of accuracy as R1R2/(R1+R2).

;; Exercise 2.14

;; scheme@(guile-user) [5]> (par1 (make-center-percent 1000 2) (make-center-percent 2000 1))
;; $4 = (-41708.5020242915 . 40882.59109311741)
;; scheme@(guile-user) [5]> (par2 (make-center-percent 1000 2) (make-center-percent 2000 1))
;; $5 = (-39279.35222672065 . 40719.3675889328)
;; scheme@(guile-user) [5]>

;; Exercise 2.15

;; To understand why, one has to look at the implementation of div-interval. Since dividing by itself does not return itself, we pretty quickly end up in a situation where the returns are not exact. And with such inexactness, the calculations start to differ very easily - even if mathematically they should be identical.

;; Exercise 2.16

;; Beyond simple exercise.
