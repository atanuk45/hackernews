
#self try
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')    #2page
#print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')    #2page
#print(soup.find(id="score_35130975"))
links = soup.select('.titleline >a')   
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline >a')      #2page
subtext2 = soup2.select('.subtext')         #2page
#print(votes[0].getText())
#print(votes[3].getText())
def sorted_by_votes(hnlist):
	return sorted(hnlist, key=lambda item : item['votes'],reverse=True)

def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			#print(points)
			if points>99:
				hn.append({'title':title,'link':href, 'votes':points})
	return hn

def create_custom_hn2(links2, subtext2):
	hn = []
	for idx, item in enumerate(links2):
		title = links2[idx].getText()
		href = links2[idx].get('href', None)
		vote = subtext2[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			#print(points)
			if points>99:
				hn.append({'title':title,'link':href, 'votes':points})
	return hn




page1 = create_custom_hn(links, subtext)
page2 = create_custom_hn2(links2, subtext2)
page1.extend(page2)

pprint.pprint(sorted_by_votes(page1))
