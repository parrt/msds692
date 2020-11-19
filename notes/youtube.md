# YouTube

YouTube, like Zillow, will allow us to use its data spigot without authentication, but we must create a secret ID or key as we did before:

> If your client application does not use OAuth 2.0, then it must include an API key when it calls an API that's enabled within a Google Cloud Platform project. The application passes this key into all API requests as a key=API_key parameter. API keys do not grant access to any account information, and are not used for authorization.

Follow these steps to get set up:
 
1. [Get a google account](https://www.google.com/accounts) if you don't already have one.
2. Go to the [Google API Console](https://console.developers.google.com/) and create a project. I call mine msds692-test or something like that.
3. Enable the "YouTube Data API v3" API from your console.

[Never store your API key in your code](https://www.zdnet.com/article/over-100000-github-repos-have-leaked-api-or-cryptographic-keys/).

Familiarize yourself with the [API documentation](https://developers.google.com/youtube/v3/) and install some Python code that will make our lives easier:

```bash
$ pip install --ignore-installed --upgrade google-api-python-client
```

(The `--ignore-installed` avoids errors on El Capitan OS X.)

## First contact

The Python library we are using hides all of the direct URL access so that this code will look different than what we did for Zillow. Using our developer key, we `build()` an object that acts like a proxy, letting us communicate with YouTube:

```python
# code from https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
import sys
import urllib
from googleapiclient.discovery import build

DEVELOPER_KEY = sys.argv[1]
QUERY = sys.argv[2] # e.g., "cats and dogs"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
```

Given that object, we can make a search, retrieving a list of elements:

```python
search_response = youtube.search().list(
    q=QUERY,            # search terms
    part="id,snippet",  # what we want back
    maxResults=20,      # how many results we want back
    type="video"        # only tell me about videos
).execute()
```

**Exercise**: The `search_response` variable is a `dict` with an `items` key containing the search results. Use the debugger or look at [API documentation](https://developers.google.com/youtube/v3/docs/search/list) to figure out what the elements of the individual search responses are. As usual, it appears there is a small discrepancy between the documentation and what I see in the actual dictionary. Figure out how to print the title and a link to the videos returned from the search. E.g., Running from the command-line, we should get:

```bash
$ python search.py MYSECRETKEY cats
Funny Cats Compilation [Most See] Funny Cat Videos Ever Part 1 https://www.youtube.com/watch?v=tntOCGkgt98
Cats are just the funniest pets ever - Funny cat compilation https://www.youtube.com/watch?v=htOroIbxiFY
Funny Cats - A Funny Cat Videos Compilation 2016 || NEW HD https://www.youtube.com/watch?v=G8KpPw303PY
Funny Cats Compilation 2016  - Best Funny Cat Videos Ever || Funny Vines https://www.youtube.com/watch?v=njSyHmcEdkw
Cats Being Jerks Video Compilation || FailArmy https://www.youtube.com/watch?v=O1KW3ZkLtuo
Cats are super funny creatures that make us laugh - Funny cat & kitten compilation https://www.youtube.com/watch?v=Zwq98O42ta0
Funny Videos Of Funny Cats Compilation 2016 [BEST OF] https://www.youtube.com/watch?v=9nZMHBDw8os
Passive Aggressive Cats Video Compilation 2016 https://www.youtube.com/watch?v=lx3egn8v4Mg
Cats are simply funny, clumsy and cute! - Funny cat compilation https://www.youtube.com/watch?v=PK2939Jji3M
Startled Cats Compilation https://www.youtube.com/watch?v=6U_XREUMOAU
People Try Walking Their Cats https://www.youtube.com/watch?v=9C1leq--_wM
Cats Saying "No" to Bath - A Funny Cats In Water Compilation https://www.youtube.com/watch?v=Wmz0wGx5sq8
Bad Cats Video Compilation 2016 https://www.youtube.com/watch?v=MXOj8yVu1fA
11 Cats You Won’t Believe Actually Exist! https://www.youtube.com/watch?v=QtMmgzGYih0
Cuddly Cats Video Compilation 2016 https://www.youtube.com/watch?v=bw5WtZmU-i0
Cats, funniest creatures in animal kingdom - Funny cat compilation https://www.youtube.com/watch?v=qIDEC2h4dZo
Funny Cats Vine Compilation September 2015 https://www.youtube.com/watch?v=HxM46vRJMZs
Adam Ruins Everything - Why Going Outside is Bad for Cats https://www.youtube.com/watch?v=GpAFpwDVBJQ
Funny Cat Videos - Cat Vines Compilation https://www.youtube.com/watch?v=VJHnPUFffCU
Gangsta Cats Video Compilation 2016 https://www.youtube.com/watch?v=VS6UOyTb5eU
```

## Getting all video comments

Now that we know how to perform a video search, let's learn how to extract comments for particular video. 

**Exercise**: We will extract comments by video ID, because that is what the [API](https://developers.google.com/youtube/v3/docs/commentThreads/list) requires. Here are two sample video IDs:

```python
videoId = "gU_gYzwTbYQ"  # bonkers the cat
videoId = "tntOCGkgt98"  # cat compilation
```

You need to call `youtube.commentThreads().list(...)` to get the comments. There is a bunch of sample code in the API documentation. Follow the code samples to extract the author and text of the top level comments. Here's a sample session:

```bash
$ python comments_one_video.py MYSECRET KEY
Comment by Humbly_Bumbly: STOP REPEATING THE SAME CLIPS﻿
Comment by mad rix: cute 😀 Come to my YouTube chanel i have lovely videos of my cats! !!!﻿
Comment by LuksterCOD1234: God this has got a lot of views﻿
Comment by DIAMOND BRAIN: No,no and no﻿
Comment by Lea Villanueva: 7:45 😂﻿
Comment by Andre Jackson: old school﻿
Comment by Chris Poerschke: "most see" ?﻿
Comment by Animalsworlds: Awesome video, my sadness immediately disappear after watching this video 
=)﻿
Comment by Vanirvis: Whats with the boxes on the screen? Thumbs down.﻿
...
```

*Please do not bring up videos that could be offensive to your fellow students!*

**Exercise**: Now let's combine the search with the comment retrieval so that we find all comments associated with, say, 10 videos. Create a function that returns a list of video IDs (cut/paste from previous functionality):

```pyhon
def videoIDs(query):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, ...)
    ...
    return ids
```

and a function that returns a dictionary mapping video ID to a list of comment strings:

```
def comments(query):
    ids = videoIDs(query)
    comments = {} # map video ID to list of comment strings
    for id in ids:
        ... previous code to pull comments ...
        comments[id] = []
        for item in results["items"]:
            ...
            comments[id].append("Comment by %s: %s" % (author, text))
    return comments
```

Then the main program can just print out a list of comments for each video, putting a tab in front of the comments so it's easier to see which video they are associated with.

```python
allcomments = comments(QUERY)
for vid in allcomments.keys()[:5]: # just 5 videos
    comments = allcomments[vid]
    print("Video "+vid)
    print("\t",)
    print('\n\t'.join(comments))
```

Sample output:

```bash
$ python comments.py SECRETKEY 'star wards'
...
Video zKoBk37EKG4
	Comment by Jamie Carey: I want a pug
	Comment by Arissa Williams: Like your videos and jokes can I please have a shout-out I subscribed and like 
	Comment by sharonda scarboro: Did the superhero kids get to come to your house DP subscribe did they leave a comment if you did they ask
...
```
	
