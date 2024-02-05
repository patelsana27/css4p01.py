# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 00:31:05 2024

@author: patel
"""
'Question 1'

import pandas as pd
movie_df = pd.read_csv("\\Users\\patel\CHPC\\movie_dataset.csv")
highest_rated_movie = movie_df[movie_df['Rating'] == movie_df['Rating'].max()]['Title'].values[0]
print('Q1')
print(highest_rated_movie)

'Question 2'

average_revenue = movie_df['Revenue (Millions)'].mean()
print('Q2')
print(average_revenue)

'Question 3'

# Filter the dataframe for movies released between 2015 to 2017
filtered_movie_df = movie_df[(movie_df['Year'] >= 2015) & (movie_df['Year'] <= 2017)]

# Calculate the average revenue for the filtered movies
average_revenue_2015_to_2017 = filtered_movie_df['Revenue (Millions)'].mean()
print('Q3')
print(average_revenue_2015_to_2017)

'Question 4'

# Filter the dataframe for movies released in 2016
movies_2016 = movie_df[movie_df['Year'] == 2016]

# Count the number of movies released in 2016
No_movies_2016 = len(movies_2016)

print('Q4')
print(No_movies_2016)

'Question 5'

# To find the number of movies directed by Christopher Nolan
Nolan_directed_movies = movie_df[movie_df['Director'] == 'Christopher Nolan'].shape[0]

print('Q5')
print(Nolan_directed_movies)

'Question 6'

# Count the number of movies with a rating of at least 8.0
No_high_rated_movies = movie_df[movie_df['Rating'] >= 8.0].shape[0]
print('Q6')
print(No_high_rated_movies)

'Question 7'

# Filter the dataframe for movies directed by Christopher Nolan
Nolan_movies = movie_df[movie_df['Director'] == 'Christopher Nolan']

# Calculate the median rating of movies directed by Christopher Nolan
median_rating_Nolan_directed = Nolan_movies['Rating'].median()
print('Q7')
print(median_rating_Nolan_directed)

'Question 8'

# Calculate the average rating for each year and find the year with the highest average rating
Average_rating_yearly = movie_df.groupby('Year')['Rating'].mean()
year_with_highest_rating = Average_rating_yearly.idxmax()

print('Q8')
print(year_with_highest_rating)

'Question 9'

# Count the number of movies made in 2006
No_movies_2006 = movie_df[movie_df['Year'] == 2006].shape[0]

# Count the number of movies made in 2016
No_movies_2016 = movie_df[movie_df['Year'] == 2016].shape[0]

# Calculate the percentage increase
percentage_increase = ((No_movies_2016 - No_movies_2006) / No_movies_2006) * 100

print('Q9')
print(percentage_increase)

'Question 10'

from collections import Counter

# Combine all the actor names into a single list
all_actors = movie_df['Actors'].str.split(', ').sum()

# Count the occurrences of each actor
actor_counts = Counter(all_actors)

# Find the most common actor
most_common_actor = actor_counts.most_common(1)[0]

print('Q10')
print(most_common_actor)

'Question 11'

# Split the genres and create a list of all unique genres
unique_genres = set(movie_df['Genre'].str.split(',').explode())

# Count the number of unique genres
No_unique_genres = len(unique_genres)

print('Q11')
print(No_unique_genres)

'Question 12'

# Exclude non-numeric columns
numeric_columns = movie_df.select_dtypes(include='number')

# Calculate the correlation matrix
correlation_matrix = numeric_columns.corr()

#1. Positive correlation between Rating and Metascore - A higher ratings is associated with higher metascore which indicates it has received more positive reviews'
#2. Negative correlation between Rank and votes - Less ranked movies usually have less votes and fewer votes.
#3. No clear correlation between number of Years and other features - There isn't a clear significant correlation between the year movie was released and its rank, Runtime, Rating, Votes and Metascore. This implies that the year of release alone doesn't dictate a movies success or its quality.
#4. Moderate positive correlation between Revenue and votes.
#5. No strong correlation between Runtime and Revenue. 

#ADVICE FOR DIRECTORS TO PRODUCE BETTER MOVIES:
    #1. To raise ratings: Draw in more people, put an emphasis on excellent storytelling and production value. 
    #2. Always interact with the audience and take their preferences.Seek criticism and identify areas that needs to be looked at and refine upcoming projects.
    #3. Work with skilled cinematographers to create visually stunning and impactful scenes.
    
'Question 13'
