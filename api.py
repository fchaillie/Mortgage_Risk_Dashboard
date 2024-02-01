# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import mlflow
from flask import Flask, render_template, jsonify, request
import json
import requests
from lime import lime_tabular
import pickle

app = Flask(__name__)


@app.route("/valeur_moyenne/")
def valeur_moyenne():
    
    args = request.args
    df = pd.DataFrame([args])
    # Convert all columns to floats
    df = df.map(lambda x: pd.to_numeric(x, errors='coerce'))
    print(df.values[0])
    
    resume = pd.read_csv('C:\\Users\\flore\\Desktop\\opensclass\\Projet 7\\virtual7\\stuff\\train_df_all_features.csv')
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
    print(resume)
    print(type(resume))
    
    resume_json = resume.to_json(orient='split')
    return resume_json

@app.route("/score/")
def score():
     # load the model from disk
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    args = request.args
    df = pd.DataFrame([args])
    # Convert all columns to floats
    df = df.applymap(lambda x: pd.to_numeric(x, errors='coerce'))
    happy = loaded_model.predict_proba(df.values, num_iteration=loaded_model.best_iteration_)[:, 1]
    # Parse the string as a list containing float(s)
    print(happy[0])
    return str(happy[0])

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
    
   # load the model from disk
    filename = 'finalized_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Création de l'explainer
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