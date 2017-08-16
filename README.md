MSAN692 Data acquisition
=======


There are lots of exciting and interesting problems in analytics, such as figuring out what the right question is, selecting features, training a model, and interpreting results. But all of that presupposes a tidy data set that is suitable for analysis or training models. Industry experts all agree that data collection and cleaning is roughly 3/4 of any analysis effort.  This course teaches how to collect, coalesce, and clean data from multiple sources in preparation for your analysis work. 

This course is part of the [MS in Analytics program at the University of San Francisco](http://analytics.usfca.edu).


# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Analytics program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES.** 101 Howard. Both sections Rm 527 on the fifth floor.

**TEMPORAL COORDINATES.** Wed Aug 23 - Wed Oct 11.

 * Section 01: Mon/Wed 10-11:50AM
 * Section 02: Mon/Wed 1:15-3:05PM 

**INSTRUCTION FORMAT**. Class runs for 1:50 hours, 2 days/week. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python 2 programming language, unless otherwise specified.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**ACADEMIC HONESTY.** You must abide by the copyright laws of the United States and academic honesty policies of USF. You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation.

The golden rule: **You must never represent another person’s work as your own.**

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

**Note:** Leaving your laptop unattended is a common means for another student to take your work. It is your responsibility to guard your work. Do not leave your printouts laying around or in the trash. *All persons with common code are likely to be considered at fault.*

**ON DISABILITIES.** If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact USF Student Disability Services (SDS) at 415/422-2613 within the first week of class, or immediately upon onset of the disability, to speak with a disability specialist. If you are determined eligible for reasonable accommodations, please meet with your disability specialist so they can arrange to have your accommodation letter sent to me, and we will discuss your needs for this course. For more information, please visit http://www.usfca.edu/sds/ or call 415/422-2613.

## Student evaluation

| Artifact | Grade Weight | Due date |
|--------|--------|--------|
|[Data pipeline](https://github.com/parrt/msan692/blob/master/hw/pipeline.md)| 5%| Mon, Sep 4 before class |
|[Search Engine Implementation](https://github.com/parrt/msan692/blob/master/hw/search.md)| 10% | Wed, Sep 13 |
|[Recommending Articles](https://github.com/parrt/msan692/blob/master/hw/recommender.md)| 7% | Wed, Sep 20 |
|[TFIDF document summarization](https://github.com/parrt/msan692/blob/master/hw/tfidf.md)| 8%| Wed, Sep 27 |
|[Tweet Sentiment Analysis](https://github.com/parrt/msan692/blob/master/hw/sentiment.md)| 10% | Wed, Oct 9 |
|Midterm Exam| 30%| 10AM-12PM Fri, Sep 15 |
|Final Exam| 30%| 10AM-12PM Fri, Oct 13 |

<!--
|[Group project](https://github.com/parrt/msan692/blob/master/hw/group.md)| 15%| Wed, Oct 12 midnight |
-->

All projects will be graded with the specific input or tests given in the project description, so you understand precisely what is expected of your program. Consequently, projects will be graded in binary fashion: They either work or they do not.  My hope is that everyone will get 100% on the projects.

Each project has a hard deadline and only those projects working correctly before the deadline get credit.  My grading script pulls from github at the deadline.

**Grading standards**. I consider an **A** grade to be above and beyond what most students have achieved. A **B** grade is an average grade for a student or what you could call "competence" in a business setting. A **C** grade means that you either did not or could not put forth the effort to achieve competence. Below **C** implies you did very little work or had great difficulty with the class compared to other students.

# Syllabus

## Data formats

* [representing text in a computer](https://github.com/parrt/msan692/blob/master/notes/chars.md); see also [7-bit ascii codes](http://www.asciitable.com/), [unicode vs ascii in python](https://docs.python.org/2/howto/unicode.html)
* [Data pipeline project](https://github.com/parrt/msan692/blob/master/hw/pipeline.md) (Converting stock history from Yahoo finance to various formats) (**project**)
	* reading delimited data; tsv, csv
	*  reading/generating XML (we'll load complicated XML in [TFIDF project](https://github.com/parrt/msan692/blob/master/hw/tfidf.md))
	* reading/generating json
* [PDF using pdf2txt.py](https://github.com/parrt/msan692/blob/master/notes/pdf.md) (Parsing documents from Eisenhower's presidential library)
* [Excel](https://github.com/parrt/msan692/blob/master/notes/excel.md) (Saving as CSV, stripping non-ASCII stuff, loading into Python)
* [HTML](https://github.com/parrt/msan692/blob/master/notes/html.md) (Parsing Tesla's IPO prospectus)
* [Parsing web access log files](https://github.com/parrt/msan692/blob/master/notes/logs.md)

## How the web works

* [Network sockets](https://github.com/parrt/msan692/blob/master/notes/sockets.md), DNS, email
* [client/server architecture](https://github.com/parrt/msan692/blob/master/notes/client-server.md)
* [HTTP](https://github.com/parrt/msan692/blob/master/notes/http.md)
* [flask](https://github.com/parrt/msan692/blob/master/notes/flask.md)
* [Web analytics](https://github.com/parrt/msan692/blob/master/notes/webanalytics.md)
* [Cookies](https://github.com/parrt/msan692/blob/master/notes/cookies.md), logging in/out
* [Building web servers](https://github.com/parrt/msan692/blob/master/hw/server.md) (**project**)

## Text feature extraction

* [Intro to information extraction from text](https://github.com/parrt/msan692/blob/master/notes/text.ipynb)
* [San Francisco police incidents word clouds and heat maps](https://github.com/parrt/msan692/blob/master/notes/sfpd.md)
* [Computing TFIDF](https://github.com/parrt/msan692/blob/master/notes/tfidf.pdf)
* [TFIDF document summarization](https://github.com/parrt/msan692/blob/master/hw/tfidf.md) (**project**)

## Data sources

* [Pulling data from (open) REST APIs](https://github.com/parrt/msan692/blob/master/notes/openapi.md)
  * yahoo
  * openpayments.us
  * IMDB movie data
* Pull data from sites requiring an ID
  * [Zillow](https://github.com/parrt/msan692/blob/master/notes/zillow.md)
  * [Youtube](https://github.com/parrt/msan692/blob/master/notes/youtube.md)
  * [Twitter](https://github.com/parrt/msan692/blob/master/notes/twitter.md)
* [APIs requiring authentication/identification](https://github.com/parrt/msan692/blob/master/notes/authapi.md) (optional)
  * [LinkedIn](https://github.com/parrt/msan692/blob/master/notes/linkedin.md)
  * [Facebook](https://github.com/parrt/msan692/blob/master/notes/facebook.md)
* [Extracting data from web pages](https://github.com/parrt/msan692/blob/master/notes/scraping.md)
  * [Crawling](https://github.com/parrt/msan692/blob/master/notes/crawling.md)
  * [buzzfeed](https://github.com/parrt/msan692/blob/master/notes/buzzfeed.md)
  * [Amazon](https://github.com/parrt/msan692/blob/master/notes/amazon.md)
  * [Scraping data from tables](https://github.com/parrt/msan692/blob/master/notes/scraping-tables.md)
* [Selenium](https://github.com/parrt/msan692/blob/master/notes/selenium.md)


## Misc

* Running shell commands from Python
* regex
* Unix commands for extracting web content: wget, grep, awk, cut, paste, join, sed
* k-means for compression, color selection