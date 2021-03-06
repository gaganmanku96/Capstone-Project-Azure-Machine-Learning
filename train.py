import os
import argparse
import joblib

import pandas as pd
import numpy as np
from scipy.sparse import data
from azureml.core.run import Run
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from azureml.data.dataset_factory import TabularDatasetFactory

dataset_url = "https://raw.githubusercontent.com/gaganmanku96/Capstone-Project-Azure-Machine-Learning/master/students_placement_data.csv"

ds = TabularDatasetFactory.from_delimited_files(dataset_url)
# ds = pd.read_csv('students_placement_data.csv')

ds = ds.to_pandas_dataframe()

def get_data(dataframe):
    dataframe.drop('roll_no', axis=1, inplace=True)

    dataframe['gender'] = dataframe['gender'].apply(lambda x: 1 if str(x) == 'M' else 0)
    dataframe['section'] = dataframe['section'].apply(lambda x: 1 if str(x) == 'A' else 0)
    dataframe['registered_for_placement_training'] = dataframe['registered_for_placement_training'].apply(lambda x: 1 if str(x) == 'YES' else 0)
    dataframe['placement_status'] = dataframe['placement_status'].apply(lambda x: 1 if str(x) == 'Placed' else 0)

    y = dataframe.pop('placement_status')
    x = dataframe
    return x, y
   
x, y = get_data(ds)
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.30, random_state=4)

run = Run.get_context()
    
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_est', type=int, default=50, help="Number of Estimators")
    parser.add_argument('--min_samples_split', type=int, default=2, help="Minimum samples split")

    args = parser.parse_args()

    run.log("Number of estimators:", np.float(args.n_est))
    run.log("Min Samples split:", np.int(args.min_samples_split))

    model = RandomForestClassifier(n_estimators=args.n_est, min_samples_split=args.min_samples_split).fit(train_x, train_y)
    accuracy = model.score(test_x, test_y)
    run.log("Accuracy", np.float(accuracy))
    joblib.dump(value=model,filename="./hyperdrive_model.pkl")


if __name__ == '__main__':
    main()
