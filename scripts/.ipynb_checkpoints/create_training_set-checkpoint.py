from domino.training_sets import TrainingSetClient, model
import pandas as pd
import numpy as np
import os
import random
 #new code
# defining the column names
cols_car = ['mpg','cylinders','displacement','horsepower','weight',
                'acceleration', 'model year', 'origin']
 
# reading the .data file using pandas
df = pd.read_csv('/mnt/data/data.csv', names=cols_car, na_values = "?",
                comment = '\t',
                sep= " ",
                skipinitialspace=True)
# pare down data
df = df[["mpg", "displacement", "horsepower", "weight", "origin"]]
df.reset_index(inplace=True)
df.rename(columns={'index':'customer_id'}, inplace=True)
# making a copy of the dataframe
data = df.copy()
 
# imputing the values with median (due to presence of outliers)
median = data.iloc[:,3].median()
data.iloc[:,3] = data.iloc[:,3].fillna(median)
data.info()
 
training_df = data
 
training_df['origin'] = training_df['origin'].astype(float)
 
tsv = TrainingSetClient.create_training_set_version(
    training_set_name="auto-prediction-training-data-{}-{}".format(os.environ['DOMINO_PROJECT_OWNER'], os.environ['DOMINO_PROJECT_ID']),
    df=training_df,
    key_columns=['customer_id'],
    target_columns=["mpg"],
    exclude_columns=[],
    meta={"meta_data": "1"},
    monitoring_meta=model.MonitoringMeta(**{
        "categorical_columns": [],
        "timestamp_columns": [],
        "ordinal_columns": []
    }),
    project_name=os.environ['DOMINO_PROJECT_NAME']
)
 
print(f"TrainingSetVersion {tsv.training_set_name}:{tsv.number}")
#new code