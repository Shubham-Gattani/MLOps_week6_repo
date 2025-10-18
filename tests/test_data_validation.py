import pandas as pd
import pytest
import sys
from get_data import download_data

# sys.path.append('/home/shubham29_gattani/MLOps_week2_repo')


def test_data_columns():
    """Test that data has expected columns for both versions"""
    for version in ["v1", "v2"]:
        download_data(version)
        data = pd.read_csv("data/data.csv")
        
        expected_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        assert list(data.columns) == expected_columns, f"Wrong columns in {version}"

def test_no_missing_values():
    """Test that data has no missing values"""
    for version in ["v1", "v2"]:
        download_data(version)
        data = pd.read_csv("data/data.csv")
        assert data.isnull().sum().sum() == 0, f"Missing values in {version}"