import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#url = 'http://web.mta.info/developers/turnstile.html'
url = 'http://www.delfi.ee'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#print soup.prettify()
#print(soup.findAll('a'))

for link in soup.findAll('a'):
    if link.text.strip():
        print(link.text.strip())
