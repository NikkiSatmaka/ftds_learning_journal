#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# initiate model and columns
LABEL = ['Not Survived', 'Survived']
with open("final_pipe.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def welcome():
    return "<h3>Welcome to My Backend Model API!</h3>"

@app.route("/predict", methods=["GET", "POST"])
def predict_titanic():
    if request.method == "POST":
        content = request.json
        try:
            new_data = {
                'Pclass': content['passenger_class'],
                'Sex': content['gender'],
                'Age': content['age'],
                'SibSp': content['sibling_spouse'],
                'Parch': content['parent_children'],
                'Fare': content['fare']
            }
            new_data = pd.DataFrame([new_data])
            res = model.predict(new_data)
            result = {
                'class': str(res[0]),
                'class_name': LABEL[res[0]]
            }
            response = jsonify(success=True, result=result)
            return response, 200
        except Exception as e:
            response = jsonify(success=False, error=str(e))
            return response, 400
        
    # return from get method
    return "<p>Please use POST method to predict <em>inference model</em></p>"

app.run(debug=True)