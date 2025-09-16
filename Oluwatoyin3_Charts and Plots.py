# import libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
quality_alcohol = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Datasets/Wine.csv", encoding='latin-1')

#show the top few rows
print(quality_alcohol.head())

#1a)Draw a bar chart using ‘quality’ and ‘alcohol’ column to see if the quality level has any relationship with the alcohol amount
qua_lev = quality_alcohol.groupby('quality')['alcohol'].mean()
print(qua_lev)

#Ploting histogram
plt.bar(quality_alcohol['quality'], quality_alcohol['alcohol'])
plt.xlabel('quality_level')
plt.ylabel('alcohol_amount')
plt.title ('The relationship between alcohol amount and quality level')
plt.show()

#1b)Draw a histogram plot using `total sulfur dioxide’ and ‘quality’, and explain what you learn from thefigure
plt.hist(quality_alcohol['total sulfur dioxide'], bins=[20, 40, 60, 80, 100, 120])
plt.show()

#1c)Draw a scatter plot using `residual sugar’ and ‘quality’, and explain what you learn from thefigure
plt.scatter(quality_alcohol['residual sugar'], quality_alcohol['quality'])
plt.xlabel('residual_sugar')
plt.ylabel('quality')
plt.title('The relationship between residual sugar and quality')
plt.show()

#1d)Draw a hexbin plot using `residual sugar’ and ‘alcohol’, and explain what you learn from the figure
quality_alcohol.plot.hexbin(x='residual sugar', y='alcohol', gridsize=20)
plt.show()


#2) (1)	Select the 10 countries with the largest population in year 1960, use the heatmap to show the changes of the populations of these 10 countries from 1960 to 1970.

largest_population = pd.read_csv("C:/Users/HP/OneDrive/Desktop/Ty  - Fall 2023/Programming/Datasets/country_population_historic.csv", encoding='latin-1')

print(largest_population.head())

country = largest_population.set_index('Country Name')
top_10_countries_1960 = largest_population.sort_values(by='1960', ascending=False).head(10)
top_10_countries_1960_transposed = top_10_countries_1960.set_index('Country Name')
print(top_10_countries_1960_transposed)

plt.figure(figsize=(10, 8))
sns.heatmap(top_10_countries_1960.transpose(), cmap='YlGnBu', annot=True, fmt=",.0f", linewidths=.5)
plt.title('Population Changes (1960-1970) - Top 10 Countries')
plt.xlabel('Countries')
plt.ylabel('Year')
plt.show()
















"""
largest_population = largest_population.iloc[:, :12]

print(largest_population)
geo1 = geo.GeonamesCache()
#List of countries
mnt = [country['name'] for country in geo1.get_countries().values()]
print(mnt)

geo2 = largest_population[largest_population['Country Name'].isin(cnt)]

population = geo2.iloc[:,:12]
population = geo2.sort_values(by='1960', ascending = False).head(10)
population.set.index(population.columns[0], inplace=True)
sns.heatmap(population, cmap = 'Spectral')
plt.show()
"""






