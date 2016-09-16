#!/bin/bash

USER=$1
MYSRC=~/courses/msan692-private/hw/pipeline

for t in TSLA VBK
do
	echo "Testing" $t

	# Test GET
	curl -s http://$USER.pythonanywhere.com/history/$t > /tmp/$t.html
	curl -s http://parrt.pythonanywhere.com/history/$t > /tmp/parrt-$t.html
        python $MYSRC/htmlcompare.py /tmp/$t.html /tmp/parrt-$t.html

	# Test POST
	curl -s --data "ticker=$t" http://$USER.pythonanywhere.com/history > /tmp/post-$t.html
	curl -s --data "ticker=$t" http://parrt.pythonanywhere.com/history > /tmp/parrt-post-$t.html
        python $MYSRC/htmlcompare.py /tmp/post-$t.html /tmp/parrt-post-$t.html

	# Test GET JSON
	curl -s http://$USER.pythonanywhere.com/data/$t > /tmp/$t.json
	curl -s http://parrt.pythonanywhere.com/data/$t > /tmp/parrt-$t.json
        python $MYSRC/jsoncompare.py /tmp/$t.json /tmp/parrt-$t.json
done
