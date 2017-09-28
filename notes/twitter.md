# Mining for tweets

## Getting access to twitter data

Sign in with your twitter account at [apps.twitter.com](https://apps.twitter.com/). Click on "Create New App". I made mine `USF-parrt-teaching`.  Click on that new app when it appears, then the "Keys and Access Tokens" tab. You should find and copy into a secure file on your laptop the *consumer_key, consumer_secret, access_token, access_token_secret*.  I store them in a one-line CSV file for convenient use in apps. We never want to expose these by putting into source code literally. More info in the [sentiment project description](https://github.com/parrt/msan692/blob/master/hw/sentiment.md).

## Tweet feeds

Twitter provides [URLs that allow us to search recent tweets](https://developer.twitter.com/en/docs/tweets/search/overview) but it's fairly inconvenient and so we use library called [tweepy](http://tweepy.readthedocs.io/en/v3.5.0/).  You will likely have to install that.

It appears Twitter's Search API searches recent tweets from the past 7-9 days and the search is rate-limited to 180 queries per 15 minute window.

Here is a simple example from the tweepy getting started documentation that pulls from the public home timeline:

```python
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
```

That assumes that you have set variables `consumer_key, consumer_secret, access_token, access_token_secret`. To do that, I have it read directly from my secret file:

```python
def loadkeys(filename):
    """"
    load keys/tokens from CSV file with form
    consumer_key, consumer_secret, access_token, access_token_secret
    """
    with open(filename) as f:
        items = f.readline().strip().split(', ')
        return items

consumer_key, consumer_secret, \
access_token, access_token_secret \
    = loadkeys("/Users/parrt/licenses/twitter.csv")
...
```

Here are is the [API reference for tweepy](http://tweepy.readthedocs.io/en/v3.5.0/api.html).  For example, here is how to get an object describing Donald Trump:

```python
user = api.get_user('realDonaldTrump')
```

To print the number of followers, you can reference `user.followers_count`.

**Exercise**:  Get the code from above working to show the public tweets and then pick a Twitter user and print their followers count and other details you find from the [API reference](http://docs.tweepy.org/en/v3.5.0/api.html?highlight=get_user#API.get_user).

## Cursors

For very large results, we need to use [cursors](http://tweepy.readthedocs.io/en/v3.5.0/cursor_tutorial.html) that handle getting page 1, page 2, etc... of tweets. Here's how to get the first 100 tweets for Donald Trump:

```python
for status in tweepy.Cursor(api.user_timeline, id='realDonaldTrump').items(100):
    print status
```

**Exercise**: Pick another user and print out there most recent tweets.

## Streaming API

From tweepy doc: "*The Twitter streaming API is used to download twitter messages in real time. It is useful for obtaining a high volume of tweets, or for creating a live feed using a site stream or user stream.*"

Stephen Hsu, MSAN2017, sent me this nice snippet to [listen in on the twitter feed](https://github.com/parrt/msan692/blob/master/notes/code/twitter/tweetstream.py).

Here is a [nice tutorial on the streaming API](https://www.dataquest.io/blog/streaming-data-python/).