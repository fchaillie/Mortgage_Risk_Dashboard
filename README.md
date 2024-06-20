Welcome to the Readme section !

Summary: The files in this repository "projet7_api" are linked to a project where I put a model on the cloud through the site Heroku using an API.
The model predicts the likelyhood that a new client could reimburse a loan given the information on the loan request. The client information is entered in a dashboard that interacts with an API on Heroku. 

All the files in this repository are used mainly to create the API on Heroku.
The main file for the API is "api.py".
The file "finalized_model.sav" is the prediction model in Pickle format.
The file "Procfile" informs Heroku that it is an API that I am launching.
The file "pyvenv.cfg" gives information on the configuration of my PC.
The file "requirement.txt" lists the necessary packages to install to run the API.
The file "runtime.text" gives the Python version used.
The file "train_df_less_features.csv" will be used to compare the information of a new client with the information of the ones we already have. 
