import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)

# Displaying the DataFrame
print("Original DataFrame:")
print(df)

# Selecting a column
print("\nSelected column 'Name':")
print(df['Name'])

# Filtering rows
print("\nRows where Age > 25:")
print(df[df['Age'] > 25])

# Adding a new column
df['Salary'] = [60000, 80000, 70000]
print("\nDataFrame with added 'Salary' column:")
print(df)

# Grouping and aggregating data
grouped = df.groupby('City')['Salary'].mean()
print("\nAverage salary by city:")
print(grouped)