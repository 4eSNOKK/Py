import requests
import bs4
import lxml

res = requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(res.text, 'lxml')
links = soup.find_all('a', href = True)
for link in links:
	print(link['href'])