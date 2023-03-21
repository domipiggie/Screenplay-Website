from datetime import date
from flask import Flask, request, render_template, make_response
from flask_cors import CORS
import sqlite3

DataBase = sqlite3.connect("screenData.db")
DBcursor = DataBase.cursor()
app = Flask(__name__, template_folder="")
CORS(app)

screenplays = [a for a in DBcursor.execute("SELECT * FROM screenplays")]


@app.route("/")
def homePage():
    return render_template('/web/index.html')

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
    
    results = []
    
    for i in screenplays:
        if i[1].lower().find(toSearch.lower()) != -1:
            results.append(i)
    
    return render_template('/web/search.html', results=results)


app.run(host='0.0.0.0', port=8000, debug=True)