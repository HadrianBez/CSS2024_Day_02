# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:48:11 2024

@author: HadrianBezuidenhout
"""

import pandas as pd
# Extract
############################################################################################
df = pd.read_csv("data_02/country_data_index.csv")

# Absolute Path
# C:\Users\HadrianBezuidenhout\Python Projects\CSS_2024_Day_02\CSS_Day_02\data_02
# Relative Path
# data_02/country_data_index.csv

# To import data from a URL
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data") 
# To add column names when importing
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)
# For text files specify the delimiter ";"
df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")
# For Excel files
df = pd.read_excel("data_02/residentdoctors.xlsx")
# For Json
df = pd.read_json("data_02/student_data.json")
############################################################################################

# Transform
############################################################################################
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.readcsv.html # Read_csv parameters

# to remove "Unamed:0" column from file, specify the index column
df = pd.read_csv("data_02/country_data_index.csv",index_col=0)

# Skip Rows - first rows contain titles that are not formatted correctly, these are skipped
df = pd.read_csv("data_02/insurance_data.csv",skiprows=5)

# Column Names - Adds titles to data
column_names = ["duration", "pulse", "max_pulse", "calories"]
df = pd.read_csv("data_02/patient_data.csv", header=None, names=column_names)

# Uniques Delimiter - Specifies formatting for text file
df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

###############################################################################
# Inconsistent Data Types & Names
df = pd.read_excel("data_02/residentdoctors.xlsx")
# Step 1: Extract the lower end of the age range (digits only)
df['LOWER_AGE'] = df['AGEDIST'].str.extract('(\d+)-') # Pseudo-code: 1. Search for a number followed by a hyphen like "30-" 2. If you find that number, extract the number and ignore the hyphen 3. Put it in a new column called LOWER_AGE
# Regular expressions (regex or regexp) are sequences of characters that define a search pattern
# Step 2: Convert the new column to float
df['LOWER_AGE'] = df['LOWER_AGE'].astype(float)
# .str, .extract(), and .astype() are all functions or methods that can be applied to a pandas Series object or single column of text data.
# .extract() to extract information from a string. Other string methods:-.upper() makes string/text upper case - .lower() makes string/text lower case - .replace() replaces certain characters

###############################################################################
# Working with dates
df = pd.read_csv("data_02/time_series_data.csv") # Promblem: date is 2020-01-10, however in the US, the day is the middle number and in UK and in most local countries here the middle number is the month 
# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
# To specify date format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y') # %d: day %m: month %Y: year

# Second Option: # Split the 'Date' column into separate columns for year, month, and day
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
###############################################################################

# NANs and Wrong Formats
df = pd.read_csv('data_02/patient_data_dates.csv')

# Allows you to see all rows
pd.set_option('display.max_rows',None)
#print(df)
# Remove redundant index column
df.drop(['Index'],inplace=True,axis=1)
# Replace Empty Values - Using fillna
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
#  inplace=True, it means that the changes made by the fillna operation will be applied directly to the original DataFrame 

# Wrong Date Format – Convert with to_datetime()
# ‘Date’ column should be a string that represents a date.
df['Date'] = pd.to_datetime(df['Date'],format="mixed")

# removing the entire row using 
df.dropna(inplace = True)
# only want to remove rows in that Date column you use df.dropna(subset=['Date'], inplace = True)

# Removing Empty Cells – Using dropna
df.dropna(inplace = True)
df = df.reset_index(drop=True)

# Replacing specific data value
df.loc[7, 'Duration'] = 45
# remove that row completely using df.drop(7, inplace = True)

# Removing Duplicates – Using drop_duplicates()
df.drop_duplicates(inplace = True)


##################################################################
# Applying Data Transformations
############################################################
df = pd.read_csv('data_02/iris.csv')
df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)
grouped = df.groupby('class') # Groups data for processing

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length_sq'].mean()
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Display the results
print("Mean of Sepal Length Squared:")
print(mean_squared_values)

print("\nSum of Sepal Length Squared:")
print(sum_squared_values)

print("\nCount of Sepal Length Squared:")
print(count_squared_values)
##################################################################
# Append & Merge
##################################################################
# Appending two data sets together that have the same column names
# Read the CSV files into dataframes
df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")
# Concatenate the dataframes
df = pd.concat([df1, df2], ignore_index=True) 

# Merging related data using common column
df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')
# inner join by default (only related data included)
df_merge = pd.merge(df1,df2,on='id') 
# returns all the rows from both dataframes, unrelated values return NaN
df_merge = pd.merge(df1, df2, on='id', how='outer')

##################################################################
#Filtering Data
##################################################################
# Filtering data
#print(df[df['age'] > 30])

df = pd.read_csv("data_02/iris.csv")
# Filter data for females (class == 'Iris-versicolor')
iris_versicolor = df[df['class'] == 'Iris-versicolor']

# Calculate the average iris_versicolor_sep_length
avg_iris_versicolor_sep_length = iris_versicolor['sepal_length'].mean()

# Better way to label "class" column
df['class'] = df['class'].str.replace('Iris-', '')

# To apply function to each element
# Apply the square to sepal length using a lambda function
df['sepal_length_sq'] = df['sepal_length'].apply(lambda x: x**2)

################################################################
# Load
################################################################

# After editing data we must export it (here into a new folder)

# CSV
#df.to_csv("data_02/output/iris_data_cleaned.csv")
#df.to_csv("data_02/output/iris_data_cleaned.csv", index=False) # Removes pandas index column

# Excel
#df.to_excel("data_02/output/iris_data_cleaned.xlsx", index=False, sheet_name='Sheet1')

# JSON
#df.to_json("data_02/output/iris_data_cleaned.json", orient='records')
# JSON format, there isn't a concept of a DataFrame index like in tabular data. The orient='records' argument specifies that the JSON file should be structured as a list of records, and the DataFrame index is not considered.






# COMMON THINGS TO LOOK FOR in SPREADSHEET

# 1. Not filling in zeros - different to blank, a zero is actual data that was measured
# 2. Null Values - different to zero, null was not measured and thus should be ignored
# 3. Formatting to make data sheet pretty - highlighting and similar - add a new column instead with info
# 4. Comments in cells - place in separate column
# 5. Entering more than one piece of information in a cell - only one piece of information per cell
# 6. Using problematic field names - avoid spaces, numbers, and special characeters
# 7. Using special characters in data - avoid in your data


