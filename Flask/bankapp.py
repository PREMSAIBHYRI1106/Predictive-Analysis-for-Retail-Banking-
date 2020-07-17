# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:34:00 2020

@author: Praveen
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from joblib import load

app = Flask(__name__)
model = load('titanic .save')

@app.route('/')
def home():
    return render_template('Frontend.php')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    x_test = [[int(x) for x in request.form.values()]]
    #print(x_test)
    #job column
 
    print(x_test)
    sc=load('standard.save')
    prediction = model.predict(sc.transform(x_test))
    print(prediction)
    output=prediction[0]
    if(output==1):
        return render_template('Frontend.php', prediction_text="He/She will Survive")
    else:
        return render_template('Frontend.php',prediction_text="He/She won't Survive")

if __name__ == "__main__":
    app.run(debug=True)