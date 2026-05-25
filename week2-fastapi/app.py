from fastapi import FastAPI

from database.connection import engine

from database.models import Base

from routes.auth_routes import router as auth_router

from routes.employee_routes import (
    router as employee_router
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)

app.include_router(employee_router)


@app.get("/")
def home():

    return {
        "message": "Backend Running"
    }