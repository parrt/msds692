import tweepy


def loadkeys(filename):
    """"
    load parrt's keys/tokens from CSV file with form
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

user = api.get_user('realDonaldTrump')
print "followers", user.followers_count

for status in tweepy.Cursor(api.user_timeline, id='realDonaldTrump').items(100):
    print status