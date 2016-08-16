#!/bin/bash

# test.sh t.csv stripped-output
# test.sh AAPL.csv stripped-output
CSV=$1
NAME=$(basename -s '.csv' $CSV)
SOLUTION_DIR=$2

# Get all html on on one line and remove whitespace
python csv2html.py $CSV > /tmp/$NAME.html
cat /tmp/$NAME.html | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/stripped-$NAME.html
diff /tmp/stripped-$NAME.html $SOLUTION_DIR/$NAME.html

python csv2xml.py $CSV > /tmp/$NAME.xml
cat /tmp/$NAME.xml | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/stripped-$NAME.xml
diff /tmp/stripped-$NAME.xml $SOLUTION_DIR/$NAME.xml

python csv2json.py $CSV > /tmp/$NAME.json
cat /tmp/$NAME.json | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/stripped-$NAME.json
diff /tmp/stripped-$NAME.json $SOLUTION_DIR/$NAME.json
