import pandas as pd

df = pd.read_csv('data.csv')
print(f"Средняя зарплата сотрудников: {df['Salary'].mean()}")
print("Сотрудники старше 30 лет:")
print(df[df['Age'] >30])