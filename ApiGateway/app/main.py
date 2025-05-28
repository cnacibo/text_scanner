# ApiGateway/app/main.py
from fastapi import FastAPI
from app.api.routers import router
from app.api.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

app = FastAPI()
app.include_router(router)

app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

