#!/bin/bash

# test.sh t.xml t.csv
XML=$1
CSV=$2

python xml2csv.py $XML > /tmp/t.csv
diff /tmp/t.csv $CSV
