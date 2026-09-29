# pandas - py lib used to working with structured/tabular data 
# it make easier to read, clean, transform, analyse or write the data 

import pandas as pd

# 1. Series
s = pd.Series([1, 2, 3, 4]) 

# 2. DataFrame
df = pd.DataFrame({       # this how we create dataframe
    "name": ["a", "b", "c"],
    "salary": [5000, 7000, 8000]
})

# 3. Index / Columns
# ----------------
# df.index
import pandas as pd
df = pd.DataFrame({
    "name": ["a", "b", "c"],
    "salary": [5000, 7000, 8000]
})#, index=["a", "b", "c"])
print(df)
print(df.index)
print(df.columns) # call for columns name

# 4. loc / iloc
# -----------------
# df.loc[0]              # by label
# df.iloc[0]             # by position
# df.loc[0, "salary"]    # specific value 


print(df.loc[0]) 
print(df.iloc[0])
print(df.loc[0, "salary"])


# 5. Read data
pd.read_csv("data.csv")
pd.read_excel("data.xlsx")
pd.read_json("data.json")

import pandas as pd
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")
df = pd.read_json("data.json")
print(df)
# 6. Write data
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")

import pandas as pd
df = pd.DataFrame({
    "name": ["a", "b", "c"],
    "salary": [5000, 7000, 8000]
})
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")



# 7. Inspect data
df.head()              # first rows
df.tail()              # last rows
df.shape               # rows, columns (2, 3)
df.columns             # column names
df.dtypes              # data types
df.info()              # structure + nulls
df.describe()          # statistics 

import pandas as pd
df = pd.DataFrame({
    "name": ["a", "b", "c"],
    "salary": [5000, 7000, 8000]
})
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe()) 

# 8. Select columns
df["salary"]                    # one column
df[["name", "salary"]]          # multiple columns

# 9. Filter rows
df[df["salary"] > 50000]

# Multiple conditions
# used for filtering rows with multiple conditions
# or = |
# and = &
df[(df["salary"] > 5000) & (df["name"] == "a")]
df[(df["salary"] > 5000) | (df["name"] == "a")] 


# Filter + select
df.loc[df["salary"] > 50000, ["name", "salary"]]


# ---------

# Adding / Modifying Columns
# Create a new column or change an existing column

import pandas as pd
df = pd.DataFrame({
    "name": ["a", "b", "c"],
    "salary": [5000, 7000, 8000]
})
# Add a new column
df["bonus"] = [500, 700, 800]
print(df)
# Create a column from another column
df["annual_salary"] = df["salary"] * 12
print(df)
# Modify an existing column
df["salary"] = df["salary"] + 1000
print(df)
# Create a column using a condition
df["status"] = df["salary"] > 6000

# --------

# Missing Data / NULL values
df.isnull()          # find missing values
df.isnull().sum()    # count missing values

df.dropna()          # remove rows with NULL

df.fillna(0)         # replace NULL with 0
df.fillna("Unknown") # replace NULL with text


import pandas as pd
df = pd.DataFrame({
    'name': ['Steven King', 'Neena Yang', 'Lex Garcia', 'Alexander James', None, 'David Williams', 'Valli Jackson', 'Diana Nguyen', 'Nancy Gruenberg', 'Daniel Faviet', 'John Chen'],
    'job_id': ['AD_PRES', 'AD_VP', 'AD_VP', 'IT_PROG', 'IT_PROG', None, 'IT_PROG', 'IT_PROG', 'FI_MGR', 'FI_ACCOUNT', None],
    'salary': [24000, 17000, 17000, 9000, 6000, 4800, None, 4200, 12008, 9000, 8200],
    'commission_pct': [0.40, 0.30, None, None, 0.15, None, 0.10, None, None, 0.20, None],
    'department_id': [90, 90, 90, 60, 60, 60, None, 60, 100, None, 100],
    'hire_date': ['2013-06-17', '2015-09-21', None, '2016-01-03', '2017-05-21', '2015-06-25', '2016-02-05', None, '2012-08-17', '2012-08-16', '2015-09-28']
})

display(df) # Display the dataframe

