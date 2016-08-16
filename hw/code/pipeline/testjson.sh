#!/bin/bash

# test.sh t.json t.csv
JSON=$1
CSV=$2

python json2csv.py $JSON > /tmp/t.csv
diff /tmp/t.csv $CSV
