import pandas as pd

# reading csv file
df = pd.read_csv("people_data.csv")
print(df)

df = pd.read_csv("people_data.csv", usecols=["First Name", "Email"])
print(df)

'''Setting an Index Column (index_col)
The index_col parameter sets one or more columns as the DataFrame index, making the specified column(s) act as row labels for easier data referencing.'''

df = pd.read_csv("people_data.csv", index_col="First Name")
print(df)



