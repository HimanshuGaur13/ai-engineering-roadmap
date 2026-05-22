from fastapi import APIRouter
from models.employee_model import Employee
from services.employee_service import employees

router = APIRouter()


@router.get("/list-employees")
def get_employees():

    return employees


@router.post("/add-employees")
def create_employee(employee: Employee):

    employees.append(employee.dict())

    return {
        "message": "Employee created successfully",
        "data": employee
    }

@router.put("/update-employees/{employee_id}")
def update_employee(employee_id: int, updated_employee: Employee):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees[index] = updated_employee.dict()

            return {
                "message": "Employee updated successfully"
            }

    return {
        "message": "Employee not found"
    }

@router.delete("/delete-employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees.pop(index)

            return {
                "message": "Employee deleted successfully"
            }

    return {
        "message": "Employee not found"
    }