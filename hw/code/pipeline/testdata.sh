#!/bin/bash

INPUT=$1
OUTPUT=$2
MYSRC=~/courses/msan692-private/hw/pipeline

for f in $INPUT/*.csv
do
	NAME=$(basename -s '.csv' $f)
	echo "Test" $NAME
	python csv2html.py $f > /tmp/csv2html-$NAME.html
	echo -n "   csv2html: "
	python $MYSRC/htmlcompare.py $OUTPUT/$NAME.html /tmp/csv2html-$NAME.html

	python csv2xml.py $f > /tmp/csv2xml-$NAME.xml
	echo -n "   csv2xml: "
	python $MYSRC/xmlcompare.py $OUTPUT/$NAME.xml /tmp/csv2xml-$NAME.xml

	python csv2json.py $f > /tmp/csv2json-$NAME.json
	echo -n "   csv2json: "
	python $MYSRC/jsoncompare.py $OUTPUT/$NAME.json /tmp/csv2json-$NAME.json

	# test xml from correct output dir -> CSV
	python xml2csv.py $OUTPUT/$NAME.xml > /tmp/xml2csv-$NAME.csv
	echo -n "   xml2csv: "
	python $MYSRC/csvcompare.py $INPUT/$NAME.csv /tmp/xml2csv-$NAME.csv

	python json2csv.py $OUTPUT/$NAME.json > /tmp/json2csv-$NAME.csv
	echo -n "   json2csv: "
	python $MYSRC/csvcompare.py $INPUT/$NAME.csv /tmp/json2csv-$NAME.csv

	python xml2csv.py $OUTPUT/$NAME.xml | python csv2xml.py > /tmp/xml2csv-csv2xml-$NAME.xml
	echo -n "   xml2csv|csv2xml: "
	python $MYSRC/xmlcompare.py $OUTPUT/$NAME.xml /tmp/xml2csv-csv2xml-$NAME.xml

	python json2csv.py $OUTPUT/$NAME.json | python csv2json.py > /tmp/json2csv-csv2json-$NAME.json
	echo -n "   json2csv|csv2json: "
	python $MYSRC/jsoncompare.py $OUTPUT/$NAME.json /tmp/json2csv-csv2json-$NAME.json
done
