from flask import Flask, request, Response, json
import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

#create api
@app.route('/api/', methods=['GET', 'POST'])
@app.route('/api',methods=['GET', 'POST'])
def predict():

    # Make prediction using model 
    prediction = {1:"Batman Begins",2:"Batman: The Animated Series: Tales of the Dark Knight"}
    return Response(json.dumps(prediction))

if __name__ == '__main__':
   app.run()