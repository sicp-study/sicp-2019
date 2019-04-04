;; Exercise 2.53

;; scheme@(guile-user)> (list 'a 'b 'c)
;; (list (list 'george))
;; (cdr '((x1 x2) (y1 y2)))
;; (cadr '((x1 x2) (y1 y2)))
;; (pair? (car '(a short list)))
;; (memq 'red '((red shoes) (blue socks)))
;; (memq 'red '(red shoes blue socks))
;; $2 = (a b c)
;; $3 = ((george))
;; $4 = ((y1 y2))
;; $5 = (y1 y2)
;; $6 = #f
;; $7 = #f
;; $8 = (red shoes blue socks)

;; Exercise 2.54

(define (equal? a b)
  (cond ((eq? a b) #t)
	((and (pair? a) (pair? b)) (and (eq? (car a) (car b)) (equal? (cdr a) (cdr b))))
	(else #f)))

scheme@(guile-user)> (equal? 1 1)
$10 = #t
scheme@(guile-user)> (equal? (list 1) (list 1))
$11 = #t
scheme@(guile-user)> (equal? (list 1 2) (list 1 2))
$12 = #t
scheme@(guile-user)> (equal? (list 2) (list 1))
$13 = #f

;; Exercise 2.55

;; scheme@(guile-user) [1]> (car ''abracadabra)
;; $14 = quote

;; ' is just syntactic sugar that equals quote:
;; scheme@(guile-user)> (car (quote (quote abracadabra)))
;; $20 = quote

;; Exercise 2.56

;; Required stuff..
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))
(define (make-sum a1 a2) (list '+ a1 a2))
(define (make-product m1 m2) (list '* m1 m2))
(define (sum? x) (and (pair? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))
(define (product? x) (and (pair? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
	((=number? a2 0) a1)
	((and (number? a1) (number? a2))
	 (+ a1 a2))
	(else (list '+ a1 a2))))

(define (=number? exp num) (and (number? exp) (= exp num)))

(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
	((=number? m1 1) m2)
	((=number? m2 1) m1)
	((and (number? m1) (number? m2)) (* m1 m2))
	(else (list '* m1 m2))))

(define (deriv exp var)
  (cond ((number? exp) 0)
	((variable? exp) (if (same-variable? exp var) 1 0))
	((sum? exp) (make-sum (deriv (addend exp) var)
			      (deriv (augend exp) var)))
	((product? exp)
	 (make-sum
	  (make-product (multiplier exp)
			(deriv (multiplicand exp) var))
	  (make-product (deriv (multiplier exp) var)
			(multiplicand exp))))
	(else
	 (error "unknown expression type: DERIV" exp))))

;; Our implementation and changes

(define (exponentiation? x) (and (pair? x) (eq? (car x) '**)))
(define (base x) (cadr x))
(define (exponent x) (caddr x))
(define (make-exponentiation x y)
  (cond ((=number? y 0) 1)
	((=number? y 1) x)
	((and (number? y) (number? x))
	 (make-product x (make-exponentiation x (- y 1))))
	(else (list '** x y))))

(define (deriv exp var)
  (cond ((number? exp) 0)
	((variable? exp) (if (same-variable? exp var) 1 0))
	((sum? exp) (make-sum (deriv (addend exp) var)
			      (deriv (augend exp) var)))
	((product? exp)
	 (make-sum
	  (make-product (multiplier exp)
			(deriv (multiplicand exp) var))
	  (make-product (deriv (multiplier exp) var)
			(multiplicand exp))))
	((exponentiation? exp)
	 (make-product
	  (make-product (exponent exp)
			(make-exponentiation (base exp) (- (exponent exp) 1)))
	  (deriv (base exp) var))
	 )	 
	(else
	 (error "unknown expression type: DERIV" exp))))

;; Test
;; scheme@(guile-user) [11]> (make-exponentiation 2 3)
;; $35 = 8
;; scheme@(guile-user) [11]> (make-exponentiation 2 4)
;; $36 = 16
;; scheme@(guile-user) [11]> (make-exponentiation 'x 5)
;; $37 = (** x 5)
;; scheme@(guile-user) [11]> (make-exponentiation 3 1)
;; $38 = 3
;; scheme@(guile-user) [11]> (make-exponentiation 3 0)
;; $39 = 1


;; Testing..

  ;; (deriv '(** x 3) 'x) should result in (* 3 (** x 2))
  ;; (deriv '(* 2 '(** x 3)) 'x) should be (* (* 2 3) (** x 2))

;; scheme@(guile-user) [11]> (deriv '(** x 3) 'x)
;; $44 = (* 3 (** x 2))

;; scheme@(guile-user) [12]> (deriv '(* 2 (** x 3)) 'x)
;; $45 = (* 2 (* 3 (** x 2)))

;; It's not the simplified form, but I'm not sure if that was required..

;; Exercise 2.57

;; Apparently no need to make make-sum & make-product work, only deriv
;; make-sum won't work with these changes, that would require changes to those processes

(define (augend s)
  (if (null? (cdddr s))
      (caddr s)
      (cons '+ (cddr s))))

;; Same logic as above
(define (multiplicand p)
  (if (null? (cdddr p))
      (caddr p)
      (cons '* (cddr p))))

;; scheme@(guile-user) [7]> (deriv '(* x y (+ x 3)) 'x)
;; $26 = (+ (* x y) (* y (+ x 3)))

;; Exercise 2.58

;; a)

(define (sum? x) (and (pair? x) (eq? (cadr x) '+)))
(define (addend s) (car s))
(define (augend s) (caddr s))

;; scheme@(guile-user) [7]> (sum? '(1 + 2))
;; $27 = #t
;; scheme@(guile-user) [7]> (sum? '(+ 1 2))
;; $28 = #f
;; scheme@(guile-user) [7]> (addend '(1 + 2))
;; $29 = 1
;; scheme@(guile-user) [7]> (augend '(1 + 2))
;; $30 = 2
;; scheme@(guile-user) [7]> (deriv '(1 + x) 'x)
;; $31 = 1

(define (product? x) (and (pair? x) (eq? (cadr x) '*)))
(define (multiplier p) (car p))
(define (multiplicand p) (caddr p))

;; scheme@(guile-user) [7]> (product? '(1 * 2))
;; $32 = #t
;; scheme@(guile-user) [7]> (multiplier '(1 * 2))
;; $33 = 1
;; scheme@(guile-user) [7]> (multiplicand '(1 * 2))
;; $34 = 2

;; This allows calculations to work, but the return values are still a bit wrong:

;; scheme@(guile-user) [7]> (deriv '((x * y) * (x + 3)) 'x)
;; $35 = (+ (x * y) (* y (x + 3)))

(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
	((=number? a2 0) a1)
	((and (number? a1) (number? a2))
	 (+ a1 a2))
	(else (list a1 '+ a2))))

(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
	((=number? m1 1) m2)
	((=number? m2 1) m1)
	((and (number? m1) (number? m2)) (* m1 m2))
	(else (list m1 '* m2))))

;; scheme@(guile-user) [7]> (deriv '((x * y) * (x + 3)) 'x)
;; $36 = ((x * y) + (y * (x + 3)))

;; b)

;; Exercise 2.59

;; From SICP:

(define (element-of-set? x set)
  (cond ((null? set) false)
	((equal? x (car set)) true)
	(else (element-of-set? x (cdr set)))))

(define (adjoin-set x set)
  (if (element-of-set? x set)
      set
      (cons x set)))

;; Our implementation

(define (union-set s1 s2)
  (cond ((null? s1) s2)
	((null? s2) s1)
	(else (union-set (adjoin-set (car s2) s1) (cdr s2)))))

;; Testing

;; (union-set (list 'a 'b) (list 'c 'b))
;; $37 = (c a b)
;; scheme@(guile-user) [7]> 

;; Exercise 2.60

;; From SICP:

(define (intersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
	((element-of-set? (car set1) set2)
	 (cons (car set1) (intersection-set (cdr set1) set2)))
	(else (intersection-set (cdr set1) set2))))

;; No need to change element-of-set as the first item is still matched. The efficiency is reduced as the same element might have to be checked multiple times.

;; adjoin-set becomes faster as there's no need to check for existing element

(define (adjoin-set x set)
  (cons x set))

;; union-set and intersection-set do not change either as neither has no knowledge if the representation has duplicates or not. 

;; Exercise 2.61

;; New element-of set? implementation for ordered list

(define (element-of-set? x set)
  (cond ((null? set) false)
	((= x (car set)) true)
	((< x (car set)) false)
	(else (element-of-set? x (cdr set)))))

;; Our implementation

(define (adjoin-set x set)
  (define (adjoin-inner-set x begin end)
    (cond ((null? end) (append begin (cons x '())))
	  ((= x (car end)) (append begin end))
	  ((> x (car end)) (adjoin-inner-set x (append begin (cons (car end) '())) (cdr end)))
	  ((< x (car end)) (append begin (list x) end))))
  (adjoin-inner-set x '() set))

;; Testing

;; (adjoin-set 1 (list 2 3))
;; (adjoin-set 2 (list 1 3))
;; (adjoin-set 3 (list 1 2))

;; scheme@(guile-user) [14]> (adjoin-set 1 (list 2 3))
;; (adjoin-set 2 (list 1 3))
;; (adjoin-set 3 (list 1 2))

;; $72 = (1 2 3)
;; $73 = (1 2 3)
;; $74 = (1 2 3)

;; Exercise 2.62

(define (union-set s1 s2)
  (cond ((null? s1) s2)
	((null? s2) s1)
	(else (let ((x1 (car s1))
	      (x2 (car s2)))
	  (cond ((= x1 x2)
		 (cons x1 (union-set (cdr s1) (cdr s2))))
		((< x1 x2)
		 (cons x1 (union-set (cdr s1) s2)))
		((> x1 x2)
		 (cons x2 (union-set s1 (cdr s2)))))))))

;; Testing

;; scheme@(guile-user) [14]> (union-set (list 1 2) (list 3 4))
;; $75 = (1 2 3 4)
;; scheme@(guile-user) [14]> (union-set (list 1 2) (list 1 2))
;; $76 = (1 2)
;; scheme@(guile-user) [14]> (union-set (list 1 2) (list 2 3))
;; $77 = (1 2 3)
;; scheme@(guile-user) [14]> (union-set (list 2 3) (list 1 2))
;; $78 = (1 2 3)
;; scheme@(guile-user) [14]> (union-set (list 1 4) (list 2 3))
;; $79 = (1 2 3 4)
;; scheme@(guile-user) [14]> (union-set (list 1 3 5) (list 2 4))
;; $80 = (1 2 3 4 5)

;; Exercise 2.63

(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right)
  (list entry left right))

(define (tree->list-1 tree)
  (if (null? tree)
      '()
      (append (tree->list-1 (left-branch tree))
	      (cons (entry tree)
		    (tree->list-1
		     (right-branch tree))))))

(define (tree->list-2 tree)
  (define (copy-to-list tree result-list)
    (if (null? tree)
	result-list
	(copy-to-list (left-branch tree)
		      (cons (entry tree)
			    (copy-to-list
			     (right-branch tree)
			     result-list)))))
  (copy-to-list tree '()))

;; From figure 2.16

(define tree1 (make-tree 7
			 (make-tree 3
				    (make-tree 1 '() '())
				    (make-tree 5 '() '()))
			 (make-tree 9 '()
				    (make-tree 11 '() '()))))

(define tree2 (make-tree 3
			 (make-tree 1 '() '())
			 (make-tree 7
				    (make-tree 5 '() '())
				    (make-tree 9 '()
					       (make-tree 11 '() '())))))

;; scheme@(guile-user) [20]> (tree->list-1 tree1)
;; $84 = (1 3 5 7 9 11)
;; scheme@(guile-user) [20]> (tree->list-2 tree1)
;; $85 = (1 3 5 7 9 11)
;; scheme@(guile-user) [21]> (tree->list-2 tree2)
;; $87 = (1 3 5 7 9 11)
;; scheme@(guile-user) [21]> (tree->list-1 tree2)
;; $88 = (1 3 5 7 9 11)

;; They produce the same output for each item as they both travel the tree in nearly identical way.
;; The major difference is that one uses append and one calls itself which does cons.
;; Now, the complexity depends on the internal implementation of those functions. The actual
;; tree->list-1 and tree->list-2 are both O(n). If append is O(1) then both are O(1), if append
;; is O(N) then as described in the exercice, each append is O(n/2) for each subtree, thus the
;; growth is logaritmic -> O(N log n)

;; Exercise 2.64
(define (list->tree elements)
  (car (partial-tree elements (length elements))))
(define (partial-tree elts n)
  (if (= n 0)
      (cons '() elts)
      (let ((left-size (quotient (- n 1) 2)))
	(let ((left-result
	       (partial-tree elts left-size)))
	  (let ((left-tree (car left-result))
		(non-left-elts (cdr left-result))
		(right-size (- n (+ left-size 1))))
	    (let ((this-entry (car non-left-elts))
		  (right-result
		   (partial-tree
		    (cdr non-left-elts)
		    right-size)))
	      (let ((right-tree (car right-result))
		    (remaining-elts
		     (cdr right-result)))
		(cons (make-tree this-entry
				 left-tree
				 right-tree)
		      remaining-elts))))))))

;; scheme@(guile-user) [21]> (list->tree (list 1 3 5 7 9 11))
;; $89 = (5 (1 () (3 () ())) (9 (7 () ()) (11 () ())))

;;              5
;;             /  \
;;            1    9
;;            \   / \
;;             3 7   11

;; partial-tree calculates the center position of the given list and uses that one as the
;; top-node. Everything from the left is smaller and everything on the right is larger. Those nodes
;; are then pushed to separate partial-tree calls and the same process is done to them.

;; b) Each element (right and left part of the tree) is visited once, with partial-tree
;; being called twice inside each iteration. However as they check different nodes and no node
;; is checked more than once, we end up with O(N)


;; Exercise 2.65

;; No idea if this was the intention, but this is still O(N) growth. Multiples of N, but still N.
;; It's not however any different to the "proper way".


(define (union-set s1 s2)
  ;; From 2.62
  (define (union-set-list s1 s2)
    (cond ((null? s1) s2)
	  ((null? s2) s1)
	  (else (let ((x1 (car s1))
		      (x2 (car s2)))
		  (cond ((= x1 x2)
			 (cons x1 (union-set-list (cdr s1) (cdr s2))))
			((< x1 x2)
			 (cons x1 (union-set-list (cdr s1) s2)))
			((> x1 x2)
			 (cons x2 (union-set-list s1 (cdr s2)))))))))
  (list->tree (union-set-list (tree->list-2 s1) (tree->list-2 s2))))

;; Testing

;; scheme@(guile-user) [23]> (union-set tree1 tree2)
;; $94 = (5 (1 () (3 () ())) (9 (7 () ()) (11 () ())))

;; Same can be applied here

(define (intersection-set s1 s2)
  ;; From SICP, loan
  (define (intersection-set-inter set1 set2)
    (if (or (null? set1) (null? set2))
	'()
	(let ((x1 (car set1)) (x2 (car set2)))
	  (cond ((= x1 x2)
		 (cons x1 (intersection-set-inter (cdr set1)
						  (cdr set2))))
		((< x1 x2)
		 (intersection-set-inter (cdr set1) set2))
		((< x2 x1)
		 (intersection-set-inter set1 (cdr set2)))))))
  (list->tree (intersection-set-inter (tree->list-2 s1) (tree->list-2 s2))))

;; scheme@(guile-user) [23]> (intersection-set tree1 tree2)
;; $95 = (5 (1 () (3 () ())) (9 (7 () ()) (11 () ())))

;; Exercise 2.66

;; From SICP:

(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right)
  (list entry left right))

;; Our implementation

(define (make-item key value) (cons key value))
(define (key entry) (car entry))
(define (value entry) (cdr entry))

(define (lookup given-key tree)
  (if (null? tree)
      '()
      (let ((node (entry tree)))
	(cond ((= given-key (key node)) (value node))
	      ((< given-key (key node)) (lookup given-key (left-branch tree)))
	      ((> given-key (key node)) (lookup given-key (right-branch tree)))))))

;; Testing

;; Simple tree with quoted keys as values

(define tree3 (make-tree (make-item 7 '7)
			 (make-tree (make-item 3 '3)
				    (make-tree (make-item 1 '1) '() '())
				    (make-tree (make-item 5 '5) '() '()))
			 (make-tree (make-item 9 '9) '()
				    (make-tree (make-item 11 '11) '() '()))))

(define tree4 (make-tree (make-item 7 'g)
			 (make-tree (make-item 3 'c)
				    (make-tree (make-item 1 'a) '() '())
				    (make-tree (make-item 5 'e) '() '()))
			 (make-tree (make-item 9 'i) '()
				    (make-tree (make-item 11 'k) '() '()))))

;; scheme@(guile-user) [25]> (lookup 7 tree3)
;; $101 = 7
;; scheme@(guile-user) [25]> (lookup 5 tree3)
;; $102 = 5
;; scheme@(guile-user) [25]> (lookup 1 tree3)
;; $103 = 1
;; scheme@(guile-user) [25]> (lookup 2 tree3)
;; $104 = ()
;; scheme@(guile-user) [25]> (lookup 1 tree4)
;; $105 = a
;; scheme@(guile-user) [25]> (lookup 4 tree4)
;; $106 = ()
;; scheme@(guile-user) [25]> (lookup 7 tree4)
;; $107 = g
;; scheme@(guile-user) [25]> (lookup 9 tree4)
;; $108 = i
