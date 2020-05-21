import sys
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():  
    # lname = []
    # lrating = []
    # limage = []
    # for j in range(1,6):
    #     url = "https://www.foody.vn/da-nang/nha-hang"
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
    #         lname.append(sName[43:len(sName) - 39])
    #         sRating = rates[i].text
    #         sRating.strip("\n\r\n")
    #         sRating = float(sRating[38:len(sRating) - 32])
    #         lrating.append(sRating)
    #         sImage = images[i].find('img')['src']
    #         limage.append(sImage)
    # return render_template("index.html", lname = lname, lrating = lrating, limage = limage) 
    return render_template("index.html")
@app.route("/login")
def login(): 
    return render_template("login.html")

@app.route("/posts", methods=["POST"])
def posts():

    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    lname = []
    lrating = []
    limage = []
    dt = []
    data = pd.read_csv('data.csv', sep=',')
    for i in range(start, end + 1):   
        lJson = {
            "name": data.loc[i][0],
            "rate": data.loc[i][1],
            "image": data.loc[i][2]
        }
        dt.append(lJson)
        # dt.append(f"Post #{i}")

    # Artificially delay speed of response.
    time.sleep(1)    
    # Return list of posts.
    # print(dt)
    return jsonify(dt)
      
if __name__ == "__main__":
    app.run(debug=True)    