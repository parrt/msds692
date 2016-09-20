# YouTube

YouTube, like Zillow, will allow us to use its data spigot without authentication, but we must create a secret ID or key as we did before:

> If your client application does not use OAuth 2.0, then it must include an API key when it calls an API that's enabled within a Google Cloud Platform project. The application passes this key into all API requests as a key=API_key parameter. API keys do not grant access to any account information, and are not used for authorization.

Follow these steps to get set up:
 
1. [Get a google account](https://www.google.com/accounts) if you don't already have one.
2. Go to the [Google API Console](https://console.developers.google.com/) and create a project. I call mine msan692-test or something like that.
3. Enable the "YouTube Data API v3" API from your console.

Familiarize yourself with the [API documentation](https://developers.google.com/youtube/v3/) and install some Python code that will make our lives easier:

```bash
$ pip install --upgrade google-api-python-client
```

## First contact

The Python library we are using hides all of the direct URL access so that this code will look different than what we did for Zillow. Using our developer key, we `build()` an object that acts like a proxy, letting us communicate with YouTube:

```python
# code from https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword
import sys
import urllib
from googleapiclient.discovery import build

DEVELOPER_KEY = sys.argv[1]
QUERY = sys.argv[2] # e.g., "cats and dogs"
QUERY = urllib.quote(QUERY)
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

**Exercise**: The `search_response` variable is a `dict` with an `items` key containing the search results. Use the debugger or look at [API documentation](https://developers.google.com/youtube/v3/docs/videos#properties) to figure out what the elements of the individual search responses are. As usual, it appears there is a small discrepancy between the documentation and what I see in the actual dictionary. Figure out how to print the title and a link to the videos returned from the search. E.g., Running from the command-line, we should get:

```bash
$ search.py MYSECRETKEY cats
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
