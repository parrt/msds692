# Twitter sentiment analysis

The goal of this project is to learn how to pull twitter data, using the [tweepy](http://www.tweepy.org/) wrapper around the twitter API, and how to perform simple sentiment analysis using the [vaderSentiment](https://github.com/cjhutto/vaderSentiment) library.  The tweepy library hides all of the complexity necessary to handshake with Twitter's server for a secure connection.

As you did in the recommendation engine project, you will also produce a web server running at AWS to display the most recent 100 tweets from a given user and the list of users followed by a given user. For example, in response to URL `/the_antlr_guy` (`http://localhost/the_antlr_guy` when tested on your laptop), your web server should respond with a tweet list color-coded by sentiment, using a red to green gradient:

<img src=figures/parrt-tweets.png width=800>

As another example URL `/realdonaldtrump` yields:

<img src=figures/trump-tweets.png width=750>

Next you will create a page responding to URLs, such as `/following/the_antlr_guy`, that displays the list of users followed by a given user:

<img src=figures/parrt-follows.png width=320>

Or:

<img src=figures/trump-follows.png width=350>

Note that the users should be sorted in reverse order by their number of followers. Just to be clear, `/following/the_antlr_guy` shows the list of users that I follow sorted by how many followers those users have. Clearly, Guido has the most followers and so he is shown first in my list of people I follow.

## Discussion

### Mining for tweets

    create a list of tweets where each tweet is a dictionary with the
    following keys:

       id: tweet ID
       created: tweet creation date
       retweeted: number of retweets
       text: text of the tweet
       hashtags: list of hashtags mentioned in the tweet
       urls: list of URLs mentioned in the tweet
       mentions: list of screen names mentioned in the tweet
       score: the "compound" polarity score from vader's polarity_scores()

    Return a dictionary containing keys-value pairs:

       user: user's screen name
       count: number of tweets
       tweets: list of tweets, each tweet is a dictionary

following

       name: real name
       screen_name: Twitter screen name
       followers: number of followers
       created: created date (no time info)
       image: the URL of the profile's image
### Generating HTML pages

```html
<li style="list-style:square; font-size:70%; font-family:Verdana, sans-serif; color:#ea4c00">
    -0.68: <a style="color:#ea4c00" href="https://twitter.com/the_antlr_guy/status/897491721944158208">RT @kotlin: Kotlin 1.1.4 is out! Auto-generating Parcelable impls, JS dead code elimination, package-default nullability &amp;amp; more: https://t.…</a>
</li>
```

```html
<tr>
    <td align=center width="80"><img src="http://pbs.twimg.com/profile_images/424495004/GuidoAvatar_normal.jpg"></td>
    <td style="font-size:70%; font-family:Verdana, sans-serif">
        <a href="https://twitter.com/gvanrossum">Guido van Rossum</a><br>
        98538 followers<br>
        Since 2008-08-11
    </td>
</tr>
```

### Authenticating with the twitter API server

Twitter requires that you register as a user and then also create an "app" for which he will give you authentication credentials. These credentials are needed for making requests to the API server. Start by logging in to [twitter app management](https://apps.twitter.com/) then click on "create new app". It should show you a dialog box such as the following, but of course you would fill in your own details:

<img src="figures/twitter-app-creation.png" width=500>

For the website, you can link to your LinkedIn account or something or even your github account. Leave the "callback URL" blank.

Once you have created that app, go to that app page. Click on the  "Keys and Access Tokens" tabs, which shows 4 key pieces that represent your authentication information:

* Consumer Key (API Key)
* Consumer Secret (API Secret)
* Access Token
* Access Token Secret	

Under the Permissions tab, make sure that you have your access as "Read only" for this application. This prevents a bug in your software from doing something horrible to your twitter account!

**We never encode secrets in source code**, consequently, we need to pass that information into our web server every time we launch. To prevent having to type that every time, we will store those keys and secrets in a CSV file format:

    consumer_key, consumer_secret, access_token, access_token_secret

The server then takes a commandline argument indicating the file name of this data. For example, I pass in my secrets via file name:

$ sudo python server.py ~/Dropbox/licenses/twitter.csv

Please keep in mind the [limits imposed by the twitter API](https://dev.twitter.com/rest/public/rate-limits). For example, you can only do 15 follower list fetches per 15 minute window, but you can do 900 user timeline fetches.

docs for http://jinja.pocoo.org/docs/2.9/templates/

Get max 100 tweets

each text should be link to tweet. underline when hovering but not normally.

'user' 
'count'
'tweets'

for each tweet:

"id"
"created"
"retweeted"
"text"
"hashtags"
"urls"
"mentions"

## Getting started

Download the [starterkit](https://github.com/parrt/msan692/tree/master/hw/code/sentiment), which has the following files and structure:

```
```

install flask, jinja2, tweepy, vaderSentiment pip install colour


## Deliverables

## Evaluation

To evaluate your projects, the grader and I will