import numpy as np 
import pandas as pd 
import scipy.stats as stats
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt 
import math 

#Importing csv file
myDF = pd.read_csv('diabetes.csv')

#Sorting cs file by the column Age
mySortedDf = myDF.sort_values(by='Age')

#To check if its sorted correctly 
print(mySortedDf.head())

#creating my bianary field and scale field
myBin = mySortedDf['Outcome']
myScale = mySortedDf['Age']

#looking how many of each true or false there is inside the file
print(myBin.value_counts())

#Seperating each category using a list with booleans
cat0 = myBin == 0
cat1 = myBin == 1

#looking at said list
print(cat0.head())

#Storing the scores of each category and storing them seperetly 
#Using dropna to drop any missing values
cat0Score = myScale[cat0].dropna()
cat1Score = myScale[cat1].dropna()

#The t test itself 
print(stats.ttest_ind(cat0Score,cat1Score))