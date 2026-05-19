import pandas as pd
df=pd.read_csv("cleaned.csv")
print("Average Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
salary=df["Salary"]>50000
print(df[salary])