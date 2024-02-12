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

# display the dataframe structure, data and test the merger of df_title_basics_2018 and df_title_ratings were correct
print(merged_df_title.head().to_string())

# get the overall statistics of the merged data of df_title_basics_2018 and df_title_ratings
print(merged_df_title.describe())

# filter the films by year of 2018 only
films_year_2018 = merged_df_title[merged_df_title['year'] == 2018]

# check the overall statistics of filtered data
print(films_year_2018.describe()) # mean of year is 2018

# first we filter out the films with number of votes that were average and above
best_films_2018 = films_year_2018[films_year_2018['numVotes'] >= films_year_2018['numVotes'].mean()]

# display the filtered data
print(best_films_2018.head().to_string())

# second we filter of the films with rating score that were rating score were average and above
best_films_2018 = best_films_2018[best_films_2018['averageRating'] >= best_films_2018['averageRating'].mean()]

# display the filtered data
print(best_films_2018.head().to_string())

# get the average run time of the films
average_film_run_time = best_films_2018['runtimeMinutes'].mean()

# get the overall statistics of the filter data
print("Average / mean of a film for year 2018: " + str(average_film_run_time))

# filter out the films with longer run time that were above or average run time
longer_view_time_films = films_year_2018[films_year_2018['runtimeMinutes'] >= average_film_run_time]

# get the overall statistics of the filter data
print(longer_view_time_films.describe())

# filter out the films with shorter run time that were below the average run time
shorter_view_time_films = films_year_2018[films_year_2018['runtimeMinutes'] < average_film_run_time]

# get the overall statistics of the filter data
print(shorter_view_time_films .describe())

print("Average rating score score of longer run or view time films: " + str(round(longer_view_time_films['averageRating'].mean(),4)))

print("Average rating score score of shorter run or view time films: " + str(round(shorter_view_time_films['averageRating'].mean(),4)))

# compare the average rating score of longer run view time films and shorter run view time films
if longer_view_time_films['averageRating'].mean() > shorter_view_time_films['averageRating'].mean():
    print("Audiences in year 2018 prefer film with longer run view time")
else:
    print("Audiences in year 2018 prefer film with shorter run view time")

