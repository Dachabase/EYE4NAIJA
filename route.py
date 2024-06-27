from flask import Flask, jsonify,request, render_template
from pymongo import MongoClient
from datetime import datetime,timedelta






app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['reports']

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/reportpage")
def reportpage():
    return render_template("reportpage.html")

@app.route("/safetytips")
def safetytips():
    return render_template("safetyttips.html")

@app.route("/emergency")
def emergency():
    return render_template("emergency.html")

if __name__ == '__main__':
    app.run(debug=True)