import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
 
with open("./artifacts/model.bin", 'rb') as f_in:
    loaded_model = pickle.load(f_in)
    f_in.close()  # close the file 
 
with open("./artifacts/scaler.bin", 'rb') as f_in:
    scaler = pickle.load(f_in)
    f_in.close()
 
def predict(displacement, horsepower, weight, origin):
    transformed_data = scaler.transform(pd.DataFrame([[displacement,horsepower,weight,origin]],columns=["Displacement", "Horsepower", "Weight", "Origin"]))
    return loaded_model.predict(transformed_data)[0]