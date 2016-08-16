#!/bin/bash

# test.sh t.csv stripped-output
# test.sh AAPL.csv stripped-output
CSV=$1
NAME=$(basename -s '.csv' $CSV)
echo $NAME
SOLUTION_DIR=$2

# Get all html on on one line and remove whitespace
python csv2html.py $CSV | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/$NAME.html
diff /tmp/$NAME.html $SOLUTION_DIR/$NAME.html

python csv2xml.py $CSV  | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/$NAME.xml
diff /tmp/$NAME.xml $SOLUTION_DIR/$NAME.xml

python csv2json.py $CSV | tr -d '\n' | tr -d '\t' | tr -d ' ' > /tmp/$NAME.json
diff /tmp/$NAME.json $SOLUTION_DIR/$NAME.json
