# -*- coding: utf-8 -*-
"""CSC302Homework6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d1kLYQkXfxdmECcUliLOaP9eCPjkx8DU
"""

import pandas as pd
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

"""##Q2
Please follow the instructions below and inspect the outputs before you proceed. You can always check this original final to compare your results in your own copy.
"""

#You have to make sure that you were able to write the file to a csv while your were working in R
house=pd.read_csv('/content/drive/MyDrive/DATA/house_prices.csv')
house.head()

"""a) For the states below, please select the rows from the house dataframe, and consider converting the date column to date data type as it may be coming in string format. Then use the head function to preview your new dataframe."""

states = ['Michigan', 'California', 'Texas', 'Indiana']
#your code goes here

"""b) Use the FacetGrid from seaborn to create line plots to represent house_price_index for each state. Please make the line color red, set ticks on x axis for years ['1980', '2000', '2020'], which you may have to convert date type again, put those years as labels, and set the titles for each small plot to their state names. In addition, set the y label to 'house price index' and remove the x label since it's obvious that these are years."""

#your code goes here

"""c) Draw a lineplot for 'house price perc', but color them based on the 'state' name which will have four lines in a single plot. Set a legend which will be at the bottom of your graph and have them horizantally positioned next to eachother. Again, set the y label to house_price_perc and remove the x label since it's obvious. (Note that my y label is still showing index. Please ignore that.)"""

#your code goes here

"""##Q4
Please work on your 4th question below. Please feel free to add new code cells.
"""

#Your code goes here.
world_cup = pd.read_csv('/content/drive/MyDrive/DATA/WorldCupMatches.csv')
world_cup.head()

#your code goes here. Just leaving an example output of an intermediate step for you to check the last two columns

world_cup2 = world_cup.groupby(by=(['Home Team Initials', 'Away Team Initials']))['Home Team Goals'].sum().reset_index()
world_cup3 = world_cup.groupby(by=(['Home Team Initials', 'Away Team Initials']))['Home Team Goals'].count().reset_index()

team_pairs = world_cup.groupby(by=(['Home Team Initials', "Away Team Initials"])).count().reset_index()
team_pairs['weight'] = team_pairs['Year']
team_pairs['HomeTeamGoalTotal'] = world_cup2['Home Team Goals']
team_pairs = team_pairs[['Home Team Initials', 'Away Team Initials', 'weight', 'HomeTeamGoalTotal']]
team_pairs.head()

"""Make sure that you only write four columns ('Home Team Initials', 'Away Team Initials', 'weight', 'HomeGoalTotal') from the data frame, team_pairs, to a csv file"""

team_pairs.to_csv('/content/drive/MyDrive/team_pairs.csv')