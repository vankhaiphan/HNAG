import sys
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():  
    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    lname = []
    lrating = []
    limage = []

    data = pd.read_csv('data.csv', sep=',')
    for i in range(start, end + 1):        
        lname.append(data.loc[i][0])
        lrating.append(data.loc[i][1])
        limage.append(data.loc[i][2])

    # Artificially delay speed of response.
    time.sleep(1)

    # Return list of posts.
    print(jsonify({
        "name":lname,
        "rating":lrating,
        "image":limage
    }))

@app.route("/posts", methods=["POST"])
def posts():

    # Get start and end point for posts to generate.
    start = int(request.form.get("start") or 0)
    end = int(request.form.get("end") or (start + 9))

    # Generate list of posts.
    lname = []
    lrating = []
    limage = []

    data = pd.read_csv('data.csv', sep=',')
    for i in range(start, end + 1):        
        lname.append(data.loc[i][0])
        lrating.append(data.loc[i][1])
        limage.append(data.loc[i][2])

    # Artificially delay speed of response.
    time.sleep(1)

    # Return list of posts.
    print(jsonify({
        "name":lname,
        "rating":lrating,
        "image":limage
    }))
      
if __name__ == "__main__":
    app.run(debug=True)    