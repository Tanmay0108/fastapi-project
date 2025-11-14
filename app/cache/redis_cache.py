import os
import redis
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL") # Adress of local url stoded in app/core/config.py 

redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)

# Assuming that we already have cached data that user wants to access :-
def get_cached_prediction(key: str):
    value = redis_client.get(key)
    return eval(value) if value else None

# If user request  has not been seen before (OR)
# If not cached data stored , cache it :-
def set_cached_prediction(key: str, value: dict):
    redis_client.set(key, str(value))

