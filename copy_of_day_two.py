# -*- coding: utf-8 -*-
"""Copy of day_two.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bIiPT8hhAfWyRXwEXxKWWOc3vsWyVNKf

# Day Two: Understanding and Visualising Data
When you first start to analyse a dataset, you will not always know all the details about how it was collected and why it has been formatted in the way it is.

Therefore, to understand these aspects, you must conduct some basic statistical analysis. You will also begin to visualise data, which is a useful way for you to get an idea of how to interpret it.
"""

#First we must start by importing the pandas library 
#Also must import the matplot lib library which allows us to be able to visualise the data 
import pandas as pd 
from matplotlib import pyplot as plt


# Uncomment if you want to run off your machine - without internet connection 
#data = pd.read_csv('Data/titanic.csv')

#This one can only be run with an internet connection 
data = pd.read_csv('https://raw.githubusercontent.com/chroadhouse/Futureme/main/Data/titanic.csv')

#Run this code to make sure the data is read into the file 
data.head()

"""# Creating our own table: Running metrics on data
Even though you can run the .describe() function that returns a table with all the metric data you would want, it is still useful to be able to do this ourselves. 

Did you see above where we wrapped the link to our dataset in brackets? 

We then **assigned** it to a variable called *'data'* using **=**. This **stores** the dataset for us (have another look at yesterday's notebook if you need a recap on variables).

We can then single out one column of this dataset by calling this variable and inserting the name of the column we want inside square brackets **[ ]**.
"""

#data['Age'] will only return the rows for the age column 
age_mean = data['Age'].mean()
age_mode = data['Age'].mode()
age_median = data['Age'].median()
age_max = data['Age'].max()
age_min = data['Age'].min()
age_stand = data['Age'].std()

#Here we create a dictionary - the *keys* are the titles of columns and the *values* are the variables we created above
age_table = pd.DataFrame({
    'Mean':age_mean,
    'Mode':age_mode,
    'Median':age_median,
    'Maximum':age_max,
    'Minumum':age_min,
    'Standard Deviation':age_stand
})

age_table

#We can also do this with another quantitative column, such as Fare.
fare_mean = data['Fare'].mean()
fare_mode = data['Fare'].mode()
fare_median = data['Fare'].median()
fare_max = data['Fare'].max()
fare_min = data['Fare'].min()
fare_stand = data['Fare'].std()


age_table = pd.DataFrame({
    'Mean':fare_mean,
    'Mode':fare_mode,
    'Median':fare_median,
    'Maximum':fare_max,
    'Minumum':fare_min,
    'Standard Deviation':fare_stand
})

age_table

"""# Checking the Frequency of Categorical data
Data is more than just numbers.
 One of the best things you can do when looking at data such as categorical data is looking at the frequency of each of the values 
"""

#Value_count method returns the freqency of each category
embark_data = data['Embarked'].value_counts()

embark_data

#Replacing the characters with strings
data['Embarked']= data['Embarked'].replace({'S':"Southhampton", 'C':'Cherbourg', 'Q':'Queenstown'})

#Storing the count and percentage to show in a table
c = data.Embarked.value_counts()
p = data.Embarked.value_counts(normalize=True).mul(100).round(1).astype(str)
value_count = pd.concat([c,p], axis=1, keys=['counts', '%'])

value_count

"""# Plotting Data 
Plotting data is one of the best ways to get a grasp of what the data is telling and showing us. 

To plot data in python we use the matplotlib library which makes plotting data very easy. When importing the library it is common practice to give it then name of plt

The Documentation can be found here for this module: https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html

# Histograms
Like a bar chart that represents data in buckets of ranges of classes along a horizontal axis.
"""

#We create a histogram to show the age of passengers on the Titanic
plt.hist(data['Age'])
plt.xlabel('Age of passenger')
plt.ylabel('Number of passengers')
plt.title('Histogram of Passenger Age')
plt.show()

#Creating histograms for the number of people that didn't survive and did survive baded on the fare they paid
not_survived_fare = data['Fare'][data['Survived']=='Not Survive']
survived_fare = data['Fare'][data['Survived']=='Survived']
plt.figure(figsize=(12,6))
plt.subplot(121)
not_survived_fare.plot(kind='hist',title = 'People who didn\'t survive')


plt.subplot(122)
survived_fare.plot(kind='hist', title= 'People who survived')

"""# Pie Charts
A chart that is a chart where sections are divided up into slices to illustrate the numerical value. It is best used for showing percentages

"""

#A pie chart to show the percentage of males to females on the ship
plt.figure(figsize=(10,10))
data.Sex.value_counts().plot(kind='pie', title='Pie chart to show the number of males and females', autopct='%d%%')

#Creating two pie charts to show the people that did an didn't survive based on where they got on the ship
not_survived_class = data['Pclass'][data['Survived']=='Not Survive']
survived_class = data['Pclass'][data['Survived']=='Survived']

plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
not_survived_class.value_counts().plot(kind='pie', title='people who didn\'t survived', autopct='%d%%')

plt.subplot(1,2,2)
survived_class.value_counts().plot(kind='pie', title='people who survived', autopct='%d%%')

"""# Bar Charts
Represents Categroical Data
"""

#The groupby method
plt.figure(figsize=(10,10))
data.groupby('Sex').Survived.value_counts().plot(kind='bar')
plt.title('Bar Chart to show the number of males and females that survived and did not survive')
plt.xlabel('Numer of males and females that survived')
plt.ylabel('Number of passengers')

"""## Bar Chart to understand our data
One of the things that should be checked when working with data is looking at what values are missing. 
* .isna() - is a method that will tell you you how many NaN's there are, which stands for Not a Number (means blank). 

Day 3 Notebook will look at this in more detail 
"""

#Shows us how much data we have for each column in the not-null count section
data.info()

#The isna() method will return whether or not the data is NaN
data.isna()

#By running the sum method on this data, it will give us the total of NaN's in the dataset
data.isna().sum()

#The ~ is the character that inverses the isna() method - Meaning the number of values that are present will be shown
fullData = ~data.isna()

#Customizing the chart we are going to create
plt.figure(figsize=(10,10))
plt.xlabel('Columns')
plt.ylabel('Number of data')
plt.title('Bar chart to show the number of valid data in each column')

#Here we actually create the barchart
fullData.sum().plot(kind='bar')

#This is bar chart shows the data that is valid - we can see this sort of data in the .info() but this is a more graphical representation