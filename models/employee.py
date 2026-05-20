# class Employee:
# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_details(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Salary: {self.salary}")


# ENCAPSULATION
class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

emp = Employee("John", 50000)

print(emp.get_salary())