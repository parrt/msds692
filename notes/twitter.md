# Mining for tweets

## Getting access to twitter data

Sign in with your twitter account at [apps.twitter.com](https://apps.twitter.com/). Click on "Create New App". I made mine `USF-parrt-teaching'.  Click on that new app when it appears, then the `Keys and Access Tokens` tab. You should find and copy into a secure file on your laptop the consumer_key, consumer_secret, access_token, access_token_secret.  I store them in a one-line CSV file for convenient use in apps. We never want to expose these by putting into source code literally.

## Tweet feeds

Twitter provides [URLs that allow us to access their data](https://developer.twitter.com/en/docs/tweets/search/overview) but it's fairly inconvenient and so we use library called [tweepy](http://tweepy.readthedocs.io/en/v3.5.0/).  You will likely have to install that.

It appears Twitter's Search API searches recent tweets from the past 7-9 days and the search is rate limited to 180 queries per 15 minute window.