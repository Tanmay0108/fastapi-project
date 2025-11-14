# train_utils.py : common functions to support model training


import os

DATA_DIR = 'data'  # folder name 
DATA_FILE_NAME = 'car-details.csv'    # file name
DATA_FILE_PATH = os.path.join(DATA_DIR, DATA_FILE_NAME)   # from this address we will read the data

APP_DIR = 'app'   # our trained model is in app folder  
MODEL_DIR_NAME = 'models'
MODEL_NAME = 'model.joblib'
MODEL_DIR = os.path.join(APP_DIR, MODEL_DIR_NAME) # will give us app/model
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)  # will give us the path of our trained model as well as ous tarined model will be saved in this path



