
from bs4 import BeautifulSoup
import requests
url = 'http://www.prnewswire.com/news-releases/dutch-philosopher-koert-van-mensvoort-founder-of-the-next-nature-network-writes-a-letter-to-humanity-619925063.html'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup)
links = soup.find_all('div', {'class': 'image'})
print ([i.find('img')['src'] for i in links])
print ([i.find('img')['title'] for i in links])