;; Procedures and the Processes They Generate (1.2)

;; Exercise 1.9
;; First one is recursive as we need to keep the stack since we're unable to calculate the
;; value without knowing the subprocesses return value.
;;
;; (+ 4 5)
;;   (inc (+ 3 5))
;;     (inc (inc (+ 2 5)))
;;       (inc (inc (inc (+ 1 5))))
;;         (inc (inc (inc (inc (+ 0 5)))))
;;           (inc (inc (inc (inc  5))))
;;         (inc (inc (inc 6)))
;;       (inc (inc 7))
;;     (inc 8)
;;   9
;;
;; Second process is iterative, the state can be maintained by only 'a' and 'b', without the need
;; to know any previous recursive call states.
;;
;; The latter example with (+ 4 5) generates the calls:
;; (+ 4 5)
;; (+ 3 6)
;; (+ 2 7)
;; (+ 1 8)
;; (+ 0 9)
;; b -> (9)

;; Exercise 1.10

;; 1024
;; 65536
;; 65536
;;
;; Omitted mathematical stuff
;;
;; Exercise 1.11
;;
;;
(define (f-recursive n)
  (if (< n 3)
      n
      (+ (f (- n 1)) (* 2 (f (- n 2))) (* 3 (f (- n 3))))))

(define (f-iterative n)
  (define (iter count psum ppsum pppsum)
    (if (> count n)
	psum
	(iter (+ count 1) (+ psum (* 2 ppsum) (* 3 pppsum)) psum ppsum)))
  (iter 3 2 1 0))

;; Exercise 1.12
;;
;; Calculates single position only, not the whole line / tree / etc
(define (pascal n i)
  (cond ((or (< i 1) (> i n)) -1)
	((= i 1) 1)
	((= i n) 1)
	(else (+ (pascal (- n 1) (- i 1)) (pascal (- n 1) i)))))

;;
;; Exercise 1.13
;;
;; Skipping this one, it's just mathematical induction.
;;

;; Exercise 1.14
;; No time, it increases with some exponential function.
;;
;; Exercise 1.15
;;
;; 5 times and it's O(log n) as we can see the sine value approaching with ~sqrt(n) changes.

;; Exercise 1.16
(define (fast-expt-iterative b n)
  (define (calc-iter a x z)
    (cond ((= z 0) a)
	  ((even? z) (calc-iter a (square x) (/ z 2)))
	  (else (calc-iter (* a x) x (- z 1)))))
  (calc-iter 1 b n))

;; Exercise 1.17
(define (double a) (+ a a))
(define (halve a) (/ a 2))
(define (fast-mult a b)
  (cond ((= b 1) a)
	((even? b) (double (fast-mult a (halve b))))
	(else (+ a (fast-mult a (- b 1))))))

;; Exercise 1.18
;; From previous:
;;(define (double a) (+ a a))
;;(define (halve a) (/ a 2))

(define (fast-mult-iterative a b)
  (define (mult-iter z x y)
    (cond ((= z 0) y)
	  ((even? z) (mult-iter (halve z) (double x) y))
	  (else (mult-iter (- z 1) x (+ x y)))))
  (mult-iter a b 0))

;; Exercise 1.20
;; 4 for applicative, 18 for normal (normal expands gcd first and that causes the
;; extra (remainder) expansions later)

;; Exercise 1.21
;; 199, 1999 and 7

;; Exercise 1.22

(define (smallest-divisor n) (find-divisor n 2))
(define (divides? a b) (= (remainder b a) 0))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
	((divides? test-divisor n) test-divisor)
	(else (find-divisor n (+ test-divisor 1)))))

(define (prime? n)
  (= n (smallest-divisor n)))

