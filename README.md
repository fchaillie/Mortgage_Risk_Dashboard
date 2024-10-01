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
