"Provided by Stephen Hsu, MSAN 2017 student"
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#link to consumer and access token: https://dev.twitter.com/ 
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

class StdOutListener(StreamListener):
    """
    link on other information to get from tweets: 
    https://dev.twitter.com/overview/api/entities-in-twitter-objects.

    Credit to https://www.dataquest.io/blog/streaming-data-python/
    for on_data and on_error 
    """
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        print(tweet)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #capture data by keywords, more useful on popular terms 
    stream.filter(track=['trump'])
