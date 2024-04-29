# use an API call to extract data - here I chose the Kaggle API to return the dataset as csv files,
# which I use as a data source for the receipts, products, and pastry inventory tables
import os
import requests

# create environment credentials
os.environ['KAGGLE_USERNAME'] = 'gracesaunders02'
os.environ['KAGGLE_KEY'] = '9821db5775436401261fa4452f925a30'

data = 'ylchang/coffee-shop-sample-data-1113' #correct kaggle data name
bad_data = 'ylchang/coffee-shp-sample-data-1113' # incorrect name to test exception handling

# import kaggle API
from kaggle.api.kaggle_api_extended import KaggleApi

if os.environ['KAGGLE_USERNAME'] is None or os.environ['KAGGLE_KEY'] is None:
    raise ValueError("Kaggle API credentials not found. Please set the 'KAGGLE_USERNAME' and 'KAGGLE_KEY' environment variables.")

# initialize the API
api = KaggleApi()
api.authenticate()

# try to download the dataset
try:
    api.dataset_download_files(dataset=data, path='./datasets', unzip=True)
    print("Dataset downloaded successfully.")
except requests.exceptions.RequestException as e:
    # handle network-related errors
    print(f"Network error occurred: {e}")
except Exception as e:
    # handle any other unexpected errors
    print(f"Error occurred: {e}")
