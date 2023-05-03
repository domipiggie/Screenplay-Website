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


@app.route("/")
def homePage():
    randomScripts = []
    
    while len(randomScripts) < 4:
        currentScript = screenplays[random.randint(0, (len(screenplays)-1))]
        if currentScript not in randomScripts:
            randomScripts.append(currentScript)
    
    return render_template('/web/index.html', randoms=randomScripts)

@app.route("/s", methods=["GET"])
def screenPage():
    response = make_response(open('./screenplays/'+request.args.get('screen', None), "rb"))
    response.headers['Content-Type'] = 'application/pdf'
    return response

@app.route("/search", methods=["GET"])
def searchPage():
    toSearch = request.args.get('q', None)
    filters = request.args.get('f', None)
    print(filters)
    
    if (not toSearch and not filters):
        return render_template('/web/search.html', results=screenplays)
    
    if (toSearch == "bátya"):
        return send_file('./static/pics/orangyalok.jpg', mimetype='image/gif')
    
    results = []
    
    if (not filters):
        for i in screenplays:
            if i[1].lower().find(toSearch.lower()) != -1:
                results.append(i)
        
        return render_template('/web/search.html', results=results)

    for i in screenplays:
        isCorrect = True
        
        j = 0
        while isCorrect and j < len(filters):
            if (i[3].find(filters[j]) == -1):
                isCorrect = False
            j+=1
        
        if (isCorrect):
            results.append(i)
                
    
    return render_template('/web/search.html', results=results)


app.run(host='0.0.0.0', port=80, debug=True)