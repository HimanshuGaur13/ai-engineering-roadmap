def generate_salary_report(data):

    average_salary = data["Salary"].mean()
    max_salary = data["Salary"].max()
    min_salary = data["Salary"].min()

    report = f"""
    Salary Report
    ----------------
    Average Salary: {average_salary}
    Maximum Salary: {max_salary}
    Minimum Salary: {min_salary}
    """

    return report