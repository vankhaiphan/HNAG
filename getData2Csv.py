# import requests
# from bs4 import BeautifulSoup
# import json

# # Adding to JSON 
# def add_json(data, filename='data.json'): 
#     with open(filename,'w') as f: 
#         json.dump(data, f, indent=4)     

# lname = []
# lrating = []
# limage = []
# for j in range(1,2):
#     url = "https://www.foody.vn/da-nang/nha-hang?page=" + str(j) + "#!#page" + str(j)
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'html.parser')
#     number = 12
#     journey = soup.findAll("div", class_='row-item filter-result-item')[:number]
#     rates = soup.findAll("div", class_='point highlight-text')[:number]
#     images = soup.findAll("div", class_='ri-avatar result-image')[:number]

#     for i in range(0, len(journey)):
#         sName = journey[i].find("h2").text
#         sName.strip("\n\r\n")
#         sName = sName[43:len(sName) - 39]
#         print(sName)
#         lname.append(sName)
#         sRating = rates[i].text
#         sRating.strip("\n\r\n")
#         sRating = sRating[38:len(sRating) - 32]
#         sRating = float(sRating)
#         lrating.append(sRating)
#         sImage = images[i].find('img')['src']
#         limage.append(sImage)
#         lJson = {
#             "name": sName,
#             "rate": sRating,
#             "image": sImage
#         }
#         with open("data.json") as json_file:
#             data = json.load(json_file)
#             temp = data["data"]
#             temp.append(lJson)
#         add_json(data)
# print(lname)

# import csv

# f = open("data.csv", "w")
# with f:
#     fnames = ["name", "rate", "image"]
#     writer = csv.DictWriter(f, fieldnames=fnames)    

#     writer.writeheader()
#     lJson = {
#             "name": "Gogi",
#             "rate": 8.6,
#             "image": "linkGogi"
#         }
#     writer.writerow(lJson)

# f = open("data.csv", "a")
# with f:
#     fnames = ["name", "rate", "image"]
#     writer = csv.DictWriter(f, fieldnames=fnames)    

#     # writer.writeheader()
#     lJson = {
#             "name": "Godddadafadssddddgi",
#             "rate": 8.6,
#             "image": "linkGogi"
#         }
#     writer.writerow(lJson)
import pandas as pd
# from ftfy import fix_encoding
data = pd.read_csv('data.csv', sep=',')
print(data.loc[5][0])
# s = str(data.loc[0][0], 'utf-8')
# s = s.encode("utf-8")
# s = str(data.loc[0][0])
# s = fix_encoding(s)
# s = s.decode("utf-8")
# print(s)
# from flask import Flask, jsonify, render_template, request
# app = Flask(__name__)
# start = 0
# end = 1
# lname = []
# lrating = []
# limage = []
# for i in range(start, end + 1): 
#     lname.append(str(data.loc[i][0]))
#     lrating.append(float(data.loc[i][1]))
#     limage.append(str(data.loc[i][2]))
# # print(limage)
# print(jsonify({
#         "name":lname,
#         "rating":lrating,
#         # "image":limage
#     }))

