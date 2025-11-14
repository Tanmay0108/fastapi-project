# ▪ model_service.py: Loads the ML model and performs predictions (with Redis caching)

import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import set_cached_prediction, get_cached_prediction

# First thing is we have to load the model
model = joblib.load(settings.MODEL_PATH) # The path from where we load our model

# Now , if model is loaded then , we will make the predicitions :-

# The user in our fastAPI end point will pass their inputs
# ----> inputs passed by the user will be json objects  
# ----> But , we will write a code in such a way that json converts into python dictionary

# that's why in below we are assuming ---> data: dict

def predict_car_price(data: dict):
    cache_key = " ".join([str(val) for val in data.values()])  # this will return a long string where {user input values are seperated by space} & this will be our unique key 
    # Unique key is used for (caching) purpose
    cached = get_cached_prediction(cache_key)
    if cached:
        return cached
    
    # Our model was trained of DataFrames but the user i/p is on dict
    # That is where we need (Pandas)
    input_data = pd.DataFrame([data]) # dict cnvrtd to dataframe in single row
    prediction = model.predict(input_data)[0]
    set_cached_prediction(cache_key, prediction) # stored in the cache memory  
    return prediction