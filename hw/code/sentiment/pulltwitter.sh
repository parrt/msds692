#!/bin/bash
IP=$(cat IP.txt)
curl "http://"$IP"/fchollet" > fchollet-tweets.html
curl "http://"$IP"/following/fchollet" > fchollet-following.html
curl "http://"$IP"/the_antlr_guy" > parrt-tweets.html
curl "http://"$IP"/following/the_antlr_guy" > parrt-following.html
