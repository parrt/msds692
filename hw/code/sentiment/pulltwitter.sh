#!/bin/bash
IP=$(cat IP.txt)
curl "http://"$IP"/the_antlr_guy" > parrt-tweets.html
curl "http://"$IP"/following/the_antlr_guy" > parrt-following.html
curl "http://"$IP"/joebiden" > joebiden-tweets.html
curl "http://"$IP"/following/joebiden" > joebiden-following.html
