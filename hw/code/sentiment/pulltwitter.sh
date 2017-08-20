#!/bin/bash
curl "http://"$(cat IP.txt)"/the_antlr_guy" > parrt-tweets.html
curl "http://"$(cat IP.txt)"/following/the_antlr_guy" > parrt-following.html
curl "http://"$(cat IP.txt)"/realdonaldtrump" > trump-tweets.html
curl "http://"$(cat IP.txt)"/following/realdonaldtrump" > trump-following.html
