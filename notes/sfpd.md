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

In Python, that would be equivalent to `data[2:]`. You can name that data file whatever you want but I will call it `SFPD.csv` for these exercises.

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

def get_columns(filename,col):
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
categories = get_columns(sys.argv[1],col=1)
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
from csvcols import get_columns
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

## Heatmaps

Clouds are pretty cool for showing the relative size of various terms but sometimes it's more interesting to look at crimes per fine-grained area. For this, we can use Google's map API.  As far as I can tell, the easiest way to do a heat map on a real live map is using Google's map API but via a small JavaScript program in a webpage. 

## Dropping a marker on a Google map

Take a look at [Google maps API doc](https://developers.google.com/maps/documentation/javascript/) and an [example showing a google map](https://developers.google.com/maps/documentation/javascript/examples/marker-simple). From this example, we can drop a marker a location in San Francisco:

<img src=figures/first-crime-in-2003.png width=350>

**Exercise**: Using the template below, fill in the `...` latitude and longitude for any place that you'd like to see. And also change `YOUR_API_KEY` to your Google API key.  For example, we can grab a location from the police data. Column 10 (from 0) is the latitude and column 9 is the longitude: 37.7981336020854, -122.427270640646. Save the file as `map.html` and then open it with your browser.

In your [Google api console](https://console.developers.google.com), you will have to make sure that the Google maps javascript API **is enabled**.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <meta name="viewport" content="initial-scale=1.0">
    <meta charset="utf-8">
    <style>
      html, body {
        height: 100%;
        margin: 0;
        padding: 0;
      }
      #map {
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script>
      var map;
      function initMap() {
        var myLatLng = {lat: ..., lng: ...};
        map = new google.maps.Map(document.getElementById('map'), {
          center: myLatLng,
          zoom: 14
        });
        var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: 'First crime in 2003!'
        });
      }
    </script>
    <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&callback=initMap"
    async defer></script>
  </body>
</html>
```

Don't worry too much about the JavaScript, we are simply going to use it as a framework for dumping in coordinates for heat map.

## Crime heat map

We are going to base our crime heat map on the [Heatmap example](https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap). Because we don't know JavaScript, we are going to use Python to process the CSV file and generate the minimum necessary JavaScript to get this working. For each crime, we will emit aligned such as:

```javascript
{lat:37.7765080370233, lng:-122.414457764634},
```

I have split Google's heat map example into two files with a small modification so that we can combine [`heatmap-start.txt`](https://github.com/parrt/msan692/blob/master/notes/code/sfpd/heatmap-start.txt) + those longitude and latitude lines + [`heatmap-end.txt`](https://github.com/parrt/msan692/blob/master/notes/code/sfpd/heatmap-end.txt) into a `heatmap.html` file and then view it in the browser.

**Exercise**: Write a small Python program called `latlng.py` that processes the file specified as an argument and prints out column 10, column 9 but in the format above.

```bash
$ python latlng.py ~/data/SFPD.csv
{lat:37.7981336020854, lng:-122.427270640646},
{lat:37.7981336020854, lng:-122.427270640646},
{lat:37.7981336020854, lng:-122.427270640646},
{lat:37.7725273607571, lng:-122.406970988225},
{lat:37.7724682400061, lng:-122.389517648036},
{lat:37.7226585129212, lng:-122.412469643631},
{lat:37.7292705199592, lng:-122.432325871028},
{lat:37.7292705199592, lng:-122.432325871028},
{lat:37.7292705199592, lng:-122.432325871028},
{lat:37.7745145380854, lng:-122.452839772389},
...
```

**Exercise**: Modify the `heatmap-end.txt` file to use your API key. Combine the start and end files with the output from `latlng.py` into `heatmap.html`. Then view that file in a browser. The easy way to do that is the following:

```bash
cat heatmap-start.txt > heatmap.html
python latlng.py ~/data/SFPD.csv >> heatmap.html 
cat heatmap-end.txt >> heatmap.html 
open heatmap.html # if on Mac OS X
```

You should see something like the following map:

<img src=figures/car-breakin-heatmap.png width=400>

Unfortunately, over such a long period, just about every location in the city has been hit; repeatedly. We need to filter the data for a smaller time range or sample the data at some interval. The easiest thing to do is simply to ask where the car break-ins have been for 2016. 

**Exercise**: Filter the original CSV to get all crimes for 2016 using `grep`. and then rerun the above procedure with `latlng.py` to get a new heat map called `2016-heatmap.html`. The regular expression you need for `grep` to find all dates from 2016 is `../../2016`. Pass that through another `grep` that filters for `GRAND THEFT FROM LOCKED AUTO` and write it to file `2016-car-break-ins.csv`.  Follow the process you did above to create the `heatmap.html` file with `latlng.py`, but now process data `2016-car-break-ins.csv`. I played around with the radius and maximum intensity parameters of the heat map and got a fairly useful image:

```javascript
heatmap.set('maxIntensity', 40);
heatmap.set('radius', 9.5);
```

My heat map looks like the following for 2016 car break-ins in SF:

<img src=figures/2016-car-breakins-heatmap.png width=400>

As we would expect, there is a lot of car break-ins at the de Young Museum garage and 5th/mission garage, but bizarrely there are lots of car break-ins at the Hall of Justice in SOMA! Weird. Wait, I also see the concentration at another police precinct station. Maybe they simply enter their own GPS location when someone calls into report a break-in.

<hr>

If you get stuck in any of these exercises, you can look at the [code associated with this notes](https://github.com/parrt/msan692/tree/master/notes/code/sfpd).