display(df.isnull()) # Check missing values / Gives True/False
display(df.isnull().sum()) # Check missing values / Gives count

# dropna() - Remove missing rows / Removes rows containing missing values
display(df.dropna()) # Remove missing rows

# fillna() - Instead of deleting the row, you can fill the missing value
df["department_id"] = df["department_id"].fillna("Unknown")
display(df)

df["salary"] = df["salary"].fillna(0)
display(df)

# Instead of deleting the row, you can fill the missing value.
df["commission_pct"] = df["commission_pct"].fillna(0)
display(df)

# ---------------

# sorting

# ascending=True     # smallest → largest
# ascending=False    # largest → smallest

# # Ascending
# df.sort_values("salary")

# # Descending
# df.sort_values("salary", ascending=False)

# # Multiple columns
# df.sort_values(["department", "salary"])

# # Different order
# df.sort_values(
#     ["department", "salary"],
#     ascending=[True, False]
# )

import pandas as pd
df = pd.DataFrame({
    'name': ['Steven King', 'Neena Yang', 'Lex Garcia', 'Alexander James', None, 'David Williams', 'Valli Jackson', 'Diana Nguyen', 'Nancy Gruenberg', 'Daniel Faviet', 'John Chen'],
    'job_id': ['AD_PRES', 'AD_VP', 'AD_VP', 'IT_PROG', 'IT_PROG', None, 'IT_PROG', 'IT_PROG', 'FI_MGR', 'FI_ACCOUNT', None],
    'salary': [24000, 17000, 17000, 9000, 6000, 4800, None, 4200, 12008, 9000, 8200],
    'commission_pct': [0.40, 0.30, None, None, 0.15, None, 0.10, None, None, 0.20, None],
    'department_id': [90, 90, 90, 60, 60, 60, None, 60, 100, None, 100],
    'hire_date': ['2013-06-17', '2015-09-21', None, '2016-01-03', '2017-05-21', '2015-06-25', '2016-02-05', None, '2012-08-17', '2012-08-16', '2015-09-28']
})
# display(df)

# print(df.sort_values("salary")) # By default, it sorts ascending
# print(df.sort_values("salary", ascending=False)) # Descending order
# print(df.sort_values(["department_id", "salary"])) # Multiple columns
print(df.sort_values(["department_id", "salary"], ascending=[True, False])) # Different order

# ------------

# groupby() is the pandas version of sql's GROUPBY

# groupby() → "How do I divide the data into groups?"
# agg()     → "What calculations do I want for each group?"

# Pandas                         SQL

# groupby()                  →   GROUP BY
# mean()                     →   AVG()
# sum()                      →   SUM()
# count()                    →   COUNT()
# min()                      →   MIN()
# max()                      →   MAX()

import pandas as pd

df = pd.DataFrame({
    "name": ["a", "b", "c", "d", "e"],
    "department": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [5000, 6000, 7000, 8000, 9000]
})

# Suppose you want Average salary for each department
print(df.groupby("department")["salary"].mean())
print(df.groupby("department")["salary"].sum())
print(df.groupby("department")["salary"].min())
print(df.groupby("department")["salary"].max())
# You can simply group '''df.groupby("department")''' But this doesn't give you a useful final result by itself
# Usually you combine groupby() with an aggregation.

# agg() - aggregation
# # Multiple calculations on one column
# df["salary"].agg(["sum", "mean", "min", "max"])

# # Multiple calculations after grouping
# df.groupby("department")["salary"].agg(
#     ["sum", "mean", "min", "max"]
# )

# # Different calculations for different columns
# df.groupby("department").agg({
#     "salary": ["sum", "mean"],
#     "name": "count"
# })

# Multiple aggregations
# can also do multiple aggregation at once
print(df.groupby("department")["salary"].agg(
    ["count", "sum", "mean", "min", "max"]
))

# Group by multiple columns
print(df.groupby(["department", "name"])["salary"].sum())

# agg() with groupby()
# This is where it becomes really useful.

df.groupby("department")["salary"].agg(
    ["sum", "mean", "min", "max"]
)

