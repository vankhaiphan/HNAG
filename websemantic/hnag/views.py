from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import pandas as pd
import time
import rdflib
from underthesea import chunk
from SPARQLWrapper import SPARQLWrapper, JSON
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
    start = str(int(request.GET.get("start") or 0))
    end = str(int(request.GET.get("end") or (start + 9)))

    # Generate list of posts.
    dt = []

    # g = rdflib.Graph()
    # g = g.parse("hnag/static/hnag/data.xml", format="xml")
    g = SPARQLWrapper("http://localhost:7200/repositories/HNAG")

    queryString = """
        PREFIX res: <http://www.hnag.com/>
        SELECT DISTINCT ?name ?url ?rating ?image ?id
        WHERE {
            ?place res:name ?name.
            ?place res:url ?url.
            ?place res:rating ?rating.
            ?place res:image ?image.
            ?place res:id ?id.  
            FILTER (?id >= """ + start + """)
            FILTER (?id <= """ + end + """)
        } 
        ORDER BY (?id)
        """
    g.setQuery(queryString)
    g.setReturnFormat(JSON)
    results = g.query().convert()
    # for result in results:
    #     print(result)
    for row in results["results"]["bindings"]:
        print(row["id"]["value"])
        lJson = {
            "url": row["url"]["value"],
            "name": row["name"]["value"],
            "rate": row["rating"]["value"],
            "image": row["image"]["value"]
        }
        dt.append(lJson)
    return JsonResponse({
        "posts": dt
    })

def search(request):
    search = str(request.GET.get("search"))
    # print(search)
    rs = chunk(search)
    print(rs)
    mon = []
    duong = []
    checkduong = ['Đường', 'đường']
    for i in range(len(rs)):
        if rs[i][1] in ['Np','N','M'] and rs[i-1][0] in checkduong:
            duong.append(rs[i][0])
        elif rs[i][1] in ['Np','N','M'] and str(rs[i-1][0]).isnumeric():
            soduong = rs[i-1][0] + " " + rs[i][0]
            duong.append(soduong)
        elif rs[i][1] == 'Np':
            mon.append(rs[i][0])    
    print("Đường: ",duong)
    print("Món: ", mon)
    # return JsonResponse({
    #     "data": []
    # })
    dt = []
    # g = rdflib.Graph()
    # g = g.parse("hnag/static/hnag/restaurants.xml", format="xml")
    g = SPARQLWrapper("http://localhost:7200/repositories/HNAG")
    
    if (len(duong) == 0): 
        if (len(mon) == 0):      
            queryString = """
                PREFIX res: <http://www.hnag.com/>
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
                """
            print(queryString)
            g.setQuery(queryString)
            
        else:
            queryString = """
                PREFIX res: <http://www.hnag.com/>
                SELECT DISTINCT ?name ?address ?url ?rating ?image ?id
                WHERE {
                    ?place res:name ?name.
                    ?place res:address ?address.
                    ?place res:url ?url.
                    ?place res:rating ?rating.
                    ?place res:image ?image.
                    ?place res:id ?id.
                    FILTER regex(?name,""" + """'""" + mon[0] + """','i').            
                } 
                ORDER BY (?id)
                """
            print(queryString)
            g.setQuery(queryString)
    else:
        print(mon)
        print(duong)
        regex = """"""
        for i in range(len(mon)):
            regex += """FILTER regex(?name,""" + """'""" + mon[i] + """','i')."""
        for i in range(len(duong)):
            regex += """FILTER regex(?street,""" + """'""" + duong[i] + """','i')."""
        print(regex)
        queryString = """
            PREFIX res: <http://www.hnag.com/>
            SELECT DISTINCT ?name ?address ?url ?rating ?image ?id
            WHERE {
                ?place res:name ?name.
                ?place res:address ?address.
                ?address res:street ?street.
                ?place res:url ?url.
                ?place res:rating ?rating.
                ?place res:image ?image.
                ?place res:id ?id.
                """ + regex + """            
            } 
            ORDER BY (?id)
            """
        print(queryString)
        g.setQuery(queryString) 
    g.setReturnFormat(JSON)
    results = g.query().convert() 
    
    for row in results["results"]["bindings"]:
        print(row["id"]["value"])
        lJson = {
            "url": row["url"]["value"],
            "name": row["name"]["value"],
            "rate": row["rating"]["value"],
            "image": row["image"]["value"]
        }
        dt.append(lJson)
    return JsonResponse({
        "posts": dt
    })