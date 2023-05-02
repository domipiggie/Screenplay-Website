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
    
    for i in range(0, 4):
        randomScripts.append(screenplays[random.randint(0, (len(screenplays)-1))])
    
    return render_template('/web/index.html', randoms=randomScripts)

@app.route("/screen", methods=["GET"])
def screenPage():
    response = make_response(open('./screenplays/'+request.args.get('screen', None), "rb"))
    response.headers['Content-Type'] = 'application/pdf'
    return response

@app.route("/search", methods=["GET"])
def searchPage():
    toSearch = request.args.get('search', None)
    
    if (not toSearch):
        return render_template('/web/search.html', results=screenplays)
    
    if (toSearch == "bátya"):
        return send_file('./static/pics/orangyalok.jpg', mimetype='image/gif')
    
    results = []
    
    for i in screenplays:
        if i[1].lower().find(toSearch.lower()) != -1:
            results.append(i)
    
    return render_template('/web/search.html', results=results)


app.run(host='0.0.0.0', port=8000, debug=True)