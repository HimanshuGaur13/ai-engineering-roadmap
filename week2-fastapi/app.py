from fastapi import FastAPI, Depends

from routes.employee_routes import router as employee_router

app = FastAPI(
    title="Employee Management API",
    version="1.0.0"
)


# Dependency Injection Example
def common_parameters():

    return {
        "app_name": "Employee Management System",
        "version": "v1"
    }


@app.get("/")
def home(params: dict = Depends(common_parameters)):

    return {
        "message": "Employee API Running",
        "app_info": params
    }


# Include Employee Routes
app.include_router(employee_router)