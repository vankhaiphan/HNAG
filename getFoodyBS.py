import requests
from bs4 import BeautifulSoup

url = "https://www.foody.vn/da-nang/nha-hang"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
number = 50
journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
rates = soup.findAll("div", class_='point highlight-text')[:number]
images = soup.findAll("div", class_='ri-avatar result-image')[:number]

lname = []
lrating = []
limage = []
for i in range(0, len(journey)):
    sName = journey[i].find("h2").text
    sName.strip("\n\r\n")
    lname.append(sName[43:len(sName) - 39])
    sRating = rates[i].text
    sRating.strip("\n\r\n")
    sRating = float(sRating[38:len(sRating) - 32])
    lrating.append(sRating)
    sImage = images[i].find('img')['src']
    limage.append(sImage)

print(lname)
print(lrating)
print(limage)

# button: //*[@id="scrollLoadingPage"]/a