import requests
r = requests.get('http://www.cnn.com')
print(r.text)
