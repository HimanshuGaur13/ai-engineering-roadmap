import pandas as pd

def analyze_salary(file_path):

    data = pd.read_csv(file_path)

    average_salary = data["Salary"].mean()
    max_salary = data["Salary"].max()
    min_salary = data["Salary"].min()

    print(f"Average Salary: {average_salary}")
    print(f"Highest Salary: {max_salary}")
    print(f"Lowest Salary: {min_salary}")


analyze_salary("data/employees.csv")
from utils.logger import log_message

log_message("Salary analysis started")