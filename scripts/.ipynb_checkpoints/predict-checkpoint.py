import pickle
# import numpy as np
import pandas as pd
# from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
# from sklearn.compose import ColumnTransformer
from domino_data_capture.data_capture_client import DataCaptureClient
import datetime
import uuid
 
# List the columns to score & monitor for drift
feature_names = ["dropperc", "mins", "consecmonths", "income", "age"]

# List the target column name
predict_names = ['churn_Y']

# Configure the DataCaptureClient to capture the specified features and target column name
pred_client = DataCaptureClient(feature_names, predict_names)
 
# Load the serialized model
with open("./models/ChurnBinaryClassifier.pkl", 'rb') as f_in:
    loaded_model = pickle.load(f_in)
    f_in.close()  # close the file 


# with open("./artifacts/scaler.bin", 'rb') as f_in:
#     scaler = pickle.load(f_in)
#     f_in.close()

scaler = StandardScaler()
    
def predict(dropperc, mins, consecmonths, income, age, customer_id=None):

    transformed_data = scaler.transform(pd.DataFrame([[dropperc, mins, consecmonths, income, age]],columns=["dropperc", "mins", "consecmonths", "income", "age"]))
    
    prediction = loaded_model.predict(transformed_data)
    print(prediction)
    
    # Create the unique column ID if it does not exist
    if customer_id is None:
        print(f"No Customer ID found! Creating a new one.")
        customer_id = str(uuid.uuid4())
    
    print(f"New Customer ID is: {customer_id}")
    #event_time = datetime.datetime.now(datetime.timezone.utc).isoformat()
    feature_array = list([dropperc, mins, consecmonths, income, age])
    pred_array = list(prediction)
    print(type(feature_array))
    print(type(prediction))
    print(type(customer_id))
    pred_client.capturePrediction(feature_array, prediction, event_id=customer_id)
    
    return dict(prediction=prediction[0])
 
# def predict_unscaled(displacement, horsepower, weight, origin, customer_id=None):
#     feature_values = [displacement, horsepower, weight, origin]
#     prediction = loaded_model.predict([feature_values]).tolist()
#     if customer_id is None:
#         print(f"No Customer ID found! Creating a new one.")
#         customer_id = str(uuid.uuid4())
#     print(f"New Customer ID is: {customer_id}")
#     pred_client.capturePrediction(feature_values, prediction, event_id=customer_id)
#     return dict(prediction=prediction[0])