import joblib
import pandas as pd
from app.core.config import settings
from app.cache.redis_cache import get_cached_prediction, set_cached_prediction

model = joblib.load(settings.MODEL_PATH)

def predict_car_price(data: dict) -> float:
    cache_key = "".join([str(value) for value in data.values()])
    cached_price = get_cached_prediction(cache_key)
    if cached_price:
        return cached_price
    
    input_df = pd.DataFrame([data])
    predicted_price = model.predict(input_df)[0]
    set_cached_prediction(cache_key, predicted_price)
    return predicted_price
