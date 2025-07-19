import requests
from bs4 import BeautifulSoup

# titleline
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline')
votes = soup.select('.score')
