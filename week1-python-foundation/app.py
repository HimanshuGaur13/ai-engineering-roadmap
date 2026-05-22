# from utils.calculator import add
# from utils.json_handler import read_json
# from utils.validators import is_positive
# from config import ENVIRONMENT
# print(ENVIRONMENT)
# from utils.logger import log_message
# from models.employee import Employee
# from models.developer import Developer
# from models.manager import Manager
# from salary_analyzer import analyze_salary
# analyze_salary(" data/employees.csv")

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
# emp = Employee("John", 50000)
# print(emp.get_salary())

# manager = Manager("John", 80000)
# developer = Developer("Alex", 90000, "Python")

# manager.display_role()
# developer.display_role()



# from utils.csv_handler import load_csv
# from utils.data_cleaner import clean_salary_column
# data = load_csv("data/employees.csv")
# # print(data.head())
# cleaned_data = clean_salary_column(data)
# print(cleaned_data)

# from utils.json_handler import write_json, read_json
# from utils.report_generator import generate_salary_report
# employee = {
#     "Name": "John",
#     "Salary": 50000
# }

# with open("data/employee_report.json", "w") as file:   #Use "with" Automatically closes file.
#     file.write('{"Name": "John", "Salary": 50000}')
# # write_json(employee, "data/employee.json")

# data = read_json("data/employee.json")

# print(data)

# report = generate_salary_report(data)

# print(report)


# from utils.file_handler import load_csv
# from utils.data_cleaner import clean_salary_column
# from utils.report_generator import generate_salary_report

# data = load_csv("data/employees.csv")
# cleaned_data = clean_salary_column(data)
# report = generate_salary_report(cleaned_data)

# print(report)
import argparse
from utils.file_handler import load_csv
from utils.data_cleaner import clean_salary_column
from utils.report_generator import generate_salary_report
from utils.json_handler import write_json
from utils.logger import log_info, log_error
from utils.custom_exceptions import InvalidSalaryError

from config import Config

# -For dynmic input from command line, we can use argparse. Uncomment the below code to enable it.
# parser = argparse.ArgumentParser()

# parser.add_argument(
#     "--input",
#     required=True,
#     help="Path to employee CSV file"
# )
# args = parser.parse_args()
def main():

    try:

        log_info("Application started")

        print(Config.APP_NAME)

        data = load_csv("data/employees.csv")
        # data = load_csv(args.input)

        cleaned_data = clean_salary_column(data)

        if cleaned_data["Salary"].min() < 0:

            raise InvalidSalaryError("Negative salary found")

        report = generate_salary_report(cleaned_data)

        print(report)

        write_json(report, "data/employee_report.json")

        log_info("Report generated successfully")

    except InvalidSalaryError as error:

        print(error)

        log_error(error)

    except Exception as error:

        print(error)

        log_error(f"Unexpected error: {error}")

    finally:

        log_info("Application execution completed")


if __name__ == "__main__":

    main()
