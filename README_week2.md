# **MLOps Week 2 Assignment – DVC Integration with GCS**

## 📌 Objective

The goal of this assignment is to integrate **Data Version Control (DVC)** into the existing **IRIS ML pipeline** and configure **Google Cloud Storage (GCS)** as the remote storage for data and model versioning.
We demonstrate how to:

* Track datasets and models using DVC
* Push and pull data to/from GCS
* Version control experiments using Git tags
* Switch between dataset/model versions with `dvc checkout`

---

## 📁 Repository Structure

| File / Folder                | Description                                                                                                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **get_data.py**              | Downloads the Iris dataset (v1 or v2) from the configured GCS bucket. The version can be passed as an argument (`--version v1` or `--version v2`). The downloaded file is saved as `data/data.csv`. |
| **train.py**                 | Reads the dataset, splits it into training and test sets, trains a Decision Tree classifier, evaluates accuracy, prints the result, and saves the trained model as `model.joblib`.                  |
| **requirements.txt**         | Contains all Python dependencies required for the project, including DVC and GCS support libraries.                                                                                                 |
| **.gitignore**               | Specifies which files and directories should be ignored by Git (e.g., `.env/`, `.dvc/`, cache files).                                                                                               |
| **mlops_week2_commands.txt** | Contains the full sequence of shell commands used to execute the assignment end-to-end — from repo setup, DVC configuration, training, data/model versioning, to version switching.                 |

---

## 🧠 Summary of Workflow

1. Initialize Git and DVC.
2. Configure GCS bucket as DVC remote storage.
3. Download versioned datasets using `get_data.py`.
4. Train and save models using `train.py`.
5. Track data and models with DVC (`dvc add`).
6. Commit and push versions to GCS (`dvc push`).
7. Use Git tags and `dvc checkout` to switch between versions.
