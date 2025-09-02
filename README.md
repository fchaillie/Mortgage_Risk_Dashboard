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
