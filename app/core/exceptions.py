from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": str(exc)},
        )
