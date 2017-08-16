# Twitter sentiment analysis


install flask, jinja2, tweepy, vaderSentiment pip install colour

log in to twitter app mgmt, click on "create new app"

E.g.,

<img src="figures/twitter-app-creation.png" width=500>

leave callback URL blank

Then for that app, click "Keys and Access Tokens". that shows consumer key/secret, access token, secret.

https://apps.twitter.com/

docs for http://jinja.pocoo.org/docs/2.9/templates/

Get max 100 tweets

http://localhost:8080/the_antlr_guy

<img src=figures/parrt-tweets.png width=800>

http://localhost:8080/realdonaldtrump

<img src=figures/trump-tweets.png width=800>

another page http://localhost:8080/following/the_antlr_guy

SORTED reverse by followers

<img src=figures/trump-follows.png width=400>

<img src=figures/parrt-follows.png width=400>

each text should be link to tweet. underline when hovering but not normally.

figure out how to make square bullets, font size 70%, font family Verdana, sans-serif. h1 is 130% size

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