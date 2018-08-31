import requests
import bs4
import lxml


res = requests.get('https://en.wikipedia.org/wiki/Machine_Learning')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('.toctext')
# print(hi)
for i in hi:
	print(i.text)
