employees = []


def get_all_employees(min_salary=0):

    filtered_employees = [
        employee
        for employee in employees
        if employee["salary"] >= min_salary
    ]

    return filtered_employees


def create_employee_service(employee):

    employees.append(employee.dict())

    return employee


def update_employee_service(employee_id, updated_employee):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees[index] = updated_employee.dict()

            return updated_employee

    return None


def delete_employee_service(employee_id):

    for index, employee in enumerate(employees):

        if employee["id"] == employee_id:

            employees.pop(index)

            return True

    return False