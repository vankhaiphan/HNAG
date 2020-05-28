from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import pandas as pd
import time
import rdflib

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "hnag/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "hnag/index.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "hnag/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "hnag/login.html", {"message": "Logged out."})

def posts(request):
    # Get start and end point for posts to generate.
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts.
    # lname = []
    # lrating = []
    # limage = []
    dt = []
    # data = pd.read_csv('hnag/data.csv', sep=',')
    # for i in range(start, end + 1):   
    #     lJson = {
    #         "url": data.loc[i][0],
    #         "name": data.loc[i][1],
    #         "rate": data.loc[i][2],
    #         "image": data.loc[i][3]
    #     }
    #     dt.append(lJson)
        # dt.append(f"Post #{i}")

    # Artificially delay speed of response.
    # time.sleep(1)    
    # Return list of posts.
    # print(dt)
    # return JsonResponse({
    #     "posts": dt
    # })

    g = rdflib.Graph()
    g = g.parse("hnag/static/hnag/data.xml", format="xml")

    result = g.query("""
        SELECT DISTINCT ?name ?url ?rating ?image ?id
        WHERE {
            ?place cd:name ?name.
            ?place cd:url ?url.
            ?place cd:rating ?rating.
            ?place cd:image ?image.
            ?place cd:id ?id.
        } 
        ORDER BY (?id)
        LIMIT 12""")
    for row in result:
        print(row.id.toPython())
        lJson = {
            "url": row.url.toPython(),
            "name": row.name.toPython(),
            "rate": row.rating.toPython(),
            "image": row.image.toPython()
        }
        dt.append(lJson)
    return JsonResponse({
        "posts": dt
    })
