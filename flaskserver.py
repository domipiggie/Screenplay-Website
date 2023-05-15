from datetime import date
from flask import Flask, request, render_template, make_response, send_file
from flask_cors import CORS
import sqlite3
import random

DataBase = sqlite3.connect("screenData.db")
DBcursor = DataBase.cursor()
app = Flask(__name__, template_folder="")
CORS(app)

screenplays = [a for a in DBcursor.execute("SELECT * FROM screenplays ORDER BY screenplays.title")]

def titleOrAuthContainSearch(screenplay, searchKey):
    return screenplay[1].lower().find(searchKey.lower()) != -1 or screenplay[2].lower().find(searchKey.lower()) != -1

def screenplayContainGenre(screenplay, genreList):
    isCorrect = False
            
    j = 0
    while not isCorrect and j < len(genreList):
        if (screenplay[3].lower().find(genreList[j]) != -1):
            isCorrect = True
        j+=1
    
    return isCorrect

def screenplayContainType(screenplay, typeList):
    isCorrect = False
            
    j = 0
    while not isCorrect and j < len(typeList):
        if (screenplay[4].find(typeList[j]) != -1):
            isCorrect = True
        j+=1
    
    return isCorrect
    

@app.route("/")
def homePage():
    randomScripts = []
    
    while len(randomScripts) < 4:
        currentScript = screenplays[random.randint(0, (len(screenplays)-1))]
        if currentScript not in randomScripts:
            randomScripts.append(currentScript)
    
    return render_template('web/index.html', randoms=randomScripts)

@app.route("/s", methods=["GET"])
def screenPage():
    return send_file('screenplays/'+request.args.get('screen', None))

@app.route("/search", methods=["GET"])
def searchPage():
    toSearch = request.args.get('q', None)
    filters = request.args.get('f', None)
    types = request.args.get('t', None)
    
    if (not toSearch and not filters and not types):
        return render_template('web/search.html', results=screenplays)
    
    if (toSearch == "bátya"):
        return send_file('static/pics/orangyalok.jpg', mimetype='image/gif')
    
    results = []
    
    if (not filters and not types):
        for i in screenplays:
            if (titleOrAuthContainSearch(i, toSearch)):
                results.append(i)
        
        return render_template('web/search.html', results=results)
    
    if (not types):
        filters = filters.split(",")
        print(filters)
        
        for i in screenplays:
            if (titleOrAuthContainSearch(i, toSearch) and screenplayContainGenre(i, filters)):
                results.append(i)
            
        return render_template('web/search.html', results=results)
    
    if (not filters):
        types = types.split(",")
        print(types)
        
        for i in screenplays:
            if (titleOrAuthContainSearch(i, toSearch) and screenplayContainType(i, types)):
                results.append(i)
            
        return render_template('web/search.html', results=results)
    
    filters = filters.split(",")
    types = types.split(",")
    print(filters, types)
    
    for i in screenplays:
        if (titleOrAuthContainSearch(i, toSearch) and screenplayContainGenre(i, filters) and screenplayContainType(i, types)):
            results.append(i)
    
    return render_template('web/search.html', results=results)



app.run(host='0.0.0.0', port=80, debug=True)