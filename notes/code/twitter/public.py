# Pull in parrt's public tweets using REST API at twitter
# It appears Twitter's Search API searches recent tweets from the past 7-9 days and the
# search is rate limited to 180 queries per 15 minute window.

import tweepy

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
    = loadkeys("/Users/parrt/Dropbox/licenses/twitter.csv")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text