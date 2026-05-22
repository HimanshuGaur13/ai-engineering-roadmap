from fastapi import APIRouter, HTTPException

from models.employee_model import Employee
from models.response_modal import EmployeeResponse


from services.employee_service import (
    get_all_employees,
    create_employee_service,
    update_employee_service,
    delete_employee_service
)

router = APIRouter()


@router.get("/employees")
def get_employees(min_salary: float = 0):

    return get_all_employees(min_salary)


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def create_employee(employee: Employee):

    created_employee = create_employee_service(employee)

    return {
        "message": "Employee created successfully",
        "data": created_employee.dict()
    }


@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    employee = update_employee_service(
        employee_id,
        updated_employee
    )

    if not employee:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee updated successfully",
        "data": employee.dict()
    }


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    deleted = delete_employee_service(employee_id)

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "message": "Employee deleted successfully"
    }