from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from database.connection import get_db

from schemas.employee_schema import Employee
from schemas.response_schema import EmployeeResponse

from services.employee_service import (
    get_all_employees,
    create_employee_service,
    update_employee_service,
    delete_employee_service
)

router = APIRouter()


@router.get("/employees")
def get_employees(
    min_salary: float = 0,
    db: Session = Depends(get_db)
):

    return get_all_employees(db, min_salary)


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def create_employee(
    employee: Employee,
    db: Session = Depends(get_db)
):

    created_employee = create_employee_service(
        employee,
        db
    )

    return {
        "message": "Employee created successfully",
        "data": {
            "id": created_employee.id,
            "name": created_employee.name,
            "salary": created_employee.salary,
            "designation": created_employee.designation        
        }
    }


@router.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated_employee: Employee,
    db: Session = Depends(get_db)
):

    employee = update_employee_service(
        employee_id,
        updated_employee,
        db
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee updated successfully",
        "data": {
            "id": employee.id,
            "name": employee.name,
            "salary": employee.salary,
            "designation": employee.designation
        }
    }


@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_employee_service(
        employee_id,
        db
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }