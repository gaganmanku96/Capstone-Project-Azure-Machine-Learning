import os
import argparse
import joblib

import pandas as pd
import numpy as np
from azureml.core.run import Run
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from azureml.data.dataset_factory import TabularDatasetFactory

dataset_url = "https://raw.githubusercontent.com/gaganmanku96/Capstone-Project-Azure-Machine-Learning/master/heart_failure_clinical_records_dataset.csv"

ds = TabularDatasetFactory.from_delimited_files(dataset_url)

ds = ds.to_pandas_dataframe()

def get_data(dataframe):
    y = dataframe.pop('DEATH_EVENT')
    x = dataframe
    return x, y
   
x, y = get_data(ds)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.30, random_state=4)

run = Run.get_context()
    
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(train_x, train_y)

    accuracy = model.score(test_x, test_y)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()

