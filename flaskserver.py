from datetime import date
from flask import Flask, request, render_template
from flask_cors import CORS


app = Flask(__name__, template_folder="web")
CORS(app)

screenplays = [
    {
        'author': 'Jon Dough',
        'title': 'Lorem`s ipsum',
        'shortDesc': 'Very cool thing'
    },
    {
        'author': 'Yu Ya',
        'title': 'idk',
        'shortDesc': 'Even cooler thing'
    }
]


@app.route("/")
def main():
    return render_template('index.html', screenplays=screenplays)


app.run(host='0.0.0.0', port=8000, debug=True)