def clean_salary_column(data):

    data["Salary"] = data["Salary"].fillna(0)

    return data