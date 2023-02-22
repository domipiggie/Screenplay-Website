from datetime import date
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/getTest')
def hello_world():
    return {
        "greeting": ["hello", "world"],
        "date": date.today()
    }

@app.route('/', methods=['GET','POST'])
def webhook():
    if request.method == 'POST':
        print("Data received is: ", request.json)
        return {
            "yes": ["yes", "yes"]
        }

app.run(host='0.0.0.0', port=8000)