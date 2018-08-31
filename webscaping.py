import requests
import bs4
import lxml


res = requests.get('https://learncodeonline.in')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hi = soup.select('title')


print(hi)