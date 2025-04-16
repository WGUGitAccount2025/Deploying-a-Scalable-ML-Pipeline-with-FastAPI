import pytest
# TODO: add necessary import
import os
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from train_model import X_train, y_train
from ml.model import compute_model_metrics, train_model

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Verifying there are 15 columns in the loaded dataset.
    """
    project_path = "/home/hurn/Deploying-a-Scalable-ML-Pipeline-with-FastAPI"
    data_path = os.path.join(project_path, "data", "census.csv")
    df = pd.read_csv(data_path)
    column_count = 15
    assert len(df.columns) == column_count
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Tests the train_model function to ensure it trains a model successfully
    """
    model = train_model(X_train, y_train)
    assert hasattr(model, 'n_features_in_'), "Model has not been trained (fitted)."
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    Test if the model pickle file loads correctly.
    """
    pickle_result = False
    try:
        with open("model/model.pkl", "rb") as f:
            pickle.load(f)
        pickle_result = True
    except:
        print("Error loading pickle file in test_ml.py")

    assert pickle_result == True
    pass
