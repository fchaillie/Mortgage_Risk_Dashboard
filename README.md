## Loan Provider API Summary:

A loan provider needs to predict the probability that new loan applicants will reimburse their loan given the information on their loan request. The client information is entered in a dashboard that interacts with an API before returning an answer. The files in this repository "Loan_Project_API" are only for the building of the API on Heroku. The other repository "Loan_Project_Dashboard" cover the dahsboard and the data used for the predictive model.

**Details for each file:**

1) "api.py" is the main file for the API.
2) "finalized_model.sav" is the predictive model in Pickle format.
3) "Procfile" informs Heroku that it is an API that I am launching.
4) "pyvenv.cfg" gives information on the configuration of my PC.
5) "requirement.txt" lists the necessary packages to install to run the API.
6) "runtime.text" gives the Python version used.
7) "train_df_less_features.csv" will be used to compare the information of a new client with the information of the ones we already have. 
