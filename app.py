
from flask import Flask, render_template, request

import pandas as pd
import petrol_price_prediction
app = Flask(__name__,template_folder="templates",static_folder="static")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def submit():
    if request.method =="POST":
        dollar = request.form["dollar"]
        barrel = request.form["barrel"]
        price= petrol_price_prediction.model.predict([[dollar, barrel]])

    return render_template("result.html",a = dollar, b=barrel, c = price)

if __name__=="__main__":
    app.run(debug=True)