;; We'll need to modify the original timed-prime-test slightly, a #f to the if clause
(define (timed-prime-test n)
  (newline)
  (display n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (if (prime? n)
      (report-prime (- (runtime) start-time))
      #f))
(define (report-prime elapsed-time)
  (display " *** ")
  (display elapsed-time)
  #t)

(define (find-next-three x)
  (define (find-iter n i)
    (if (= i 3)
	i
	(if (timed-prime-test n)
	    (find-iter (+ n 2) (+ i 1))
	    (find-iter (+ n 2) i))))
  (find-iter (- (+ x 1) (remainder x 2)) 0))

;; The timings do not work well in modern machines..

;1 ]=> (find-next-three 10000)

;10001
;10003
;10005
;10007 *** 0.
;10009 *** 0.
;10011
;10013
;10015
;10017
;10019
;10021
;10023
;10025
;10027
;10029
;; 10031
;; 10033
;; 10035
;; 10037 *** 9.999999999999787e-3
;Value: 3

;; 1 ]=> (find-next-three 100000)

;; 100001
;; 100003 *** 0.
;; 100005
;; 100007
;; 100009
;; 100011
;; 100013
;; 100015
;; 100017
;; 100019 *** 0.
;; 100021
;; 100023
;; 100025
;; 100027
;; 100029
;; 100031
;; 100033
;; 100035
;; 100037
;; 100039
;; 100041
;; 100043 *** 0.
;; ;Value: 3

;; 1 ]=> (find-next-three 1000000)

;1000001
;1000003 *** 9.999999999999787e-3
;1000005
;1000007
;1000009
;1000011
;1000013
;1000015
;1000017
;1000019
;1000021
;1000023
;1000025
;1000027
;1000029
;1000031
;1000033 *** 0.
;1000035
;1000037 *** 1.0000000000001563e-2
;Value: 3


;; Since times were too fast, using values 1e9, 1e10 and 1e11 were used instead. Those lead us to
;; around 0.07, 0.21 and 0.66 on my machine. Which is around ~3 times and thus close to sqrt(10).

;; Exercise 1.23

(define (next n)
  (if (= n 2)
      3
      (+ n 2)))

(define (smallest-divisor n) (find-divisor n 2))
(define (divides? a b) (= (remainder b a) 0))
(define (find-divisor n test-divisor)
  (cond ((> (square test-divisor) n) n)
	((divides? test-divisor n) test-divisor)
	(else (find-divisor n (next test-divisor)))))

;; With changes:
(find-next-three 1e11)

;; 100000000001.
;; 100000000003. *** .39000000000000057
;; 100000000005.
;; 100000000007.
;; 100000000009.
;; 100000000011.
;; 100000000013.
;; 100000000015.
;; 100000000017.
;; 100000000019. *** .370000000000001
;; 100000000021.
;; 100000000023.
;; 100000000025.
;; 100000000027.
;; 100000000029.
;; 100000000031.
;; 100000000033.
;; 100000000035.
;; 100000000037.
;; 100000000039.
;; 100000000041.
;; 100000000043.
;; 100000000045.
;; 100000000047.
;; 100000000049.
;; 100000000051.
;; 100000000053.
;; 100000000055.
;; 100000000057. *** .35999999999999943
;; ;Value: 3

;; That is, time is around half the previous.

;; Exercise 1.24
(define (square x)
   (* x x))

(define (even? n)
   (= (remainder n 2) 0))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
	((even? exp)
	 (remainder
	  (square (expmod base (/ exp 2) m))
	  m))
	(else
	 (remainder
	  (* base (expmod base (- exp 1) m))
	  m))))

(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))
(define (fast-prime? n times)
  (cond ((= times 0) true)
	((fermat-test n) (fast-prime? n (- times 1)))
	(else false)))

;; Use our modified version of timed-prime-test to reduce printing to only primes

(define (timed-prime-test n)
  (start-prime-test n (runtime)))
(define (start-prime-test n start-time)
  (if (fast-prime? n 100)
      (report-prime (- (runtime) start-time) n)
      #f))
(define (report-prime elapsed-time n)
  (newline)
  (display n)
  (display " *** ")
  (display elapsed-time)
  #t)

;; Use (find-next-three (round->exact n)) to get it working with large numbers..

;; The time to calculate fermat numbers does not seem to increase at all and is less than the precision of
;; the runtime. Replacing runtime with real-time-clock (mit-scheme) gives us a better indication:

(define (timed-prime-test n)
  (start-prime-test n (real-time-clock)))
(define (start-prime-test n start-time)
  (if (fast-prime? n 100)
      (report-prime (- (real-time-clock) start-time) n)
      #f))


;; 10 error> (find-next-three (round->exact 1e40))

;; 10000000000000000303786028427003666890753 *** 53
;; 10000000000000000303786028427003666891041 *** 30
;; 10000000000000000303786028427003666891101 *** 32
;; ;Value: 3

;; 10 error> (find-next-three (round->exact 1e300))

;; 1000000000000000052504760255204420248704468581108159154915854115511802457988908195786371375080447864043704443832883878176942523235360430575644792184786706982848387200926575803737830233794788090059368953234970799945081119038967640880074652742780142494579258788820056842838115669472196386865459400540381 *** 502
;; 1000000000000000052504760255204420248704468581108159154915854115511802457988908195786371375080447864043704443832883878176942523235360430575644792184786706982848387200926575803737830233794788090059368953234970799945081119038967640880074652742780142494579258788820056842838115669472196386865459400542127 *** 510
;; 1000000000000000052504760255204420248704468581108159154915854115511802457988908195786371375080447864043704443832883878176942523235360430575644792184786706982848387200926575803737830233794788090059368953234970799945081119038967640880074652742780142494579258788820056842838115669472196386865459400543303 *** 496
;; ;Value: 3

;; 10 error> (find-next-three (round->exact 1e150))

;; 999999999999999980835596172437374590573120014030318793091164810154100112203678582976298268616221151962702060266176005440567032331208403948233373515999 *** 151
;; 999999999999999980835596172437374590573120014030318793091164810154100112203678582976298268616221151962702060266176005440567032331208403948233373516469 *** 151
;; 999999999999999980835596172437374590573120014030318793091164810154100112203678582976298268616221151962702060266176005440567032331208403948233373517033 *** 150
;; ;Value: 3

;; Exercise 1.25

;; Explained in the footnote 46, fast-exp would be a lot slower since we would have to calculate large numbers
;; which is not necessary with the modulo operations.

;; Exercise 1.26

;; This transforms the expmod to be a tree recursion, which is a lot slower.

;; Exercise 1.27

(define (test-carmichael n)
  (define (fermat-test n a)
    (= (expmod a n n) a))
  (define (iter-cm n a)
    (if (= a n)
	#t
	(if (fermat-test n a)
	    (iter-cm n (+ a 1))
	    #f)))
  (iter-cm n 2))

(test-carmichael 561)

;Value: #t

(test-carmichael 1105)

;Value: #t

(test-carmichael 1729)

;Value: #t

(test-carmichael 2465)

;Value: #t

(test-carmichael 2821)

;Value: #t

(test-carmichael 6601)

;Value: #t

;; Exercise 1.28
