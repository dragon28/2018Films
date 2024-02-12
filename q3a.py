import pandas as pd

# read the title_basics_2018.csv file and load it into Pandas DataFrame
df_title_basics_2018 = pd.read_csv('./title_basics_2018.csv')

# display the dataframe structure, data and test the title_basics_2018.csv file was loaded correctly
print(df_title_basics_2018.head().to_string())

# read the title_ratings.csv file and load it into Pandas DataFrame
df_title_ratings = pd.read_csv('./title_ratings.csv')

# display the dataframe structure, data and test the title_ratings.csv file was loaded correctly
print(df_title_ratings.head().to_string())

# merge the df_title_basics_2018 and df_title_ratings on the 'tconst' column, which works as primary key:
merged_df_title = pd.merge(df_title_basics_2018, df_title_ratings, on='tconst')

# display the dataframe structure and test the merger of df_title_basics_2018 and df_title_ratings were correct
print(merged_df_title.head().to_string())

# filter the films by year of 2018 only
films_year_2018 = merged_df_title[merged_df_title['year'] == 2018]

# check the overall statistics of filtered data
print(films_year_2018.describe()) # mean of year is 2018

# first we filter out the films that contain the largest number of votes, which 25% of the most voted or top 25% most voted films
best_films_2018 = films_year_2018[films_year_2018['numVotes'] >= films_year_2018['numVotes'].nlargest(int(films_year_2018['tconst'].count() * 0.25)).min()]

# display the filtered data
print(best_films_2018.head().to_string())

# second we filter of the films that contain the highes rating score, which 25% of most rated or top 25% most rated films
best_film_2018 = best_films_2018[best_films_2018['averageRating'] >= best_films_2018['averageRating'].nlargest(int(best_films_2018['tconst'].count() * 0.25)).min()]

# display the filtered data
print(best_film_2018.head().to_string())

# and finally we filter by the most voted films
best_film_2018 = best_film_2018[best_film_2018['numVotes'] >= best_film_2018['numVotes'].max()]

# display the filtered data
print(best_film_2018.to_string()) # Avengers: Infinity War