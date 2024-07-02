Loan_Project_API Repository Summary:

This is a project for a loan company that needs to predict the likelyhood that new clients will not reimburse their loan given the information on their loan request. The client information is entered in a dashboard and interacts with an API before returning an answer saying if the loan request is accepted or not. The files in this repository "Loan_Project_API" are only for the building of the API on Heroku.

Details:

The main file for the API is "api.py".
The file "finalized_model.sav" is the prediction model in Pickle format.
The file "Procfile" informs Heroku that it is an API that I am launching.
The file "pyvenv.cfg" gives information on the configuration of my PC.
The file "requirement.txt" lists the necessary packages to install to run the API.
The file "runtime.text" gives the Python version used.
The file "train_df_less_features.csv" will be used to compare the information of a new client with the information of the ones we already have. 
