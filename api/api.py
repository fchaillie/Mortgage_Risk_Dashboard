
import pandas as pd
import numpy as np
import mlflow
from flask import Flask, render_template, jsonify, request
import json
import requests
from lime import lime_tabular
import pickle

app = Flask(__name__)

# Getting the prediction of the model for a client
@app.route("/score/")
def score():
    # Load the model
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    args = request.args
    df = pd.DataFrame([args])

    # Convert all columns to floats
    df = df.map(lambda x: pd.to_numeric(x, errors ='coerce'))

    happy = loaded_model.predict_proba(df.values, num_iteration = loaded_model.best_iteration_)[:, 1]
    print(happy[0])
    return str(happy[0])

# Creating a table to compare the clients with the 2 groups of customers (good and bad ones)
@app.route("/valeur_moyenne/")
def valeur_moyenne():
    
    args = request.args
    df = pd.DataFrame([args])

    # Convert all columns to floats
    df = df.map(lambda x: pd.to_numeric(x, errors='coerce'))
    
    resume = pd.read_csv('train_df_less_features.csv')
    feats = ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "PAYMENT_RATE", "DAYS_BIRTH", "DAYS_EMPLOYED",
             "DAYS_EMPLOYED_PERC", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH", "AMT_ANNUITY", "ANNUITY_INCOME_PERC",
             "INSTAL_DBD_MEAN", "REGION_POPULATION_RELATIVE","TARGET"]
    resume = resume[feats]
    resume = round(resume.groupby('TARGET').mean(),2)

    # Rename the index (row labels)
    resume = resume.rename({0: 'Clients sans complication', 1: 'Clients avec complications'})

    # Add a new row with a label and values
    new_row_label = 'Demandeur de prêt'
    new_row_values = df.values[0]  
    resume.loc[new_row_label] = new_row_values
    resume = resume.rename_axis("Features")
    resume = resume.T
    resume_json = resume.to_json(orient='split')

    return resume_json



# Getting the personal features that explained the prediction for that client
@app.route("/prediction/")
def askpersonalfeatures():
    
    
    train_df = pd.read_csv('train_df_less_features.csv')
    feats = ["EXT_SOURCE_1", "EXT_SOURCE_2", "EXT_SOURCE_3", "PAYMENT_RATE", "DAYS_BIRTH", "DAYS_EMPLOYED",
             "DAYS_EMPLOYED_PERC", "DAYS_REGISTRATION", "DAYS_ID_PUBLISH", "AMT_ANNUITY", "ANNUITY_INCOME_PERC",
             "INSTAL_DBD_MEAN", "REGION_POPULATION_RELATIVE"]
    train_df = train_df[feats]
    args = request.args
    df = pd.DataFrame([args])

    # Convert all columns to floats
    df = df.map(lambda x: pd.to_numeric(x, errors='coerce'))
    
   # load the model
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Creating the explainer
    explainer = lime_tabular.LimeTabularExplainer(train_df.values, 
                                                  feature_names = feats, 
                                                  class_names = ['0','1'], 
                                                  verbose = True, 
                                                  mode = 'classification',
                                                  discretize_continuous=False)
    

    exp = explainer.explain_instance(df.values[0],loaded_model.predict_proba, num_features = 5)  
   
    return pickle.dumps(exp)
    
    
if __name__ == "__main__":
    app.run(debug=True)