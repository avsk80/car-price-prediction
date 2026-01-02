import redis 
import os
from dotenv import load_dotenv
from app.core.config import settings
import json

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")

redis_client = redis.StrictRedis.from_url(REDIS_URL)

def set_cached_prediction(key, value, expire=3600):
    """Set a value in the Redis cache."""
    redis_client.set(name=key, value=str(value), ex=expire)

def get_cached_prediction(key):
    """Get a value from the Redis cache."""
    value = redis_client.get(name=key)
    if value:
        return json.loads(value)
    return None