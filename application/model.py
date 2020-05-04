import numpy as np
import pickle
import pandas as pd
import math
import re
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt
#from surprise import Reader, Dataset, SVD
#sns.set_style("darkgrid")
#from surprise.model_selection import cross_validate, KFold


class Pearson_Model:
    
    def __init__(self, df_title, df_p, df_movie_summary):
        self.df_title = df_title
        self.df_p = df_p
        self.df_movie_summary = df_movie_summary
           
    def recommend(self, movie_title, top_number, min_count = 0):
        
        print("For movie ({})".format(movie_title))
        print("- Top "+str(top_number)+" movies recommended based on Pearsons'R correlation - ")    
        i = int(self.df_title.index[self.df_title['Name'] == movie_title][0])
        target = self.df_p[i]
        similar_to_target = self.df_p.corrwith(target)
        corr_target = pd.DataFrame(similar_to_target, columns = ['PearsonR'])
        corr_target.dropna(inplace = True)
        corr_target = corr_target.sort_values('PearsonR', ascending = False)
        corr_target.index = corr_target.index.map(int)
        corr_target = corr_target.join(self.df_title).join(self.df_movie_summary)[['PearsonR', 'Name', 'count', 'mean']]
        print(corr_target[corr_target['count']>min_count][:top_number].to_string(index=False))