# Output:
#             sum    mean   min   max
# department
# HR        14000  7000.0  6000  8000
# IT        12000  6000.0  5000  7000

# Different aggregation for different columns
df.groupby("department").agg({
    "salary": ["sum", "mean"],
    "name": "count"
})

# ------------------

# Duplicates in Pandas is about finding and removing repeated rows

import pandas as pd

df = pd.DataFrame({
    "name": ["a", "b", "b", "c", "c"],
    "salary": [5000, 6000, 6000, 7000, 7000]
})

# Find duplicates → df.duplicated()
print(df.duplicated())

# in output 
# 0    False
# 1    False
# 2     True
# 3    False
# 4     True

# False → first occurrence
# True  → duplicate occurrence

# to count the total no of duplicates
print(df.duplicated().sum())

# Remove duplicates → drop_duplicates()
print(df.drop_duplicates()) # keeps the first occurrence and removes the repeated ones.

# Duplicate based on specific column
print(df.duplicated(subset=["name"]))

# Remove based on specific column
print(df.drop_duplicates(subset=["name"]))

# Keep last duplicate
print(df.drop_duplicates(keep="last"))

# Remove all duplicated records
print(df.drop_duplicates(keep=False))

# -------------------

# String Operations in Pandas
# String operations are used when a column contains text and you need to clean or transform it

# f["name"].str.upper()       # uppercase
# df["name"].str.lower()       # lowercase
# df["name"].str.strip()       # remove spaces
# df["name"].str.contains("a") # search text
# df["name"].str.replace("a", "x") # replace
# df["name"].str.len()         # length

import pandas as pd

df = pd.DataFrame({
    "name": [" alice ", "BOB", " Charlie "],
    "city": ["chennai", "CHENNAI", "Bangalore"]
})

# print(df["name"].str.upper()) #Convert text to uppercase
# print(df["name"].str.lower()) #Convert text to lowercase
# print(df["name"].str.strip()) #Remove leading and trailing spaces
print(df["city"].str.contains("CHENNAI"))
print(df["city"].str.replace("CHENNAI", "Chennai"))
print(df["city"].str.len())

# --------------

# Date/Time operations

# # Convert
# pd.to_datetime(df["date"])

# # Extract
# df["date"].dt.year
# df["date"].dt.month
# df["date"].dt.day
# df["date"].dt.day_name()
# df["date"].dt.month_name()

# # Filter
# df[df["date"] > "2024-01-01"]

# # Date difference
# df["date2"] - df["date1"]

# # Number of days
# (df["date2"] - df["date1"]).dt.days

# # Add/subtract
# df["date"] + pd.Timedelta(days=30)

# # Format
# df["date"].dt.strftime("%d-%m-%Y")
# Convert a date column into Pandas datetime → then extract or manipulate parts of the date

import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "joining_date": ["2024-01-15", "2023-06-20", "2025-03-10"]
})

print(df)
print(df.dtypes) # this will show the dtype as object 

# Convert to datetime - df[] = pd.to_datetime()
df["joining_date"] = pd.to_datetime(df["joining_date"])  # convberting the dtype to datetime
print(df)
print(df.dtypes)

# Extract year, month, day

df["year"] = df["joining_date"].dt.year
df["month"] = df["joining_date"].dt.month
df["day"] = df["joining_date"].dt.day
print(df)

# Other useful date parts
df["day_name"] = df["joining_date"].dt.day_name()
df["month_name"] = df["joining_date"].dt.month_name()
df["day_of_week"] = df["joining_date"].dt.dayofweek
df["day_of_year"] = df["joining_date"].dt.dayofyear
print(df)

# Add/subtract dates

df["after_30_days"] = df["joining_date"] + pd.Timedelta(days=30)
df["before_7_days"] = df["joining_date"] - pd.Timedelta(days=7)
print(df)

df["after_4_months"] = df["joining_date"] + pd.DateOffset(months=4)
df["before_2_years"] = df["joining_date"] - pd.DateOffset(years=2)
print(df)

# Filter using dates
df[df["joining_date"] > "2024-01-01"]
df[df["joining_date"].dt.year == 2024]
df[
    (df["joining_date"] >= "2024-01-01") &
    (df["joining_date"] <= "2024-12-31")
]

