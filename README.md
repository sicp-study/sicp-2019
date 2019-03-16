# SICP Study, a collaborative classroom style learning

This project is for peer reviewing the Structure and Interpretation of Computer Programs (SICP) assigments using this workflow:

-   Watch the lecture and read the book,
-   Submit assignments before Friday, and
-   Review others assignments on Friday.

Bookmarks:

-   [iCalendar schedule](README.ics).
-   [MIT courses](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/index.htm), [videos archive](http://archive.org/download/MIT_Structure_of_Computer_Programs_1986/).
-   [The SICP book](https://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book.html), [epub version](https://github.com/sarabander/sicp-epub/blob/master/sicp.epub?raw=true).
-   [ensure-mit-scheme](https://github.com/TristanCacqueray/ensure-mit-scheme) Ansible installer.

Do not edit this document directly, instead modify the README.org file and re-export the markdown and ics file.


# Submit Assignment

To submit an assignment, first create a folder with your name in the assignments directory and add your answers in text file(s). Any file format or directory structure will do. For example:

-   assignments/my-name/solution-1.txt
-   assignments/my-name/week1/1.2.scm

Note that if the file name matches an exercise number, then an evaluation script will be used to validate the code (wip). Org-mode tangle are also supported, feel free to use the [template](assignments/template/notes.org).

Then submit a Pull request with the assignment name in the commit message.


# Review Assignment

Go to the [pull request list](https://github.com/sicp-study/sicp-2019/pulls) and pick another student assignment. Click the **Files Changed** button and check the answers. Feel free to add comment or ask for clarification by clicking the blue + sign. If the answers look correct to you, click the **Review changes** button and **Approve** the change.

When one or more other studends already approved a change, then add a **mergeit** label to close the pull request.


# 2019 Schedule

This is a weekly schedule adapted from this [meetup](https://github.com/CompSciCabal/SMRTYPRTY/wiki/Reading-Schedule!-SICP-Mark-I):


## Chapter 1


### DONE 1.1 (The Elements of Programming)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-11 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec1a.mp4)

-   For exercice 1.3, name the function square-sum-larger.
-   For exercise 1.7, name the function sqrt
-   For exercise 1.8, name the function cube-root


### DONE 1.2 (Procedures and the Processes They Generate)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-18 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec1b.mp4)

-   For exercise 1.11, name the procedure f-recursive and f-iterative
-   For exercise 1.12, name the procedure (pascal row col), with row and col starting at 1. The procedure should return -1 for invalid operands.
-   For exercise 1.16, name the procedure (fast-expt-iterative b n)
-   For exercise 1.17, name the procedure (fast-mult a b)
-   For exercise 1.18, name the procedure (fast-mult-iterative a b)


### DONE 1.3 (Formulating Abstractions with Higher-Order Procedures)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-25 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec2a.mp4)

-   For exercise 1.29, name the procedure simpson-integral
-   For exercise 1.31, name the recursive product: product-recursive, the iterative produce: product, the factorial: (factorial n), and (john-wallis-pi n) the pi approximationg using n terms (the example is n=6).
-   For exercise 1.32, name the recursive accumulate: accumulate-recursive, the iterative accumulate: accumulate.
-   For exercise 1.33, name the procedures (sum-square-prime a b) and (sum-coprime n).
-   For exercise 1.37, name the procedures count-fract-recursive and count-fract.
-   For exercise 1.38, name the D procedures (euler-sequence k) and the number (euler-number k).
-   For exercise 1.44, name the procedure (nfold-smooth f n)
-   For exercise 1.45, name the procedure (nroot n x)


## Chapter 2


### DONE 2.1.1 & 2.1.2 & 2.1.3 (Introduction to Data Abstraction)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-01 Fri&gt;</span></span></p>

[lecture-2b](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec2b.mp4)

-   For exercise 2.3, name the procedures (make-rectangle point1 point2), perimeter-rectangle and area-rectangle.


### DONE 2.1.4 (Interval Arithmetic)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-08 Fri&gt;</span></span></p>


### DONE 2.2.1 & 2.2.2 (Hierarchical Data and the Closure Property)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-15 Fri&gt;</span></span></p>

[lecture 3a (first half)](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec3a.mp4)

-   For exercise 2.29, assume a list based implementation of mobile and branch
-   For exercise 2.30, name the functions square-tree and square-tree-with-map


### DONE 2.2.3 (Sequences as Conventional Interfaces)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-22 Fri&gt;</span></span></p>

-   For exercise 2.41, name the procedure (ord-triples-sum n s)


### DONE 2.2.4 (A Picture Language)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-01 Fri&gt;</span></span></p>

[lecture 3a (second half)](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec3a.mp4)

To use the picture language, you can use DrRacket and load this [library](https://gist.github.com/etscrivner/e0105d9f608b00943a49).


### DONE 2.3.1 & 2.3.2 (Symbolic Differentiation)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-08 Fri&gt;</span></span></p>

[lecture 3b](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec3b.mp4)


### 2.3.3 (Representing Sets)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-15 Fri&gt;</span></span></p>


### 2.3.4 (Huffman Encoding)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-22 Fri&gt;</span></span></p>


### 2.4 (Data Representations)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-29 Fri&gt;</span></span></p>


### 2.5.1 & 2.5.2 (Generic Operations)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-04-05 Fri&gt;</span></span></p>


### 2.5.3 (Symbolic Algebra)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-04-12 Fri&gt;</span></span></p>


## Chapter 3


### 3.1 (Local State)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-04-19 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec5a.mp4)


### 3.2 (The Environmental Model)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-04-26 Fri&gt;</span></span></p>


### 3.3.1 & 3.3.2 (Mutable Lists and Queues)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-05-03 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec5b.mp4)


### 3.3.3 & 3.3.4 (Mutable Tables and Circuit Simulation)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-05-10 Fri&gt;</span></span></p>


### 3.3.5 (Propagation of Constraints)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-05-17 Fri&gt;</span></span></p>


### 3.4 (Concurrency)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-05-24 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec6a.mp4)


### 3.5.1 & 3.5.2 (Infinite Streams)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-05-31 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/Lec6b.mp4)


### 3.5.3 (Exploiting the Stream Paradigm)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-06-07 Fri&gt;</span></span></p>


### 3.5.4 & 3.5.5 (Streams and Delayed Evaluation)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-06-14 Fri&gt;</span></span></p>


## Chapter 4


### 4.1.1 & 4.1.2 (Metacircular Doohickeys)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-06-21 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec7a.mp4)


### 4.1.3 & 4.1.4 & 4.1.5 & 4.1.6 & 4.1.7 (Evaluators are Programs Too)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-06-28 Fri&gt;</span></span></p>


### 4.1.3 & 4.1.4 & 4.1.5 & 4.1.6 & 4.1.7 (Evaluators are Programs Too)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-07-05 Fri&gt;</span></span></p>


### 4.2.1 & 4.2.2 (Lazy Evaluators Need Motivation)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-07-12 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec7b.mp4)


### 4.2.3 (Lazy Streams Wend Cross Dales)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-07-19 Fri&gt;</span></span></p>


### 4.3.1, first half of 4.3.2 (Non-deterministic Computing Exclamation Point)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-07-26 Fri&gt;</span></span></p>


### remainder of 4.3 (Implementing Amb)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-08-02 Fri&gt;</span></span></p>


### 4.4.1 (Deductive Information Retrieval)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-08-09 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec8a.mp4)


### 4.4.2, 4.4.3

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-08-16 Fri&gt;</span></span></p>


### 4.4.2, 4.4.3

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-08-23 Fri&gt;</span></span></p>


### Week off!


### 4.4.4.1&2

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-09-06 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec8b.mp4)


### 4.4.4.3&4

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-09-13 Fri&gt;</span></span></p>


## Chapter 5


### 5.1

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-09-20 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec9a.mp4)


### 5.1.1-5.1.2

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-09-27 Fri&gt;</span></span></p>


### 5.1.3-5.1.5

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-10-04 Fri&gt;</span></span></p>


### 5.2.1

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-10-11 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec9b.mp4)


### 5.2.2

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-10-18 Fri&gt;</span></span></p>


### 5.2.3-5.2.4

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-10-25 Fri&gt;</span></span></p>


### 5.3

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-11-01 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/Lec10a.mp4)


### 5.4.1 & 5.4.2

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-11-08 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec10b.mp4)


### 5.4.3 & 5.4.4

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-11-15 Fri&gt;</span></span></p>


### 5.5.1 & 5.5.2

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-11-22 Fri&gt;</span></span></p>


### 5.5.3 & 5.5.4

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-11-29 Fri&gt;</span></span></p>


### 5.5.5 & 5.5.6

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-12-06 Fri&gt;</span></span></p>


## Ending


### SICP The Final Chapter! (SICP The End)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">SCHEDULED:</span> <span class="timestamp">&lt;2019-12-13 Fri&gt;</span></span></p>


### SICP REVIEW PARTY!!! (SICP Review Party!)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">SCHEDULED:</span> <span class="timestamp">&lt;2019-12-20 Fri&gt;</span></span></p>
