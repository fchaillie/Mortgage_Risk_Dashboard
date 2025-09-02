# Mortgage_Risk_Dashboard
## Home Loan Provider Dashboard Summary:
 
A home loan provider needs to predict the probability that new loan applicants will reimburse their loan given the information on their loan request. The client information is entered in a dashboard that interacts with an API before returning an answer. 

The files in this repository are only for the building of the dashboard on Heroku with Streamlit. The repository "Home Loan Provider API" covers the API on Heroku and the repository "Home Loan Provider Models and Data" covers the data used and the predictive model creation.

**Details of the files:**

1) Main file for the appearance of the dashboard: "dashboard.py"
2) "Procfile" informs Heroku that it is with Streamlit that the dashboard will be launched.
3) "requirement.txt" lists the packages to install to make this dashboard.
4) "runtime.text" gives the Python version used.
5) "tests" has the tests that will be executed every time I push a file on this branch (Github Actions).
6) "Pipfile", "Pipfile.lock", "setup.sh" and folder "src" configurate the dashboard according to my system settings.
## Home Loan Provider API Summary:

A home loan provider needs to predict the probability that new loan applicants will reimburse their loan given the information on their loan request. The client information is entered in a dashboard that interacts with an API before returning an answer. The files in this repository are only for the building of the API on Heroku. The repository "Home Loan Provider Dashboard" covers the dahsboard and the repository "Home Loan Provider Models and Data" covers the data used and the predictive model creation.

**Details for each file:**

1) "api.py" is the main file for the API.
2) "finalized_model.sav" is the predictive model in Pickle format.
3) "Procfile" informs Heroku that it is an API that I am launching.
4) "pyvenv.cfg" gives information on the configuration of my PC.
5) "requirement.txt" lists the necessary packages to install to run the API.
6) "runtime.text" gives the Python version used.
7) "train_df_less_features.csv" will be used to compare the information of a new client with the information of the ones we already have. 
## Loan Provider Models and Data Summary

The 4 notebooks are related to the data used and the predictive model.

**Details of each file:**

**Notebook "Business_metrics":**
I build a confusion matrix to find the most profitable credit default threshold (between 0 and 1) to be used by the home loan provider to determine whether a loan is granted or not to a new client. If the probability of default given by the model for a client is higher than the threshold then the loan is not granted.

**Notebook "Data_Drift":**
I analyze the data drift between the train data and the test data to see if there is a fundamental change in the data, using the library Evidently.
If there is a significant difference between the 2 sets then the data needs to be changed so that the train data and test data look similar statistically speaking.

**Notebook "Model_Balanced_Classes":**
I test the Light GBM model with the 2 unbalanced classes ("good" clinets and "bad" clients) and I load that model on the site ML Flow (mlflow.org) for tracking purposes. Then I do the same for the model with the 2 classes that are balanced this time.

**Notebook "Model_Creation_and_ML_Flow_Upload":**
I test the Light GBM model with 798 features then test the model with only the most important 13 features. Then I upload the lighter model on ML Flow.
