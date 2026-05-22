from models.employee import Employee
# INHERITANCE
# class Developer(Employee):

#     def __init__(self, name, salary, programming_language):

#         super().__init__(name, salary)

#         self.programming_language = programming_language

#     def show_developer_details(self):

#         print(f"Name: {self.name}")
#         print(f"Salary: {self.salary}")
#         print(f"Language: {self.programming_language}")

# POLYMORPHISM
class Developer(Employee):

    def display_role(self):
        print("I am a Developer")