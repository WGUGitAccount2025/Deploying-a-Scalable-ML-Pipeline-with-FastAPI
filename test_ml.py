import pytest
# TODO: add necessary import
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# TODO: implement the first test. Change the function name and input as needed
def test_one():
    """
    Testing if the model is a RandomForestClassifier.
    """
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)

    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    Verifying there are 15 columns in the loaded dataset.
    """
    df = pd.read_csv("data/census.csv")
    column_count = 15
    assert len(df.columns) == column_count
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
