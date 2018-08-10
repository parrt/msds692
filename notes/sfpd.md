# Crime data visualization in San Francisco

San Francisco has one of the most "open data" policies of any large city. In this lab, we are going to download about 400M of data (1,968,080 records) describing all police incidents since 2003 (I'm grabbing data on October 6, 2016).

## Getting started

Download all [San Francisco police department incident since 1 January 2003](https://data.sfgov.org/Public-Safety/SFPD-Incidents-from-1-January-2003/tmnf-yvry). Save in "CSV for Excel" format.

We can easily figure out how many records there are:

```bash
$ wc -l ~/data/SFPD_Incidents_from_1_January_2003.csv 
 1968081 /Users/parrt/data/SFPD_Incidents_from_1_January_2003.csv
```

So 1,968,080 not including the header row.  Let's kill that first row using `tail`:

```bash
$ tail +2 SFPD_Incidents_from_1_January_2003.csv > SFPD.csv
```

In Python, that would be equivalent to `data[1:]` (it counts from 0 not 1 like `tail`). You can name that data file whatever you want but I will call it `SFPD.csv` for these exercises.

## Sniffing the data

To get an idea of what the data looks like, let's do a simple histogram of the categories and crime descriptions.  Here is the category histogram:

```bash
$ python histo.py ~/data/SFPD.csv
406342 LARCENY/THEFT
279619 OTHER OFFENSES
210564 NON-CRIMINAL
172414 ASSAULT
117467 VEHICLE THEFT
113708 DRUG/NARCOTIC
100802 VANDALISM
 93082 WARRANTS
 81932 BURGLARY
 70707 SUSPICIOUS OCC
 57810 MISSING PERSON
 50477 ROBBERY
 37409 FRAUD
 22549 SECONDARY CODES
 22157 FORGERY/COUNTERFEITING
 19415 WEAPON LAWS
 16750 TRESPASS
 15932 PROSTITUTION
 10586 STOLEN PROPERTY
 10065 SEX OFFENSES, FORCIBLE
  9331 DISORDERLY CONDUCT
  9281 DRUNKENNESS
  7779 RECOVERED VEHICLE
  5147 DRIVING UNDER THE INFLUENCE
  4989 KIDNAPPING
  4062 RUNAWAY
  3956 LIQUOR LAWS
  3430 ARSON
  2688 EMBEZZLEMENT
  2377 LOITERING
  1164 SUICIDE
  1114 FAMILY OFFENSES
   880 BAD CHECKS
   707 BRIBERY
   643 EXTORTION
   365 SEX OFFENSES, NON FORCIBLE
   319 GAMBLING
    49 PORNOGRAPHY/OBSCENE MAT
    12 TREA
```

and here is the start of the crime description histogram:
 
```bash
143903 GRAND THEFT FROM LOCKED AUTO
 70123 LOST PROPERTY
 60593 BATTERY
 59892 STOLEN AUTOMOBILE
 59412 DRIVERS LICENSE, SUSPENDED OR REVOKED
 52218 WARRANT ARREST
 49375 AIDED CASE, MENTAL DISTURBED
 47935 SUSPICIOUS OCCURRENCE
 45227 PETTY THEFT FROM LOCKED AUTO
 39820 MALICIOUS MISCHIEF, VANDALISM OF VEHICLES
 38117 PETTY THEFT OF PROPERTY
 36992 MALICIOUS MISCHIEF, VANDALISM
 35278 TRAFFIC VIOLATION
 31879 THREATS AGAINST LIFE
 28655 FOUND PROPERTY
 25815 ENROUTE TO OUTSIDE JURISDICTION
 25254 GRAND THEFT OF PROPERTY
 22830 PETTY THEFT FROM A BUILDING
 21511 PETTY THEFT SHOPLIFTING
 21340 POSSESSION OF NARCOTICS PARAPHERNALIA
 21336 FOUND PERSON
 20757 GRAND THEFT FROM A BUILDING
 20068 CREDIT CARD, THEFT BY USE OF
...
```

**Exercise**: Create a helper function in `csvcols.py` that opens a CSV file in Excel format given a `filename` and returns the indicated column number:

```python
import csv
from collections import Counter

def get_column(filename,col):
    """
    Load CSV in Excel format, return Counter created from column of data indicated by
    integer col parameter.
    """
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, dialect='excel')
        ...
    data = Counter(data)
    return data
```

Then in `histo.py`, we can use it to get a particular column:

```python
categories = get_column(sys.argv[1],col=1)
```

Print out the histograms as shown above for categories and descriptions to finish off the exercise.

## Word clouds

A more interesting way to visualize differences in term frequency is using a so-called word cloud.  For example, here is a word cloud showing the categories from 2003 to the present.

<img src=figures/SFPD-wordcloud.png width=400>

Python has a nice library you can use:

```bash
$ pip install wordcloud
```

**Exercise**: In a file called `catcloud.py`, once again get the categories and then create a word cloud object and display it:

```python
from wordcloud import WordCloud
from csvcols import get_column
import matplotlib.pyplot as plt
import sys

...
wordcloud = WordCloud(width=1800,
                      height=1400,
                      max_words=10000,
                      random_state=1,
                      relative_scaling=0.25)

... get tuples with (word,count) from categories Counter ...                      
wordcloud.fit_words(wordtuples)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
```

### Which neighborhood is the "worst"?

**Exercise**: Now, pullout the police district and do a word cloud on that in `hoodcloud.py` (it's ok to cut/paste):

<img src=figures/SFPD-hood-wordcloud.png width=400>

### Crimes per neighborhood


**Exercise**: Filter the CSV file using `grep` from the commandline to get just the rows from a particular precinct, such as MISSION:

```bash
$ grep MISSION ~/data/SFPD.csv > /tmp/mission.csv
$ grep RICHMOND ~/data/SFPD.csv > /tmp/richmond.csv
```

Run the `wordcloud.py` script on those files to get an idea of the types of crimes per those two neighborhoods. Here is the mission and richmond districts crime category clouds.

<img src=figures/SFPD-mission-wordcloud.png width=300> <img src=figures/SFPD-richmond-wordcloud.png width=300>

### Which neighborhood has most car break-ins?

**Exercise**: Filter the SFPD.csv for `GRAND THEFT FROM LOCKED AUTO` and then run `hoodcloud.py` on the resulting csv.

<img src=figures/SFPD-car-breakin-hood-wordcloud.png width=300>

Hmm..ok, so parking in the Mission is ok, but Northern, Central, and Southern precincts are bad news.

If you get stuck in any of these exercises, you can look at the [code associated with this notes](https://github.com/parrt/msds692/tree/master/notes/code/sfpd).
