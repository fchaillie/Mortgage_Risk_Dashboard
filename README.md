**Loan Project Dashboard Summary:**

A loan company that needs to predict the likelyhood that new clients will not reimburse their loan given the information on their loan request. 
The client information is entered in a dashboard and interacts with an API before returning an answer saying if the loan request is accepted or not. 

The files in this Loan_Project_Dashboard branch are for the dashboard made with Streamlit on Heroku. It used by the company staff. 
The files in the other branch "Loan_Project_Models_and_data" are related to the models used and the data used for the final model put on the cloud.

**Details of the files in this "Loan_Project_Dashboard" branch:**

Main file for the appearance of the dashboard: "dashboard.py"
"Procfile" informs Heroku that it is with Streamlit that the dashboard will be launched.
"requirement.txt" lists the packages to install to make this dashboard.
"runtime.text" gives the Python version used.
"tests" has the tests that will be executed every time I push a file on this branch (Github Actions).
Files "Pipfile", "Pipfile.lock", "setup.sh" and the folder "src" configurate the dashboard according to my system settings.
