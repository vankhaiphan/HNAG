from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import pandas as pd
import time
import rdflib
from underthesea import chunk

# Create your views here.
def index(request):
    # List all user
    # print(User.objects.all())
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
    start = str(int(request.GET.get("start") or 0)).zfill(3)
    end = str(int(request.GET.get("end") or (start + 9))).zfill(3)

    # Generate list of posts.
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
            FILTER (?id >= """ + """'""" + start + """')
            FILTER (?id <= """ + """'""" + end + """')
        } 
        ORDER BY (?id)
        """)
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

def search(request):
    search = str(request.GET.get("search"))
    # print(search)
    rs = chunk(search)
    mon = []
    duong = []
    checkduong = ['Đường', 'đường']
    for i in range(len(rs)):
        if rs[i][1] == 'Np' and rs[i-1][0] in checkduong:
            duong.append(rs[i][0])
        if rs[i][1] == 'Np' and str(rs[i-1][0]).isnumeric():
            soduong = rs[i-1][0] + " " + rs[i][0]
            duong.append(soduong)
        elif rs[i][1] == 'Np':
            mon.append(rs[i][0])    
    # print("Mon:",mon[0])
    # return JsonResponse({
    #     "data": []
    # })
    dt = []
    g = rdflib.Graph()
    g = g.parse("hnag/static/hnag/restaurants.xml", format="xml")
    
    if (len(duong) == 0):        
        result = g.query("""
            SELECT DISTINCT ?name ?address ?url ?rating ?image ?id
            WHERE {
                ?place res:name ?name.
                ?place res:address ?address.
                ?place res:url ?url.
                ?place res:rating ?rating.
                ?place res:image ?image.
                ?place res:id ?id.
                FILTER regex(?name,""" + """'""" + search + """','i').            
            } 
            ORDER BY (?id)
            """)        
    else:
        print(mon)
        print(duong)
        regex = """"""
        for i in range(len(mon)):
            regex += """FILTER regex(?name,""" + """'""" + mon[i] + """','i')."""
        for i in range(len(duong)):
            regex += """FILTER regex(?address,""" + """'""" + duong[i] + """','i')."""
        # print(regex)
        result = g.query("""
            SELECT DISTINCT ?name ?address ?url ?rating ?image ?id
            WHERE {
                ?place res:name ?name.
                ?place res:address ?address.
                ?place res:url ?url.
                ?place res:rating ?rating.
                ?place res:image ?image.
                ?place res:id ?id.
                """ + regex + """            
            } 
            ORDER BY (?id)
            """)        
    for row in result:        
        print(row.id.toPython())
        lJson = {
            "address": row.address.toPython(),
            "url": row.url.toPython(),
            "name": row.name.toPython(),
            "rate": row.rating.toPython(),
            "image": row.image.toPython()
        }
        dt.append(lJson)
    return JsonResponse({
        "posts": dt
    })