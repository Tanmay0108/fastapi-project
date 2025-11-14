#  train_model.py: model training script

# In this file we want (joblib) bcz ---> We will train the model first as well as we will save it


import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from training.train_utils import DATA_FILE_PATH, MODEL_DIR, MODEL_PATH   # DATA_FILE_PATH has location of our dataset

df = (
    pd
    .read_csv(DATA_FILE_PATH)
    .drop_duplicates()
    .drop(columns=['name', 'model', 'edition'])
)

X = df.drop(columns='selling_price')
y = df.selling_price.copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

num_cols = X_train.select_dtypes(include='number').columns.tolist()
cat_cols = [col for col in X_train.columns if col not in num_cols]

num_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipe, num_cols),
    ('cat', cat_pipe, cat_cols)
])

regressor = RandomForestRegressor(
    n_estimators=10, max_depth=5, random_state=42
)

rf_model = Pipeline(steps=[
    ('pre', preprocessor),
    ('reg', regressor)
])
rf_model.fit(X_train, y_train)


# Upto above code ---> The model is being trained 
# Now , we want to save the model

os.makedirs(MODEL_DIR, exist_ok=True)   # This line of code will create a folder inside app folder and a file name inside it called "models" # This is the path/address where the model needs to be saved
joblib.dump(rf_model, MODEL_PATH)  # saved the model

# On terminal run ---> python -m training.train_model

