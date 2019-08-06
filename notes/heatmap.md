# San Francisco police activity heat map using google map API

*It looks like you have to pay to use the Google maps API now, at least through Python*

Clouds are pretty cool for showing the relative size of various terms but sometimes it's more interesting to look at crimes per fine-grained area. For this, we can use Google's map API.  As far as I can tell, the easiest way to do a heat map on a real live map is using Google's map API but via a small JavaScript program in a webpage. 

## Dropping a marker on a Google map

Take a look at [Google maps API doc](https://developers.google.com/maps/documentation/javascript/) and an [example showing a google map](https://developers.google.com/maps/documentation/javascript/examples/marker-simple). From this example, we can drop a marker a location in San Francisco:

<img src=figures/first-crime-in-2003.png width=350>

**Getting a google API key**. Google requires that you get a so-called API key for use with every Google Maps request. Follow these steps to get set up:

* Get a google account if you don't already have one.
* Go to the [Google API Console](https://console.developers.google.com/apis/dashboard) and create a project. I call mine msds692-test or something like that.
* Enable the " Google Maps JavaScript API" API from your console (click the "Enable APIs and services" link).

**Exercise**: Using the template below, fill in the `...` latitude and longitude for any place that you'd like to see. And also change `YOUR_API_KEY` to your Google API key.  For example, we can grab a location from the police data. Column 10 (from 0) is the latitude and column 9 is the longitude: 37.7981336020854, -122.427270640646. Save the file as `map.html` and then open it with your browser. Here is the HTML file containing the JavaScript necessary to create a map with a marker:

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

We are going to base our crime heat map on the [Heatmap example](https://developers.google.com/maps/documentation/javascript/examples/layer-heatmap). Because we don't know JavaScript, we are going to use Python to process the CSV file and generate the minimum necessary JavaScript to get this working. For each crime, we will emit a line such as:

```javascript
{lat:37.7765080370233, lng:-122.414457764634},
```

I have split Google's heat map example into two files with a small modification so that we can combine [`heatmap-start.txt`](https://github.com/parrt/msds692/blob/master/notes/code/sfpd/heatmap-start.txt) + those longitude and latitude lines + [`heatmap-end.txt`](https://github.com/parrt/msds692/blob/master/notes/code/sfpd/heatmap-end.txt) into a `heatmap.html` file and then view it in the browser.

**Exercise**: Write a small Python program called `latlng.py` that processes the file specified as an argument and prints out column 10, column 9 but in the format above. It should look like:

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

*The lesson here is that there is no substitute for domain-specific knowledge when analyzing data.*

Ok, to get an accurate picture, we should really filter out the police stations. 

**Exercise**: Modify your `latlng.py` so that it accepts an argument, `-raw`, after the filename that indicates we don't want anything except the latitude and longitude:

```bash
$ python latlng.py /tmp/2016-car-break-ins.csv -raw
37.7251897236748 -122.461683159559
37.775420706711 -122.403404791479
37.7986812884373 -122.415573641104
37.8054616189682 -122.414427932689
37.8035408565775 -122.414878527767
37.7802134292058 -122.509695887518
37.8047715653509 -122.40256476079
37.7814987213218 -122.404934413339
37.7833104067015 -122.388379873919
37.7410156428706 -122.428891058718
37.7884427601235 -122.40034634474
37.7321638759455 -122.421305348396
37.7877002417804 -122.427699766322
...
```

Now, we can use our favorite commandline sequence to get a histogram of these coordinates. First, rerun that program but redirect the output into a file, such as ` /tmp/locs`, using the `>` operator from the shell. Then, do the standard sequence we discussed in the computational boot camp to get a histogram from the shell:

```bash
$ sort < /tmp/locs | uniq -c | sort -r -n |more
 552 37.775420706711 -122.403404791479
 165 37.7784692199467 -122.513642064265
 158 37.7725405391593 -122.466204667893
  92 37.7835100715421 -122.405395493939
  66 37.7580021664589 -122.387316279433
  60 37.7830295716044 -122.431046366089
  56 37.804271887891 -122.44827840533
  54 37.7800332991006 -122.464279879446
  52 37.7822458223917 -122.446612978839
  49 37.7845681170336 -122.431206932079
  46 37.7849531241612 -122.427991151911
  44 37.7827317884887 -122.406481972743
  42 37.7800304351156 -122.432116233695
  38 37.7800478529923 -122.431979576386
...
```

No doubt those first few are the police stations, but let's find out.

**Exercise**: Of course we don't know where those coordinates are so let's plot them on the map using markers as we did in the first exercise. Yep, the first coordinate is definitely the hall of justice:

<img src=figures/hallofjustice.png width=200>

The second coordinate however is a big tourist area at the Cliff House:
 
<img src=figures/cliffhouse.png width=200>

Hmm.. so in 2016, I guess that is the absolute worst place to park your car. (excluding police stations, hahaha). The next coordinate is the DeYoung Museum:

<img src=figures/deyoung.png width=200>

Ok, so it sounds like we just need to strip out the first one to get a more accurate picture.  The Hall of Justice artificially dampens down the other areas because it is three or four times as intense. On the other hand, we have set the max intensity (`heatmap.set('maxIntensity', 40);`) so that this peak did not visually dampen the others. At least we can get rid of that big red dot that is spurious.

Strip out the Hall of Justice using `grep`. First list check if a simple expression will find all of the Hall of Justice. It looks like it:

```bash
$ grep '\-122.403404791479' /tmp/2016-car-break-ins.csv |wc -l
     552
```

That 552 matches the number we see above. So now we can filter that by finding everything else:

```bash
grep -v '\-122.403404791479' /tmp/2016-car-break-ins.csv > /tmp/others.csv
cat heatmap-start.txt > heatmap.html
python latlng.py /tmp/others >> heatmap.html 
cat heatmap-end.txt >> heatmap.html 
open heatmap.html # if on Mac OS X
```

I changed the radius in that JavaScript to be the same as I had for the previous heat map:

```javascript
heatmap.set('radius', 9.5);
```

Ok, so after we stripped out the Hall of Justice, we get basically the same picture but without the spurious value:

<img src=figures/better-2016-car-breakins-heatmap.png width=400>


## What is the worst block in the city?

**Exercise**: Run histogram on the raw latitude and longitude for the entire Police Department records from 2003 to the present. I see something like:

```
58098 37.775420706711 -122.403404791479
9006 37.7642205603745 -122.41965834371
8846 37.7564864109309 -122.406539115148
7339 37.7841893501425 -122.407633520742
7012 37.7650501214668 -122.419671780296
5489 37.7850629421661 -122.406520987144
5201 37.7833862379382 -122.409853729941
5057 37.7725405391593 -122.466204667893
4503 37.7285280627465 -122.475647460786
```

The first coordinate is the Hall of Justice again, but the next one is not a police station it turns out. It is, in fact, likely the worst block in the entire city from casual inspection. It ain't pretty. Yep, The block between 16th and 17th on Mission Street:

<img src=figures/16thbart.png width=200>

What's the second worst? Yep, the area in front of "The General":

<img src=figures/thegeneral.png width=200>

And the next? Yep, Fifth and Market St.

<img src=figures/5thmarket.png width=200>

<hr>

If you get stuck in any of these exercises, you can look at the [code associated with this notes](https://github.com/parrt/msds692/tree/master/notes/code/sfpd).
