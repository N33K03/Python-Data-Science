import requests

url_get = 'http://httpbin.org/get'   # GET appended to the end
payload = {'name':'Joseph', 'ID':'123'}  # creates a query string
r = requests.get(url_get, params=payload) # pass the dictionary payload to the params parameter of the get() function
print('GET request data', r.url)
print(r.json()) # content type formatted using json method

url_post = 'http://httpbin.org/post' # send POST request
r_post = requests.post(url_post, data=payload) # uses data parameter
print('Post request data', r_post.url)
print(r_post.json()['form']) # view the key form to get the pay load