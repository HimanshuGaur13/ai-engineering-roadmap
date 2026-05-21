import pandas as pd
from utils.logger import log_info, log_error
from utils.custom_exceptions import InvalidSalaryError

def analyze_salary(file_path):
    try:
        log_info("Salary analysis started")

        data = pd.read_csv(file_path)
        print(data.head())

        if data["Salary"].min() < 0:
            raise InvalidSalaryError("Negative salary found")
        average_salary = data["Salary"].mean()
        print(f"Average Salary: {average_salary}")

        log_info("Salary analysis completed")

    except FileNotFoundError:
        print("CSV file not found")
        log_error("CSV file not found")

    except InvalidSalaryError as error:
        print(error)
        log_error(error)

    except Exception as error:
        print(error)
        log_error(f"Unexpected error: {error}")

    finally:
        log_info("Program execution completed")
      