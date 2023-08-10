# Domino Model Monitoring Tutorial

Repo with template files for setting up Domino Model Monitoring.

Domino Model Moniotring Documentation can be found here:
https://docs.dominodatalab.com/en/latest/user_guide/715969/model-monitoring/

Domino’s Model Monitoring uses data from several supported data sources to analyze models in production and alerts you when a model’s performance falls outside the specified range.

Model monitoring uses training and prediction data to track drift for the model’s input features and prediction variables, and alerts you about every feature that exceeds a configurable threshold. If you have ground truth data for the model’s predicted values, Domino can ingest it to produce model quality metrics using standard measures such as accuracy, precision, and recall. Domino can also alert you about every metric that exceeds a threshold.

Setting up Model Monitoring will differ slightly depending on whether the model is deployed in Domino as a Model API or externally to Domino.

## Set Up Monitoring for Domino Model APIs

For setting up model monoitoring on a Domino Model API, this tutorial assumes you already have a trained model in your project ready to go.

This example's model is here: models/ChurnBinaryClassifier.pkl

### (1) Register your training dataet

Domino Model Monitoring needs the dataset your model was trained on to establish a reference baseline for input drift detection. This baseline dataset is registered in Domino as a TrainingSet - a versioned set of data, column information, and other metadata.

TrainingSet docs here:
https://docs.dominodatalab.com/en/latest/api_guide/440de9/trainingsets-use-cases/

This example model was trained on **Test&TrainData/churnTrainingData.csv**

