import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.ibm.com/uk-en')

# creates a BeautifulSoup object
soup = BeautifulSoup(page, 'html.parser')

# pulls all instances of <a> tag
artists = soup.find_all('a')

# clears data of all tags
for artist in artists:
    names = artist.contents[0]
    print(names)
