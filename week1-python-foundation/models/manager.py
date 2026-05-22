from models.employee import Employee

class Manager(Employee):

    def display_role(self):
        print("I am a Manager")