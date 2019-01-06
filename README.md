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

Note that if the file name matches an exercise number, then an evaluation script will be used to validate the code (wip). Org-mode tangle are also supported, feel free to use the [template](assignments/template/notes.md).

Then submit a Pull request with the assignment name in the commit message.


# Review Assignment

Go to the [pull request list](https://github.com/sicp-study/sicp-2019/pulls) and pick another student assignment. Click the **Files Changed** button and check the answers. Feel free to add comment or ask for clarification by clicking the blue + sign. If the answers look correct to you, click the **Review changes** button and **Approve** the change.

When one or more other studends already approved a change, then add a **mergeit** label to close the pull request.


# 2019 Schedule

This is a weekly schedule adapted from this [meetup](https://github.com/CompSciCabal/SMRTYPRTY/wiki/Reading-Schedule!-SICP-Mark-I):


## Chapter 1


### 1.1 (The Elements of Programming)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-11 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec1a.mp4)

-   For exercice 1.3, name the function square-sum-larger.
-   For exercise 1.7, name the function sqrt
-   For exercise 1.8, name the function cube-root


### 1.2 (Procedures and the Processes Who Love Them)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-18 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec1b.mp4)


### 1.3 (Formulating Abstractions)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-01-25 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec2a.mp4)


## Chapter 2


### 1.3.4 & 2.1.1 & 2.1.2 & 2.1.3 (Data Abstraction)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-01 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec2b.mp4)


### 2.1.4 (Interval Arithmetic)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-08 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec3a.mp4)


### 2.2.1 & 2.2.2 (Hierarchical Structures)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-15 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec3b.mp4)


### 2.2.3 (Sequences as Conventional Interfaces)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-02-22 Fri&gt;</span></span></p>


### 2.2.4 (A Picture Language)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-01 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec4a.mp4)


### 2.3.1 & 2.3.2 (Symbolic Differentiation)

<p><span class="timestamp-wrapper"><span class="timestamp-kwd">DEADLINE:</span> <span class="timestamp">&lt;2019-03-08 Fri&gt;</span></span></p>

[lecture](https://archive.org/download/MIT_Structure_of_Computer_Programs_1986/lec4b.mp4)


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
