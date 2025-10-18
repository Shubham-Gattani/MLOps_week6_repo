import argparse
from google.cloud import storage
import os
import pandas as pd

def download_data(version="v1"):
    """
    Download specific version of Iris dataset from GCS
    """
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    version_map = {
        "v1": "source-data/data_v1.csv",
        "v2": "source-data/data_v2.csv"
    }

    bucket_name = "mlops-iris-week2-graded-unique-shubhamg"
    source_blob_name = version_map[version]
    destination_file_name = "data/data.csv"

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print(f"Downloaded {source_blob_name} to {destination_file_name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=["v1", "v2"], default="v1", help="Data version to download")
    args = parser.parse_args()
    download_data(args.version)

if __name__ == "__main__":
    main()