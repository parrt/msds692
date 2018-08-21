MSDS692 Data acquisition
=======


There are lots of exciting and interesting problems in analytics, such as figuring out what the right question is, selecting features, training a model, and interpreting results. But all of that presupposes a tidy data set that is suitable for analysis or training models. Industry experts all agree that data collection and preparation is roughly 3/4 of any analysis effort.

The title of this course is "Data Acquisition" but of course, once we get the data, we have to organize it into handy data structures and typically have to extract information from the raw data. For example, we might need to boil down a Twitter stream into a single positive or negative sentiment score for a given user.  This course teaches you how to collect, organize, coalesce, and extract information from multiple sources in preparation for your analysis work. Along the way, you'll learn about networks, the internet protocols, and your own building web servers.

This course is part of the [MS in Data Science program at the University of San Francisco](https://www.usfca.edu/arts-sciences/graduate-programs/data-science).


# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science and data science departments and was founding director of the MS in Analytics program at USF (which became the MS data science program).  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES:**<br>

* Class is held at 101 Howard in 5th floor classroom 527.
* Exams are held in 527 and 529. Both sections meet together.
* My office is room 607 @ 101 Howard up on mezzanine

**TEMPORAL COORDINATES.** Wed Aug 22 - Wed Oct 10.

* Section 01: Mon/Wed 10-11:50AM
* Section 02: Mon/Wed 1:15-3:05PM 
* Exams: Wednesdays, 9:15 - 9:55AM and (last exam) 3:15-4:15PM

**INSTRUCTION FORMAT**. Class runs for 1:50 hours, 2 days/week. Instructor-student interaction during lecture is encouraged and we'll mix in mini-exercises / labs during class. All programming will be done in the Python 3 programming language, unless otherwise specified.

**TARDINESS.** Please be on time for class. It is a big distraction if you come in late.

**ACADEMIC HONESTY.** You must abide by the copyright laws of the United States and academic honesty policies of USF. You may not copy code from other current or previous students. All suspicious activity will be investigated and, if warranted, passed to the Dean of Sciences for action.  Copying answers or code from other students or sources during a quiz, exam, or for a project is a violation of the university’s honor code and will be treated as such. Plagiarism consists of copying material from any source and passing off that material as your own original work. Plagiarism is plagiarism: it does not matter if the source being copied is on the Internet, from a book or textbook, or from quizzes or problem sets written up by other students. Giving code or showing code to another student is also considered a violation.

The golden rule: **You must never represent another person’s work as your own.**

If you ever have questions about what constitutes plagiarism, cheating, or academic dishonesty in my course, please feel free to ask me.

**Note:** Leaving your laptop unattended is a common means for another student to take your work. It is your responsibility to guard your work. Do not leave your printouts laying around or in the trash. *All persons with common code are likely to be considered at fault.*

**USF policies and legal declarations**

*Students with Disabilities*

If you are a student with a disability or disabling condition, or if you think you may have a disability, please contact <a href="/sds">USF Student Disability Services</a> (SDS) for information about accommodations.

*Behavioral Expectations*

All students are expected to behave in accordance with the <a href="/fogcutter">Student Conduct Code</a> and other University policies.

*Academic Integrity*

USF upholds the standards of honesty and integrity from all members of the academic community. All students are expected to know and adhere to the University's <a href="/academic-integrity/">Honor Code</a>.

*Counseling and Psychological Services (CAPS)*

CAPS provides confidential, free <a href="/student-health-safety/caps">counseling</a> to student members of our community.

*Confidentiality, Mandatory Reporting, and Sexual Assault*

For information and resources regarding sexual misconduct or assault visit the <a href="/TITLE-IX">Title IX</a> coordinator or USFs <a href="http://usfca.callistocampus.org" target="_blank">Callisto website</a>.

## Student evaluation

| Artifact | Grade Weight | Due date |
|--------|--------|--------|
|[Data pipeline](https://github.com/parrt/msds692/blob/master/hw/pipeline.md)| 4%| Fri, Aug 31 11:59pm |
|[Search Engine Implementation](https://github.com/parrt/msds692/blob/master/hw/search.md)| 10% | Mon, Sep 10 |
|[TFIDF document summarization](https://github.com/parrt/msds692/blob/master/hw/tfidf.md)| 6%| Mon, Sep 17 |
|[Recommending Articles](https://github.com/parrt/msds692/blob/master/hw/recommender.md)| 5% | Mon, Sep 24 |
|[Tweet Sentiment Analysis](https://github.com/parrt/msds692/blob/master/hw/sentiment.md)| 10% | Mon, Oct 8 |
|Exam 1| 15%| 9AM-9:55AM Wed, Sep 5 |
|Exam 2| 22%| 9AM-9:55AM Wed, Sep 19 |
|Exam 3| 28%| 3-4PM Wed, Oct 10 |

<!--
|[Group project](https://github.com/parrt/msds692/blob/master/hw/group.md)| 15%| Wed, Oct 12 midnight |
-->

All projects will be graded with the specific input or tests given in the project description, so you understand precisely what is expected of your program. Consequently, projects will be graded in binary fashion: They either work or they do not.  My hope is that everyone will get 100% on the projects.

Each project has a hard deadline and only those projects working correctly before the deadline get credit.  My grading script pulls from github at the deadline.  *All projects are due at the start of class on the day indicated, unless otherwise specified.*

**Grading standards**. I consider an **A** grade to be above and beyond what most students have achieved. A **B** grade is an average grade for a student or what you could call "competence" in a business setting. A **C** grade means that you either did not or could not put forth the effort to achieve competence. Below **C** implies you did very little work or had great difficulty with the class compared to other students.

# Syllabus

## Data formats

Most data you encounter will be in the form of human readable text, such as comma-separated value (CSV) files. We begin the course by studying how characters are stored in files and learning about the key data formats.

* [Representing text in a computer](notes/chars.ipynb); see also [7-bit ascii codes](http://www.asciitable.com/), [unicode vs ascii in python](https://docs.python.org/3/howto/unicode.html) (Day 1)
* [Data pipeline project](https://github.com/parrt/msds692/blob/master/hw/pipeline.md) (Converting stock history from Quandl to various formats) (**project**) (Day 1)
	* reading delimited data; tsv, csv
	* reading/generating XML (we'll load complicated XML in [TFIDF project](https://github.com/parrt/msds692/blob/master/hw/tfidf.md))
	* reading/generating json
* (git intro; clone, add, commit, push, pull; see [Using git revision control](https://github.com/parrt/msds501/blob/master/notes/git.md) from Boot camp)
* [PDF using pdftotext](notes/pdf.ipynb) (Extracting text from Tesla's marketing brochure) (Day 2)
* [Excel and CSV data](notes/excel.ipynb) (Day 2)
* [HTML](notes/html.ipynb) (Parsing Tesla's IPO prospectus) (Day 3)

There are also plenty of nontext, binary formats. You can learn more from the msds501 boot camp material for [audio processing](https://github.com/parrt/msds501/blob/master/notes/sound.ipynb) and [image processing](https://github.com/parrt/msds501/raw/master/projects/images.pdf).

## Organizing data in memory into structures

* [Debugging with PyCharm](notes/debugger.md) (Day ?)
* [Associations and dictionaries](notes/dict.ipynb) (Day 3)
* [Data structure basics](notes/datastructures.ipynb) (Day 4)

## Text feature extraction

* [Search Engine Implementation](https://github.com/parrt/msds692/blob/master/hw/search.md) (**project**) (Day 3)
* (code review of sample jsontable functions, more htable discussion)
* [CSV command-line kung fu](notes/bashcsv.ipynb) (Day 4)
* [Intro to information extraction from text](notes/text.ipynb) (Day 5)
* [Computing TFIDF](notes/tfidf.pdf) (Day 5)
* [TFIDF document summarization](https://github.com/parrt/msds692/blob/master/hw/tfidf.md) (**project**) (Day 6)

## How the web works

Now you know how to work with data files already sitting on your desk, we turn towards a study of computer networking and web infrastructure.

* [Network sockets](notes/sockets.md), DNS, email (Day 6)
* [client/server architecture](notes/client-server.md) (Day 6)
* [HTTP](notes/http.md) (Day 7)
* [flask](notes/flask.md) (Day 7)
* Review exam, launch AWS box, launch flask server at port 80 (Day 8)
* [Web analytics](notes/webanalytics.md) (Day 9)
* [Cookies](notes/cookies.md), logging in/out (Day 9)
* [Building web servers](https://github.com/parrt/msds692/blob/master/hw/server.md) (**optional project**)

## Data sources

With an understanding of how the Internet and web works, it's time to start pulling data from various web sources.  The difficulty of collecting data depends a great deal on the permissions and services available for a site or page.  A good analogy is: some doors are open, some doors are closed, some doors are locked, some "doors" are not doors but reinforced steel walls.

* [Pulling data from (open) REST APIs](notes/openapi.md) (Day 10, skip IMDB; new key mech fails)
  * Quandl stock data (*todo*: move to next section)
  * openpayments.us
  * IMDB movie data (*todo*: damn, now this one uses an API key also and mine is currently not working that are received by email)
* Pull data from sites requiring an ID
  * [Zillow](notes/zillow.md) (Optional)
  * [Twitter](notes/twitter.md)  (jump ahead here to sync with project Day 10, more detail Day 11)
  * [Youtube](notes/youtube.md)  (Day 11)
* [APIs requiring authentication/identification](notes/authapi.md) (optional)
  * [LinkedIn](notes/linkedin.md)
  * [Facebook](notes/facebook.md)
* [Extracting data from web pages](notes/scraping.md) (Day 12)
  * [Crawling](notes/crawling.md)
  * [buzzfeed](notes/buzzfeed.md) (Day 12)
  * [Amazon](notes/amazon.md)
  * [Scraping data from tables](notes/scraping-tables.md)
* [Selenium](notes/selenium.md)

## Misc

* [San Francisco police activity heat map using google map API](notes/heatmap.md)
* [San Francisco police incidents word clouds](notes/sfpd.md)
