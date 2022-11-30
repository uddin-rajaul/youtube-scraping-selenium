import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/feed/trending'

response = requests.get(url)
print('response ', response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
