import sys
import json
import requests
from bs4 import BeautifulSoup
# from flask import Flask, jsonify, render_template, request

# url = "https://www.foody.vn/__get/Place/HomeListPlace?t=1589099207254&page=1&lat=16.051571&lon=108.214897&count=12&districtId=&cateId=&cuisineId=&isReputation=&type=1"
url = "https://www.foody.vn/da-nang"
res = requests.get(url)
# res = requests.get("https://code.junookyo.xyz/api/ncov-moh/")
# print(type(res))
# print(res.content)
# print(res.json())
soup = BeautifulSoup(res.text, "html.parser")
print(soup)
# nres = 10
# journey = soup.find_all("div", class_ = "content-item.ng-scope")[:nres]
# print(journey)

