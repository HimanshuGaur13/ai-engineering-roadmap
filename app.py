import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


 #------------- Read CSV File
df = pd.read_csv("data/employees.csv")
# Show full data
print("Employee Data")
print(df)
# Highest salary
highest_salary = df["Salary"].max()
print("\nHighest Salary:", highest_salary)

# #Lowest salary
# lowest_salary = df["Salary"].min()
# print("\nLowest Salary:", lowest_salary)

# # Average salary
# average_salary = df["Salary"].mean()
# print("Average Salary:", average_salary)

# Highest salary employee
highest_employee = df[df["Salary"] == highest_salary]
print("\nEmployee with Highest Salary")
print(highest_employee)

# data = {
#     "name": ["A", "B", "C"],
#     "salary": [30000, 50000, 70000]
# }
# df = pd.DataFrame(data)
# df = pd.read_csv("employees.csv")
# print(df)
# print(df.head())          #---Shows first 5 rows.
# print(df.tail())          #---Shows last rows.
# print(df.info())          #---Shows column info.
# print(df["Name"])
# high_salary=df[df["Salary"]>50000]
# print(high_salary)
# print(df.isnull().sum())



# arr=[1,2,3,4]
# print(arr)
# numpy_arr = np.array([1,2,3,4])
# print(arr)
# print(numpy_arr.mean())
# print(numpy_arr.max())
# print(numpy_arr.min())
# df = pd.read_csv("employees.csv")
# print(df)
# print(df.head())
# print(df["Salary"].mean())
# print(df["Salary"].max())
# print(df["Salary"].min())

# df.to_csv("cleaned.csv", index=False)  #---Saves the DataFrame to a new CSV file without the index.

# x = [1,2,3,4,5]
# y = [10,20,30,40,50]

# plt.plot(x, y)

# plt.savefig("graph.png")
# print("Graph saved")
# employees = ["A", "B", "C"]
# salary = [30000, 50000, 70000]

# plt.bar(employees, salary)

# plt.show()
# labels = ["HR", "IT", "Sales"]
# sizes = [20, 50, 30]

# plt.pie(sizes, labels=labels)

# plt.show()

# salary = [30000,35000,40000,50000,70000,80000]

# plt.hist(salary)

# plt.show()
# data = {
#     "employee": ["A", "B", "C"],
#     "salary": [30000, 50000, 70000]
# }

# df = pd.DataFrame(data)

# plt.bar(df["employee"], df["salary"])

# plt.title("Salary Analysis")
# plt.xlabel("Employee")
# plt.ylabel("Salary")

# plt.show()