import requests
import json
import sys

name = sys.argv[1]
URL = f"http://openpayments.us/data?query={name}"

r = requests.get(URL)
data = json.loads(r.text)

print(json.dumps(data, indent=4))
