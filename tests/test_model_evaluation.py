import pandas as pd
import joblib
from get_data import download_data
import train  # Import the module, not the function
from sklearn.metrics import confusion_matrix

def test_model_loading():
    """Test that model can be loaded and used"""
    download_data("v1")
    train.main()  # Call the main function from the module
    
    model = joblib.load("model.joblib")
    assert model is not None
    assert hasattr(model, 'predict')

def test_confusion_matrix():
    """Test model predictions and generate confusion matrix for CML"""
    download_data("v1")
    train.main()  # Call the main function from the module
    
    data = pd.read_csv("data/data.csv")
    model = joblib.load("model.joblib")
    
    X = data.drop("species", axis=1)
    y = data["species"]
    predictions = model.predict(X)
    
    # Generate confusion matrix for CML report
    cm = confusion_matrix(y, predictions)
    
    print("\n" + "="*40)
    print("CONFUSION MATRIX (for CML report):")
    print("="*40)
    print("Actual \\ Predicted  setosa  versicolor  virginica")
    species = ['setosa', 'versicolor', 'virginica']
    for i, actual in enumerate(species):
        print(f"{actual:12}      {cm[i]}")
    print("="*40)
    
    accuracy = (predictions == y).mean()
    assert accuracy > 0.8, f"Low accuracy: {accuracy}"