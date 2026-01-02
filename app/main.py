from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.api import routes_predict, routes_auth
from app.middleware.logging_middleware import LoggingMiddleware
from app.core.exceptions import register_exception_handlers

app = FastAPI(title="Car Price Prediction API", version="1.0.0")

# Register exception handlers
app.add_middleware(LoggingMiddleware)

# link routes
app.include_router(routes_auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(routes_predict.router, prefix="/predict", tags=["Prediction"])

# monitoring with Prometheus
Instrumentator().instrument(app).expose(app)

# Register custom exception handlers
register_exception_handlers(app)
