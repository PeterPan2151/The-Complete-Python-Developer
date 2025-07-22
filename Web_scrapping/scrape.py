import requests
from bs4 import BeautifulSoup
import pprint

# titleline
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline>a')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['Votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):

        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'Votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtext))