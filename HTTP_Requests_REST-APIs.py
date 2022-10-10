import requests
url = 'HTTP://www.IBM.com/'
r = requests.get(url)
print(r.request.headers)
header = r.headers # gives list of headers
print(header['date']) # gives date
print(header['Content-Type']) # gives content type
print(r.encoding) # checks the encoding
print(r.text[0:100]) # gives first 100 characters of the text file

