import csv
from collections import Counter

def get_columns(filename,col):
    """
    Load CSV in Excel format, return Counter created from column of data indicated by
    integer col parameter.
    """
    data = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, dialect='excel')
        for row in reader:
            data.append(row[col])

    data = Counter(data)
    return data
