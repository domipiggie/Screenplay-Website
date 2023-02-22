from datetime import date
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__, template_folder="web")
CORS(app)

screenplays = [
    {
        'author': 'Scott Roberts based on screenplay by Patrick Meyers',
        'title': 'K 2',
        'shortDesc': 'Very cool thing'
    },
    {
        'author': 'Irene Mecchi & Jonathan Roberts',
        'title': 'The Lion King',
        'shortDesc': 'Even cooler thing'
    },
    {
        'author': 'Robert Riskin, based on the novel by James Hilton',
        'title': 'Lost Horizon',
        'shortDesc': 'omg cool thing'
    }
]


@app.route("/")
def homePage():
    return render_template('index.html')

@app.route("/search", methods=["GET"])
def searchPage():
    toSearch = request.args.get('search', None)
    
    if (not toSearch):
        print("eee")
        return render_template('search.html')
    
    results = []
    
    for i in screenplays:
        if i['title'].find(toSearch) != -1:
            results.append(i)
    
    return render_template('search.html', results=results)


app.run(host='0.0.0.0', port=8000, debug=True)