# Format dates as strings - .dt.strftime()
# %Y → 2024
# %m → 01
# %d → 15
df["formatted_date"] = df["joining_date"].dt.strftime("%m-%d-%Y")
print(df)

# -----------------

# Combining DataFrames: merge() and concat()

# merge() → similar to SQL JOIN / wokr like same like matching column name
# concat() → similar to stacking rows / UNION-like operation

# merge() -> join two dataframes suppose if we have

import pandas as pd
# two dataferames!
employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

salary = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "salary": [50000, 60000, 70000]
})
# merging them
df = pd.merge(employees, salary, on="emp_id")
print(df)

# suppsoe if we have no matching column or diff name then

employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["A", "B", "C"]
})

salary = pd.DataFrame({
    "employee_id": [1, 2, 3],
    "salary": [50000, 60000, 70000]
})

# we use like this
df = pd.merge(
    employees,
    salary,
    left_on="emp_id",
    right_on="employee_id"
)
print(df)


# differnt type of merge() -> similar to joins 
# merge()
# │
# ├── inner → INNER JOIN
# ├── left  → LEFT JOIN
# ├── right → RIGHT JOIN
# └── outer → FULL OUTER JOIN

import pandas as pd

employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5, 6],
    # "name": ["A", "B", "C"]
})

salary = pd.DataFrame({
    "emp_id": [1, 2, 3, 3, 4, 6],
    # "salary": [50000, 60000, 70000]
})

# inner -> Only matching records
pd.merge(
    employees,
    salary,
    on="emp_id",
    how="inner"
)


# left join
pd.merge(
    employees,
    salary,
    on="emp_id",
    how="left"
)

# right join
pd.merge(
    employees,
    salary,
    on="emp_id",
    how="right"
)

# outer join
pd.merge(
    employees,
    salary,
    on="emp_id",
    how="outer"
)

# concat() — Combine DataFrames
# imagine we have employees from two different sources

import pandas as pd
df1 = pd.DataFrame({
    "name": ["A", "B"],
    "salary": [50000, 60000]
})

df2 = pd.DataFrame({
    "name": ["C", "D"],
    "salary": [70000, 80000]
})

# We want:
# A
# B
# C
# D

# so we use 
df = pd.concat([df1, df2])
print(df)

# If you want a fresh index not like 0 1 0 1 since its from two df know! to avoid that we use
df = pd.concat([df1, df2], ignore_index=True)
print(df)

# concat can also combine columns
df1 = pd.DataFrame({
    "name": ["A", "B", "C"]
})

df2 = pd.DataFrame({
    "salary": [50000, 60000, 70000]
})

# axis tells Pandas which direction to combine.
# axis=0 → along rows / column-wise
# axis=1 → along columns / row-wise
df = pd.concat([df1, df2], axis=1)
print(df)

# -----------------------------

# apply() + lambda

# apply() = run a function on every value/row/column
# lambda = write a small function in one line

# apply() - with normal function
import pandas as pd

df = pd.DataFrame({
    "name": ["A", "B", "C"],
    "salary": [50000, 60000, 70000]
})

# i have a df 
# then i would create a normal function
def add_bonus(salary):
    return salary + 5000 # 

# then am applying it
df["new_salary"] = df["salary"].apply(add_bonus) #Take every value in salary and pass it to add_bonus()
print(df)

# lambda - small function
df["new_salary"] = df["salary"].apply(lambda x: x + 2000)
print(df)
# multiply
df["new_salary"] = df["salary"].apply(lambda x: x * 2)
print(df)
# add 10%
df["new_salary"] = df["salary"].apply(lambda x: x * 1.10)
print(df)
# convet into lowercase
df["name"] = df["name"].apply(lambda x: x.lower())
print(df)


# apply() - with conditons
df["level"] = df["salary"].apply(lambda x: "high" if x > 60000 else "low")
print(df)
# apply() - apply on a dataframe
def employee_info(row):
    return row["name"] + "-" + str(row["salary"])

df["info"] = df.apply(employee_info, axis=1)
print(df)