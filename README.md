MSAN692 Data acquisition
=======


There are lots of exciting and interesting problems in analytics, such as figuring out what the right question is, selecting features, training a model, and interpreting results. But all of that presupposes a tidy data set that is suitable for analysis or training models. Industry experts all agree that data collection and preparation is roughly 3/4 of any analysis effort.

The title of this course is "Data Acquisition" but of course, once we get the data, we have to organize it into handy data structures and typically have to extract information from the raw data. For example, we might need to boil down a Twitter stream into a single positive or negative sentiment score for a given user.  This course teaches you how to collect, organize, coalesce, and extract information from multiple sources in preparation for your analysis work. 

This course is part of the [MS in Analytics program at the University of San Francisco](http://analytics.usfca.edu).


# Administrivia

**INSTRUCTOR.** [Terence Parr](http://parrt.cs.usfca.edu). I’m a professor in the computer science department and was founding director of the MS in Analytics program at USF.  Please call me Terence or Professor (the use of “Terry” is a capital offense).

**SPATIAL COORDINATES:**<br>

* Class is held at 101 Howard in 5th floor classroom 529.
* Exams are held on first floor, 152/154. Both sections meet together.

**TEMPORAL COORDINATES.** Wed Aug 23 - Wed Oct 11.

* Section 01: Mon/Wed 10-11:50AM
* Section 02: Mon/Wed 1:15-3:05PM 
* My office is room 608 @ 101 Howard (which I share with Prof. John Veitch).

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
|[Data pipeline](https://github.com/parrt/msan692/blob/master/hw/pipeline.md)| 5%| Fri, Sep 1 11:59pm |
|[Search Engine Implementation](https://github.com/parrt/msan692/blob/master/hw/search.md)| 12% | Wed, Sep 13 |
|[TFIDF document summarization](https://github.com/parrt/msan692/blob/master/hw/tfidf.md)| 8%| Wed, Sep 20 |
|[Recommending Articles](https://github.com/parrt/msan692/blob/master/hw/recommender.md)| 5% | Wed, Sep 27 |
|[Tweet Sentiment Analysis](https://github.com/parrt/msan692/blob/master/hw/sentiment.md)| 10% | Sun, Oct 8 11:59pm |
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

Most data you encounter will be in the form of human readable text, such as comma-separated value (CSV) files. We begin the course by studying how characters are stored in files and learning about the key data formats.

* [representing text in a computer](https://github.com/parrt/msan692/blob/master/notes/chars.ipynb); see also [7-bit ascii codes](http://www.asciitable.com/), [unicode vs ascii in python](https://docs.python.org/2/howto/unicode.html) (Day 1)
* [Data pipeline project](https://github.com/parrt/msan692/blob/master/hw/pipeline.md) (Converting stock history from Quandl to various formats) (**project**) (Day 1)
	* reading delimited data; tsv, csv
	* reading/generating XML (we'll load complicated XML in [TFIDF project](https://github.com/parrt/msan692/blob/master/hw/tfidf.md))
	* reading/generating json
* (git intro)
* [PDF using pdf2txt.py](https://github.com/parrt/msan692/blob/master/notes/pdf.ipynb) (Expecting text from Eisenhower's presidential library) (Day 2)
* [Excel and CSV data](https://github.com/parrt/msan692/blob/master/notes/excel.ipynb) (Saving as CSV, stripping non-ASCII stuff, processing CSV with Python) (Day 2)
* [HTML](https://github.com/parrt/msan692/blob/master/notes/html.md) (Parsing Tesla's IPO prospectus) (Day 3)
* [Parsing web access log files](https://github.com/parrt/msan692/blob/master/notes/logs.md) (Optional)

There are also plenty of nontext, binary formats. You can learn more from the MSAN501 boot camp material for [audio processing](https://github.com/parrt/msan501/blob/master/notes/sound.ipynb) and [image processing](https://github.com/parrt/msan501/raw/master/projects/images.pdf).

## Text feature extraction

* [Associations and dictionaries](notes/dict.ipynb) (Day 3)
* [Search Engine Implementation](https://github.com/parrt/msan692/blob/master/hw/search.md) (**project**) (Day 3)
* (code review of sample jsontable functions, more htable discussion)
* [CSV command-line kung fu](notes/bashcsv.ipynb) (Day 4)
* [Intro to information extraction from text](https://github.com/parrt/msan692/blob/master/notes/text.ipynb) (Day 5)
* [Computing TFIDF](https://github.com/parrt/msan692/blob/master/notes/tfidf.pdf) (Day 5)
* [TFIDF document summarization](https://github.com/parrt/msan692/blob/master/hw/tfidf.md) (**project**) (Day 6)

## How the web works

Now you know how to work with data files already sitting on your desk, we turn towards a study of computer networking and web infrastructure.

* [Network sockets](https://github.com/parrt/msan692/blob/master/notes/sockets.md), DNS, email (Day 6)
* [client/server architecture](https://github.com/parrt/msan692/blob/master/notes/client-server.md) (Day 6)
* [HTTP](https://github.com/parrt/msan692/blob/master/notes/http.md) (Day 7)
* [flask](https://github.com/parrt/msan692/blob/master/notes/flask.md) (Day 7)
* Review exam, launch AWS box, launch flask server at port 80 (Day 8)
* [Web analytics](https://github.com/parrt/msan692/blob/master/notes/webanalytics.md) (Day 9)
* [Cookies](https://github.com/parrt/msan692/blob/master/notes/cookies.md), logging in/out (Day 9)
* [Building web servers](https://github.com/parrt/msan692/blob/master/hw/server.md) (**optional project**)

## Data sources

With an understanding of how the Internet and web works, it's time to start pulling data from various web sources.  The difficulty of collecting data depends a great deal on the permissions and services available for a site or page.  A good analogy is: some doors are open, some doors are closed, some doors are locked, some "doors" are not doors but reinforced steel walls.

* [Pulling data from (open) REST APIs](https://github.com/parrt/msan692/blob/master/notes/openapi.md)
  * [Quandl stock data](https://www.quandl.com/api/v3/datasets/EOD/AAPL.csv).
  * openpayments.us
  * IMDB movie data
* Pull data from sites requiring an ID
  * [Zillow](https://github.com/parrt/msan692/blob/master/notes/zillow.md)
  * [Youtube](https://github.com/parrt/msan692/blob/master/notes/youtube.md)
  * [Twitter](https://github.com/parrt/msan692/blob/master/notes/twitter.md)
  * [San Francisco police activity heat map using google map API](https://github.com/parrt/msan692/blob/master/notes/heatmap.md)
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

* [San Francisco police incidents word clouds](https://github.com/parrt/msan692/blob/master/notes/sfpd.md)
