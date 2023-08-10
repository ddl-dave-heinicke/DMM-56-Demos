import pickle
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from domino_data_capture.data_capture_client import DataCaptureClient
import uuid
import datetime

feature_names = ['displacement', 'horsepower', 'weight', 'origin']
predict_names = ['mpg']
pred_client = DataCaptureClient(feature_names, predict_names)

with open("./artifacts/model.bin", 'rb') as f_in:
    loaded_model = pickle.load(f_in)
    f_in.close()  # close the file 
 
with open("./artifacts/scaler.bin", 'rb') as f_in:
    scaler = pickle.load(f_in)
    f_in.close()
 
def predict(displacement, horsepower, weight, origin, event_id=None):
    transformed_data = scaler.transform(pd.DataFrame([[displacement,horsepower,weight,origin]],columns=["displacement", "horsepower", "weight", "origin"]))
    
    feature_values = [displacement, horsepower, weight, origin]
    predict_values = loaded_model.predict([feature_values])

    event_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
     # Create the unique column ID if it does not exist
    if customer_id is None:
        print(f"No Customer ID found! Creating a new one.")
        customer_id = str(uuid.uuid4())

    pred_client.capturePrediction(feature_values, predict_values, event_id=customer_id, timestamp=event_time)
    
    return dict(predict_value=predict_values[0])