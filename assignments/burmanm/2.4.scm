;; Exercise 2.73

;; a)
;;  Instead of using hardcoded parameters for (product?), (sum?) etc, we look at the operator such as + or * and
;;  then fetch the correct function from the map. number? can't be put to the map as there's no single key that would map it.
;;  Same applies to the variable? as it isn't fixed key either. Also, as primitives they can't be parsed since they're not symbols.

;; b)

(define (make-sum-map exp var)
  (deriv (addend exp) var)
  (deriv (augend exp) var))

(put 'deriv '+ make-sum-map)

(define (make-product-map exp var)
  (get 'deriv '+
       (make-product
	(multiplier exp)
	(deriv (multiplicand exp) var))
       (make-product
	(deriv (multiplier exp) var)
	(multiplicand exp))))

(put 'deriv '* 'make-product-map)

;; c)

(put 'deriv '**
     (lambda (exp var)
       (make-product
	  (make-product (exponent exp)
			(make-exponentiation (base exp) (- (exponent exp) 1)))
	  (deriv (base exp) var))))

;; d)

;; One needs to change the order of put function's parameters

;; Exercise 2.74

;; If we treat files and records inside records both as sets, then there's no requirement to do different processing for each. We would just call the inner
;; record by first extracting the outer record

;; As long as the structure is equivalent to a map for a file and a record inside, it is enough for
;; these to work. We don't implement I/O methods here. Thus, <key><record> is enough.

;; a)

(define (get-record set user)
  (get set user))

;; b)

(define (get-salary record)
  (get record 'salary))

;; c)

(define (find-employee-record files user)
  (if (null? files)
      (error "Could not find the requested record for employee " user))
  (let ((record (get-record (car files) user)))
    (if record
	record
	(find-employee-record (cdr files) user))))

;; d)

;; The new files must adhere to previous requirements, nothing else.

;; Exercise 2.75

(define (make-from-mag-ang r a)
  (define (dispatch op)
    (cond ((eq? op 'angle) a)
	  ((eq? op 'magnitude) r)
	  ((eq? op 'real-part) (* r (cos a)))
	  ((eq? op 'imag-part) (* r (sin a)))
	  (else (error "Could not find op " op))))
  dispatch)

;; Exercise 2.76

;; The answer wanted by the book is probably:
;; Message-passing when adding new operations
;; Data-directed when adding new types

;; Personally I think both are examples of overengineering and make a mess of code. Stick to properly
;; namespaced code and there shouldn't be any issues with integration and it's less of a hassle to
;; maintain.
