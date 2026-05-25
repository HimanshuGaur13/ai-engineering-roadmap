from database.models import EmployeeDB


def get_all_employees(db, min_salary=0):

    return db.query(EmployeeDB).filter(
        EmployeeDB.salary >= min_salary
    ).all()


def create_employee_service(employee, db):
    db_employee = EmployeeDB(
        name=employee.name,
        salary=employee.salary,
        designation=employee.designation
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee_service(
    employee_id,
    updated_employee,
    db
):
    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()
    if not employee:
        return None
    employee.name = updated_employee.name
    employee.salary = updated_employee.salary
    employee.designation = updated_employee.designation
    db.commit()
    db.refresh(employee)
    return employee


def delete_employee_service(employee_id, db):
    employee = db.query(EmployeeDB).filter(
        EmployeeDB.id == employee_id
    ).first()
    if not employee:
        return False
    db.delete(employee)
    db.commit()
    return True