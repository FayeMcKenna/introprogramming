#load the libraries using the normal convention
#load the libraries using the normal convention
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
##prevent plotting errors
%matplotlib inline


##prevent plotting errors

#Load our excel files of interest into pandas
NHL_Goalies = pd.read_excel('NHLGoalies2016_2017.xls',na_values='',sheetname=0)
GAA_ = pd.read_excel('NHLGoalies2016_2017.xls',na_values='',sheetname='5vs5')

#Filtering the correct DF for Goalies that played 1 game (GP = Games played)
#Answer 1A:

#Get rid players other than ones that only played in 1 game and make new df NHL_Ones
print(NHL_Goalies['GP'])
NHL_Ones=NHL_Goalies[NHL_Goalies['GP'] == 1]
print(NHL_Ones['GP'])


#Find the value of the minimum Salary for the entire dataset
#Answer 1B: #575000.0
Min_Goalies=NHL_Goalies.groupby('Salary').min()
print(Min_Goalies.head())

#B. Replace the missing values from the NHL_Ones DF with this, # concatenate 'Salary' from 'Adjusted_Salary' to NHL_Ones
#Answer 1B:
#Answer 1B:
Adjusted_Salary=NHL_Ones
print(NHL_Ones['Salary'])
Adjusted_Salary['Salary'] = NHL_Ones['Salary'].replace(np.nan, 575000)
print(Adjusted_Salary['Salary'])

#C. Create a new DF after replacement by adding a column called "Adjusted_Salary" : didn't need this
#Combine_DF = pd.concat([NHL_Ones, Adjusted_Salary['Adjusted_Salary']], axis=1)
#print(Combine_DF['Salary'])
#print(Combine_DF['Adjusted_Salary'])




#D. I would like to only see the old "Salary" column and the "Adjusted Salary" column from the new Dataframe
new = NHL_Ones.filter(['Salary','Adjusted_Salary'], axis=1)
print(new)


# PART 2
#A. Subset the NHL goalies data to include Goalies that played in more than 25 games AND have a GAA lower than 3.00 and store the New DF as 'workhorse'

#Answer 2:
print(NHL_Goalies['GP'])
workhorse=NHL_Goalies[NHL_Goalies['GP'] > 25]
workhorse=NHL_Goalies[NHL_Goalies['GAA'] < 3.00]
print(workhorse['GP'])
print(workhorse['GAA'])

#PART 3
#Create 2 python functions that:Creates/Returns a new DataFrame that displays the number of missing values in every column.
#This new DataFrame has one new column named "Missing" with the sum of the missing values from the columns

#3A. Creates/Returns a new DataFrame that displays the number of missing values in every column.

#make new column missing and sum missing values of each row in new col

#Missing_Rows=NHL_Goalies
#Missing_Rows=Missing_Rows.assign(Missing = Series(np.random.randn(95), index=Missing_Rows.index))
#print(Missing_Rows)
 # need to add new row to sum 'New_Row'

#sum null

#Missing_Rows['Missing'] = Missing_Rows[NHL_Goalies.columns].isnull().sum(axis=0)
#print(Missing_Rows['Missing'])
 # need to add new row to sum 'New_Row'

#sum null

#B. Creates a new column called 'missing_values' in the input DF that sums the missing values in each row.
import pandas as pd
#sum null
Missing_Cols=NHL_Goalies
Missing_Cols=Missing_Cols.assign(Missing = Series(np.random.randn(95), index=Missing_Cols.index))
print(Missing_Cols)

Missing_Cols['Missing'] = Missing_Cols[NHL_Goalies.columns].isnull().sum(axis=1) # Need to put Null in so is not summing numbers
print(Missing_Cols['Missing'])


#Answer 4 here: pleae comment
#. Plot the histogram of the all the GAA of the NHL_Goalies DF AND the goalies that played in more than 25 games with a GAA < 3.00,
#B. Label the Titles of the plots differently (ie EntireSet + Subset)
#C. Change the color of one of the plots from the default

#make Subset of NHL_Goalies with Gp over 25 and GAA less than 3
NHL_plot=NHL_Goalies[NHL_Goalies['GP'] > 25]
NHL_plot=NHL_Goalies[NHL_Goalies['GAA'] < 3.00]


#from before
f = NHL_Goalies.GAA
f.plot(kind='bar')


my_list = NHL_Goalies["GAA"].tolist()

print(my_list)

import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
x = np.random.normal(size = 1000)
plt.hist(x, normed=True, bins=59)
plt.ylabel('my_list');

#Answer 5 here: please comments
# Subset the NHL_Goalies DataFrame where Injuries is not known (Injuries=NaN);
# Use a Merge with the GAA_ DF (workhorse) and Injuries is not known (Injuries=NaN) to produce a NEW DF (called mergedDF)
#USE A JOIN THAT PRESERVES ORDER AND USES THE INTERSECTION OF KEYS
#USE BOTH THE LEFT AND RIGHT INDEXES AS JOIN KEYS
#From the mergedDF keep FirstName/LastName/Team/Cntry/ SV% /GA/GAA/ TOI (note one copy for any duplicate column)
#GroupBy country on mergedDF and aggregate The Means, Mins, and Maximum of the kept columns
#Create a dataframe of the TOI groupby object and write it to a comma seperated value file called ('TOI_2017.csv')

# new injuries DF

injuries =NHL_Goalies[NHL_Goalies['Injuries'] is 'NaN']

# merge injuries and workhorse dataframes
mergedDF = pd.merge(workhorse, injuries,left_on='Last Name',right_on='Last Name',how='right')

#From the mergedDF keep FirstName/LastName/Team/Cntry/ SV% /GA/GAA/ TOI (note one copy for any duplicate column)
#not sure

# using .groupby function to see The Means, Mins, and Maximum of the kept columns
mergedDF=mergedDF.groupby('country').columns.agg(['mean', 'min', 'max'])


#Create a dataframe of the TOI groupby object and write it to a comma seperated value file called ('TOI_2017.csv')

TOI=mergedDF[mergedDF['TOI']]

TOI.to_csv('TOI_2017.csv')

#6

#write a functions subsets a dataframe by removing rows that are WITHIN the InterQuartile Region of a specified column

#The function takes as input
    #A: Pandas_Dataframe (For example use NHL_GoaliesDF)
    #B. Column name
    #Add a condition that returns an error if the Column Name chosen is not:
    #A. Numeric Dtype
    #B. Does not exist in the Numeric Columns
    #The output is a DataFrame that removes rows outside of the specified columns IQR

df.A <- df[df$A > quantile(df$A,0.25) & df$A < quantile(df$A,0.75), c("A")]

#add in own info