;; From SICP:

(define (make-leaf symbol weight) (list 'leaf symbol weight))
(define (leaf? object) (eq? (car object) 'leaf))
(define (symbol-leaf x) (cadr x))
(define (weight-leaf x) (caddr x))
(define (make-code-tree left right)
  (list left
	right
	(append (symbols left) (symbols right))
	(+ (weight left) (weight right))))
(define (left-branch
	 tree) (car
		tree))
(define (right-branch tree) (cadr tree))
(define (symbols tree)
  (if (leaf? tree)
      (list (symbol-leaf tree))
      (caddr tree)))
(define (weight tree)
  (if (leaf? tree)
      (weight-leaf tree)
      (cadddr tree)))

(define (decode bits tree)
  (define (decode-1 bits current-branch)
    (if (null? bits)
	'()
	(let ((next-branch
	       (choose-branch (car bits) current-branch)))
	  (if (leaf? next-branch)
	      (cons (symbol-leaf next-branch)
		    (decode-1 (cdr bits) tree))
	      (decode-1 (cdr bits) next-branch)))))
  (decode-1 bits tree))

(define (choose-branch bit branch)
  (cond ((= bit 0) (left-branch branch))
	((= bit 1) (right-branch branch))
	(else (error "bad bit: CHOOSE-BRANCH" bit))))

(define (adjoin-set x set)
  (cond ((null? set) (list x))
	((< (weight x) (weight (car set))) (cons x set))
	(else (cons (car set)
		    (adjoin-set x (cdr set))))))

(define (make-leaf-set pairs)
  (if (null? pairs)
      '()
      (let ((pair (car pairs)))
	(adjoin-set (make-leaf (car pair)
			       (cadr pair))
					; symbol
					; frequency
		    (make-leaf-set (cdr pairs))))))

(define (append list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (append (cdr list1) list2))))

;; Exercise 2.67


(define sample-tree
  (make-code-tree (make-leaf 'A 4)
		  (make-code-tree
		   (make-leaf 'B 2)
		   (make-code-tree
		    (make-leaf 'D 1)
		    (make-leaf 'C 1)))))
(define sample-message '(0 1 1 0 0 1 0 1 0 1 1 1 0))

;; scheme@(guile-user)> (decode sample-message sample-tree)
;; $2 = (A D A B B C A)

;; Exercise 2.68

;; From SICP
(define (encode message tree)
  (if (null? message)
      '()
      (append (encode-symbol (car message) tree)
	      (encode (cdr message) tree))))

;;
(define (encode-symbol symbol tree)
  (define (encode-symbol-inner symbol tree bits)
    (cond ((leaf? tree)
	   (if (eq? (symbol-leaf tree) symbol)
	       bits
	       (error "No symbol found from the tree: " symbol)))
	  ((eq? (symbol-leaf (left-branch tree)) symbol) (append bits '(0)))
	  (else (encode-symbol-inner symbol (right-branch tree) (append bits '(1))))))
  (encode-symbol-inner symbol tree '()))

;; Testing

;; scheme@(guile-user)> (encode-symbol 'A sample-tree)
;; (encode-symbol 'B sample-tree)
;; (encode-symbol 'D sample-tree)
;; (encode-symbol 'C sample-tree)

;; $23 = (0)
;; $24 = (1 0)
;; $25 = (1 1 0)
;; $26 = (1 1 1)

;; scheme@(guile-user)> (equal? sample-message (encode (decode sample-message sample-tree) sample-tree))
;; $37 = #t

;; Exercise 2.69

(define (generate-huffman-tree pairs)
  (successive-merge (make-leaf-set pairs)))

(define (successive-merge leaf-set)
  (if (null? (cdr leaf-set))
      (car leaf-set)
      (successive-merge
       (adjoin-set
	(make-code-tree (car leaf-set) (cadr leaf-set)) (cddr leaf-set)))))

;; {(A 8) (B 3) (C 1) (D 1) (E 1) (F 1) (G 1) (H 1)}

;; Testing, use previous exercise
;; (generate-huffman-tree '((A 4) (B 2) (C 1) (D 1)))
;; $4 = ((leaf A 4) ((leaf B 2) ((leaf D 1) (leaf C 1) (D C) 2) (B D C) 4) (A B D C) 8)

;; Exercise 2.70

(define tree (generate-huffman-tree '((A 2) (NA 16) (BOOM 1) (SHA 3) (GET 2) (YIP 9) (JOB 2) (WAH 1))))

;; Technically we can't encode the following song by storing all the information as our tree doesn't match:

(define song '(Get a job
Sha na na na na na na na na
Get a job
Sha na na na na na na na na
Wah yip yip yip yip yip yip yip yip yip
Sha boom))

;; ERROR: In procedure scm-error:
;; symbol not found:  Get

;; So we need to encode actually the upper-case version of the song for the given tree:

(define song '(GET A JOB 
SHA NA NA NA NA NA NA NA NA 
GET A JOB SHA NA NA NA NA NA NA NA NA 
WAH YIP YIP YIP YIP YIP YIP YIP YIP YIP 
SHA BOOM))

;; scheme@(guile-user) [3]> (encode song tree)
;; $7 = (1 1 1 1 1 1 1 0 0 1 1 1 1 0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 0 0 1 1 1 1 0 1 1 1 0 0 0 0 0 0 0 0 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 0 1 1 0 1 1)
;; scheme@(guile-user) [3]> (length (encode song tree))
;; $8 = 84


;; Fixed length, we need n-symbols:

;; scheme@(guile-user) [3]> (length '((A 2) (NA 16) (BOOM 1) (SHA 3) (GET 2) (YIP 9) (JOB 2) (WAH 1)))
;; $11 = 8

;; 2^3 = 8, so we need 3 bits for each item.
;; (* (length song) 3)
;; $13 = 108

;; Exercise 2.71

;; Incoming bad ASCII art..

;;   /\
;; 16  \
;;     /\
;;    8  \
;;       /\
;;      4  \
;;         /\
;;        2  1


;;  Not going to draw the n=10, in any case.. 16 = 0, 8 = 10, 4 = 110, 2 = 1110, 1 = 1111 ; thus max 4 bits
;;  And that leads to the: n-1 bits for least used symbol and 1 bit for the most used symbol

;; Exercise 2.72

;; Considering the case of 1,2,4,8,..,n^2-1 symbol occurence. For these symbols, we see a pattern of:
;; 16*1 + 8*2 + 4*3 + 2*4 + 1*4 accesses to get all the symbol occurences.

;; Thus, the most accessed is actually O(1) but we search it n-times, thus O(N). For the least used, we need to search
;; the tree (this unbalanced one) for O(m-1) with m being the amount of codewords. Thus we end up with O(m*n). 
