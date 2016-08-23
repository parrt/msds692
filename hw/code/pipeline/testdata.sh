#!/bin/bash

INPUT=$1
OUTPUT=$2

for f in $INPUT/*.csv
do
	NAME=$(basename -s '.csv' $f)
	echo "Test" $NAME
	python csv2html.py $f > /tmp/$NAME.html
	echo -n "   csv2html: "
	python htmlcompare.py $OUTPUT/$NAME.html /tmp/$NAME.html

	python csv2xml.py $f > /tmp/$NAME.xml
	echo -n "   csv2xml: "
	python xmlcompare.py $OUTPUT/$NAME.xml /tmp/$NAME.xml

	python csv2json.py $f > /tmp/$NAME.json
	echo -n "   csv2json: "
	python jsoncompare.py $OUTPUT/$NAME.json /tmp/$NAME.json

	# test xml from correct output dir -> CSV
	python xml2csv.py $OUTPUT/$NAME.xml > /tmp/$NAME.csv
	echo -n "   xml2csv: "
	python csvcompare.py $INPUT/$NAME.csv /tmp/$NAME.csv

	python json2csv.py $OUTPUT/$NAME.json > /tmp/$NAME.csv
	echo -n "   json2csv: "
	python csvcompare.py $INPUT/$NAME.csv /tmp/$NAME.csv

	python xml2csv.py $OUTPUT/$NAME.xml | python csv2xml.py > /tmp/$NAME.xml
	echo -n "   xml2csv|csv2xml: "
	python xmlcompare.py $OUTPUT/$NAME.xml /tmp/$NAME.xml

	python json2csv.py $OUTPUT/$NAME.json | python csv2json.py > /tmp/$NAME.json
	echo -n "   json2csv|csv2json: "
	python jsoncompare.py $OUTPUT/$NAME.json /tmp/$NAME.json
done
