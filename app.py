from utils.calculator import add
from utils.validators import is_positive
from utils.logger import log_message
from models.employee import Employee
from models.developer import Developer
from models.manager import Manager
# Calculator functions
# result = add(10, 5)
# print(result)
# print(is_positive(result))
# log_message("Application started")

# CLASS & OBJECT
# emp1 = Employee("John", 50000, "python")
# emp1.display_details()

# INHERITANCE
# empNew=Developer("Alice", 70000, "Python")
# empNew.show_developer_details()

# ENCAPSULATION
emp = Employee("John", 50000)
print(emp.get_salary())

# manager = Manager("John", 80000)
# developer = Developer("Alex", 90000, "Python")

# manager.display_role()
# developer.display_role()