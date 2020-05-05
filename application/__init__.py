from flask import Flask, request, Response, json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import pandas as pd
import math
import re
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
import seaborn as sns
#from surprise import Reader, Dataset, SVD
sns.set_style("darkgrid")
#from surprise.model_selection import cross_validate, KFold
from model import Pearson_Model


app = Flask(__name__)


loaded_p_model = pickle.load(open("C:/Users/Yelena/Desktop/p_model.sav", 'rb'))


#create api
@app.route('/api/', methods=['GET', 'POST'])
@app.route('/api',methods=['GET', 'POST'])
def predict():
    # Get the data from POST request
    data = request.get_json(force=True)

    return Response(loaded_p_model.recommend(data, 10))

if __name__ == '__main__':
   app.run()
