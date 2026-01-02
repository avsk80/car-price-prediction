from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_current_user, get_api_key
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float

@router.post("/predict")
def predict_price(features: CarFeatures, user = Depends(get_current_user), api_key = Depends(get_api_key)):
    feature_dict = features.model_dump()
    predicted_price = predict_car_price(feature_dict)
    return {"predicted_price": f'{predicted_price:,.2f}'}

