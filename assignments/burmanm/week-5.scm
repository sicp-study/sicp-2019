;; Exercise 2.17

(define (last-pair list)
  (if (null? (cdr list))
      list
      (last-pair (cdr list))))


;; scheme@(guile-user) [6]> (last-pair (list 23 72 149 34))
;; $14 = (34)

;; Exercise 2.18

(define (reverse list)
  (if (null? list)
      '()
      (append (reverse (cdr list)) (cons (car list) '()))))

;; Exercise 2.19

(define (except-first-denomination coin-values)
  (cdr coin-values))

(define (first-denomination coin-values)
  (car coin-values))

(define (no-more? coin-values)
  (null? coin-values))

(define (cc amount coin-values)
  (cond ((= amount 0) 1)
	((or (< amount 0) (no-more? coin-values)) 0)
	(else
	 (+ (cc amount
		(except-first-denomination
		 coin-values))
	    (cc (- amount
		   (first-denomination
		    coin-values))
		coin-values)))))

;; (define us-coins (list 50 25 10 5 1))
;; (define uk-coins (list 100 50 20 10 5 2 1 0.5))

;; scheme@(guile-user) [6]> (cc 100 us-coins)
;; $27 = 292
;; scheme@(guile-user) [6]> (cc 100 uk-coins)
;; $28 = 104561
;; scheme@(guile-user) [6]> 

;; It does make a difference, since larger amount of coins creates larger recursion tree and more potential answers.

;; Exercise 2.20

(define (same-parity x . y)
  (define (not-even? z) (not (even? z)))
  (define (print-list comp l1 l2)
    (if (null? l2)
	l1
	(if (comp (car l2))
	    (print-list comp (cons l1 (car l2)) (cdr l2))
	    (print-list comp l1 (cdr l2)))))
  (if (even? x)
      (print-list even? (list x) y)
      (print-list not-even? (list x) y)))

;; Exercise 2.21

;; For guile, not needed with mit scheme
(define (square x) (* x x))

;; nil is not known by mit-scheme or guile..
(define nil '())

(define (square-list items)
  (if (null? items)
      nil
      (cons
       (square (car items)) (square-list (cdr items)))))

(define (square-list items)
  (map square items))

;; For both:
;; scheme@(guile-user) [7]> (square-list '(1 2 3 4))
;; $43 = (1 4 9 16)

;; Exercise 2.22

;; cons in the iter is adding the current item as the first one and then appends the
;; answer as the remaining part. That's why it's in wrong order

;; Newer version does not work either, since the syntax of cons now creates pairs with
;; first item being the new pair (thus, it's a "heap")

;; Exercise 2.23

(define (for-each f items)
  (define (fei f left forget)
    (if (null? left)
	'() ;; return value is undefined and we don't care about forget
	(fei f (cdr left) (f (car left)))))
  (fei f items '()))

;; Test:
(for-each (lambda (x) (newline) (display x)) (list 57 321 88))

;; 1 ]=> (for-each (lambda (x) (newline) (display x)) (list 57 321 88))

;; 57
;; 321
;; 88
;; ;Value: ()

;; Exercise 2.24

;; scheme@(guile-user)> (list 1 (list 2 (list 3 4)))
;; $4 = (1 (2 (3 4)))

;; "draw" :

;; (1) -> (2) -> (3 4)

;; Exercise 2.25

;; (1 3 (5 7) 9) = (cdr (car (cdr (cdr

;; scheme@(guile-user) [7]> (cdr (car (cdr (cdr (list 1 3 (cons 5 7) 9)))))
;; $14 = 7

;; ((7)) = (car (car))

;; scheme@(guile-user) [8]> (car (car '((7))))
;; $19 = 7

;; (1 (2 (3 (4 (5 (6 7))))))

;; scheme@(guile-user) [13]> (car (cdr (car (cdr (car (cdr (car (cdr (car (cdr (car (cdr (list 1 (list 2 (list 3 (list 4 (list 5 (list 6 7))))))))))))))))))
;; $34 = 7

;; Exercise 2.26

;; scheme@(guile-user) [13]> (append x y)
;; $35 = (1 2 3 4 5 6)
;; scheme@(guile-user) [13]> (cons x y)
;; $36 = ((1 2 3) 4 5 6)
;; scheme@(guile-user) [13]> (list x y)
;; $37 = ((1 2 3) (4 5 6))

;; Exercise 2.27

(define (deep-reverse list)
  (if (null? list)
      '()
      (append (deep-reverse (cdr list)) (cons (reverse (car list)) '()))))

;; scheme@(guile-user) [15]> (deep-reverse x)
;; $44 = ((4 3) (2 1))

;; Exercise 2.28

(define (fringe t)
  (cond ((null? t) '())
	((not (pair? t)) (list t))
	(else (append (fringe (car t))
		      (fringe (cdr t))))))

;; scheme@(guile-user) [25]> (fringe x)
;; $60 = (1 2 3 4)
;; scheme@(guile-user) [25]> (fringe (list x x))
;; $61 = (1 2 3 4 1 2 3 4)
;; scheme@(guile-user) [25]> 

;; Exercise 2.29

;; a)

(define (make-mobile left right)
  (list left right))

(define (make-branch length structure)
  (list length structure))

(define (left-branch mobile)
  (car mobile))

(define (right-branch mobile)
  (car (cdr mobile)))

(define (branch-length mobile)
  (car mobile))

(define (branch-structure mobile)
  (car (cdr mobile)))

;; b)

(define (total-weight mobile)
  (define (count-branch b)
    (if (not (pair? (branch-structure b)))
	(branch-structure b)
	(total-weight (branch-structure b))))
  (+ (count-branch (left-branch mobile)) (count-branch (right-branch mobile))))

;; Test..

(define m1 (make-mobile (make-branch 1 1) (make-branch 1 2)))

;; scheme@(guile-user) [33]> (total-weight m1)
;; $78 = 3

(define m2 (make-mobile (make-branch 1 1) (make-branch 1 (make-mobile (make-branch 1 2) (make-branch 1 1)))))

;; (total-weight m2)
;; $79 = 4

;; c)

;; Export count-branch

(define (balanced? mobile)
  (define (count-branch b)
    (if (not (pair? (branch-structure b)))
	(branch-structure b)
	(total-weight (branch-structure b))))
  (define (total-weight mobile)
    (+ (count-branch (left-branch mobile)) (count-branch (right-branch mobile))))
  (define (count-torque b)
    (* (branch-length b) (count-branch b)))
  (define (branch-balanced? b)
    (if (pair? (branch-structure b))
	(balanced? (branch-structure b))
	#t))
  (and (= (count-torque (left-branch mobile)) (count-torque (right-branch mobile)))
       (branch-balanced? (left-branch mobile))
       (branch-balanced? (right-branch mobile))))

      
;; Test..

(define m3 (make-mobile (make-branch 1 4) (make-branch 2 (make-mobile (make-branch 1 1) (make-branch 1 1)))))
(define m4 (make-mobile (make-branch 1 1) (make-branch 1 1)))

;; scheme@(guile-user) [36]> (balanced? m1)
;; $84 = #f
;; scheme@(guile-user) [36]> (balanced? m2)
;; $85 = #f
;; scheme@(guile-user) [36]> (balanced? m3)
;; $86 = #t
;; scheme@(guile-user) [36]> (balanced? m4)
;; $87 = #t
;; scheme@(guile-user) [36]> 

;; d)

;; Change to:

(define (right-branch mobile)
  (cdr mobile))

(define (branch-structure mobile)
  (cdr mobile))

;; Exercise 2.30

(define (square x) (* x x))

(define (square-tree tree)
  (cond ((null? tree) '())
	((not (pair? tree)) (square tree))
	(else (cons (square-tree (car tree))
		    (square-tree (cdr tree))))))

;; Test

(square-tree
 (list 1
       (list 2 (list 3 4) 5)
       (list 6 7)))

;; scheme@(guile-user) [36]> (square-tree
;;  (list 1
;;        (list 2 (list 3 4) 5)
;;        (list 6 7)))

;; $88 = (1 (4 (9 16) 25) (36 49))

(define (square-tree-map tree)
  (map (lambda (sub-tree)
	 (if (pair? sub-tree)
	     (square-tree-map sub-tree)
	     (square sub-tree)))
       tree))

;; Test returns the same as previous

;; Exercise 2.31

(define (square-tree tree) (tree-map square tree))

(define (tree-map f tree)
  (map (lambda (sub-tree)
	 (if (pair? sub-tree)
	     (tree-map f sub-tree)
	     (f sub-tree)))
       tree)) 

;; Exercise 2.32

;; This one was tricky to understand.. needed a bit of Googling..

(define (subsets s)
  (if (null? s)
      (list nil)
      (let ((rest (subsets (cdr s))))
	(append rest (map
		      (lambda (x)
			(cons (car s) x))
		      rest)))))

;; Test..

(subsets '(1 2 3))
;; $94 = (() (3) (2) (2 3) (1) (1 3) (1 2) (1 2 3))

;; Exercise 2.33

;; From SICP
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
	  (accumulate op initial (cdr sequence)))))

(define (map p sequence)
  (accumulate (lambda (x y)
		(cons (p x) y)) nil sequence))

(define (append seq1 seq2)
  (accumulate cons seq2 seq1))

(define (length sequence)
  (accumulate
   (lambda (x y) (+ y 1)) 0 sequence))

;; Test

;; scheme@(guile-user) [37]> (map square (list 1 2 3 4 5 6))
;; $101 = (1 4 9 16 25 36)

;; scheme@(guile-user) [37]> (append (list 1 2 3) (list 4 5 6))
;; $96 = (1 2 3 4 5 6)

;; scheme@(guile-user) [37]> (length (list 1 2 3 4 5 6 7 8 9))
;; $98 = 9

;; Exercise 2.34

;; result = result*x + poly[i]

(define (horner-eval x coefficient-sequence)
  (accumulate (lambda (this-coeff higher-terms)
		(+ (* higher-terms x) this-coeff))
	      0
	      coefficient-sequence))

;; Test

(horner-eval 2 (list 1 3 0 5 0 1))

;; scheme@(guile-user) [37]> (horner-eval 2 (list 1 3 0 5 0 1))
;; $109 = 79


;; Exercise 2.35

;; From 2.2.2.. 
;; (define (count-leaves x)
;;   (cond ((null? x) 0)
;; 	((not (pair? x)) 1)
;; 	(else (+ (count-leaves (car x))
;; 		 (count-leaves (cdr x))))))

(define (count-leaves t)
  (accumulate + 0
	      (map (lambda (item)
		     (if (pair? item)
			 (count-leaves item)
			 1))
		   t)))

;; Test
(define x (cons (list 1 2) (list 3 4)))
(count-leaves x)
(count-leaves (list x x))

;; scheme@(guile-user) [38]> (count-leaves x)
;; $111 = 4
;; scheme@(guile-user) [38]> (count-leaves (list x x))
;; $112 = 8

;; Exercise 2.36

(define (accumulate-n op init seqs)
  (if (null? (car seqs))
      nil
      (cons (accumulate op init (map (lambda (x) (car x)) seqs))
	    (accumulate-n op init (map (lambda (x) (cdr x)) seqs)))))

;; Test

(define s (list (list 1 2 3) (list 4 5 6) (list 7 8 9) (list 10 11 12)))
(accumulate-n + 0 s)

;; scheme@(guile-user) [50]> (accumulate-n + 0 s)
;; $120 = (22 26 30)

;; Exercise 2.37

;; From SICP
(define (dot-product v w)
  (accumulate + 0 (map * v w)))

(define (matrix-*-vector m v)
  (map (lambda (x) (dot-product x v)) m))

(define (transpose mat)
  (accumulate-n
   cons '() mat))

(define (matrix-*-matrix m n)
  (let ((cols (transpose n)))
    (map
     (lambda (x) (matrix-*-vector cols x))       
     m)))

;; Exercise 2.38

(define (fold-left op initial sequence)
  (define (iter result rest)
    (if (null? rest)
	result
	(iter (op result (car rest))
	      (cdr rest))))
  (iter initial sequence))

(define fold-right accumulate)

(fold-right / 1 (list 1 2 3))
(fold-left / 1 (list 1 2 3))
(fold-right list nil (list 1 2 3))
(fold-left list nil (list 1 2 3))

;; $121 = 3/2
;; $122 = 1/6
;; $123 = (1 (2 (3 ())))
;; $124 = (((() 1) 2) 3)

;; Any property were the order of the operands makes no difference to execution (obviously). For example, * or + (but not - for example)

;; Exercise 2.39

;; (define (reverse list)
;;   (if (null? list)
;;       '()
;;       (append (reverse (cdr list)) (cons (car list) '()))))

(define (reverse sequence)
  (fold-right (lambda (x y)
		(append y (cons x '()))) nil sequence))

(define (reverse sequence)
  (fold-left (lambda (x y)
		(append (cons y '()) x)) nil sequence))

;; Test, both return the same..

;; scheme@(guile-user) [55]> (reverse (list 1 2 3))
;; $130 = (3 2 1)

;; Exercise 2.40

;; 1 <= i < j <= n

(define (enumerate-interval low high)
  (if (> low high)
      nil
      (cons low (enumerate-interval (+ low 1) high))))

(define (flatmap proc seq)
  (accumulate append nil (map proc seq)))

(define (unique-pairs n)
  (flatmap (lambda (i)
	     (map (lambda (j) (list i j))
		  (enumerate-interval 1 (- i 1))))
  (enumerate-interval 1 n)))

;; Test

;; scheme@(guile-user) [59]> (unique-pairs 5)
;; $137 = ((2 1) (3 1) (3 2) (4 1) (4 2) (4 3) (5 1) (5 2) (5 3) (5 4))

;; Simplify prime-sum-pairs..

(define (make-pair-sum pair)
  (list (car pair) (cadr pair) (+ (car pair) (cadr pair))))

(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter prime-sum? (flatmap
			   (lambda (i)
			     (map (lambda (j) (list i j))
				  (enumerate-interval 1 (- i 1))))
			   (enumerate-interval 1 n)))))

(define (prime-sum? pair)
  (prime? (+ (car pair) (cadr pair))))

;; Test

;; Original:

;; scheme@(guile-user) [58]> (prime-sum-pairs 5)
;; $134 = ((2 1 3) (3 2 5) (4 1 5) (4 3 7) (5 2 7))

(define (prime-sum-pairs n)
  (map make-pair-sum
       (filter prime-sum? (unique-pairs n))))

;; Modified:

;; scheme@(guile-user) [59]> (prime-sum-pairs 5)
;; $136 = ((2 1 3) (3 2 5) (4 1 5) (4 3 7) (5 2 7))


;; Exercise 2.41

(define (make-triplet-sum triplet)
  (+ (car triplet) (cadr triplet) (caddr triplet)))

(define (create-triple-permutations n)
  (flatmap (lambda (i)
	     (map (lambda (j) (cons i j)) (unique-pairs n)))
	   (enumerate-interval 1 n)))

(define (make-triple-sum-pair triple)
  (list triple (make-triplet-sum triple)))

(define (ordered-triples n s)
  (map (lambda (x) (car x))
  (filter (lambda (x) (= s (cadr x)))
	  (map make-triple-sum-pair (create-triple-permutations n)))))

;; Test

;; scheme@(guile-user) [60]> (ordered-triples 3 5)
;; $149 = ((1 3 1) (2 2 1))

;; Exercise 2.42

(define (adjoin new-row k rest-of-queens))

(define (safe? k positions))

(define (empty-board '()))

;; From SICP
(define (queens board-size)
  (define (queen-cols k)
    (if (= k 0)
	(list empty-board)
	(filter
	 (lambda (positions) (safe? k positions))
	 (flatmap
	  (lambda (rest-of-queens)
	    (map (lambda (new-row)
		   (adjoin-position
		    new-row k rest-of-queens))
		 (enumerate-interval 1 board-size)))
	  (queen-cols (- k 1))))))
  (queen-cols board-size))

