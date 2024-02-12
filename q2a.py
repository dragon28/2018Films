import pandas as pd

# read the title_basics_2018.csv file and load it into Pandas DataFrame
df_title_basics_2018 = pd.read_csv('./title_basics_2018.csv')

# print or display the dataframe structure and test the title_basics_2018.csv file was loaded correctly
print(df_title_basics_2018.head().to_string())

# read the title_ratings.csv file and load it into Pandas DataFrame
df_title_ratings = pd.read_csv('./title_ratings.csv')

# print or display the dataframe structure and test the title_ratings.csv file was loaded correctly
print(df_title_ratings.head().to_string())

# merge the df_title_basics_2018 and df_title_ratings based on the 'tconst' column, which works as primary key
merged_df_title = pd.merge(df_title_basics_2018, df_title_ratings, on='tconst')

# display the dataframe structure, data and check the overall merger of df_title_basics and df_title_ratings 
print(merged_df_title.head().to_string())

# filter the films by year of 2018 only
films_year_2018 = merged_df_title[merged_df_title['year'] == 2018]

# check the overall statistics of filtered data
print(films_year_2018.describe()) # mean of year is 2018

# filter out the rating score with 8 or higher from the 'averageRating' column of the merged dataframe 
films_scored_8_or_higer = films_year_2018[films_year_2018['averageRating'] >= 8.0]

# check the overall statistics of filtered data 
print(films_scored_8_or_higer.describe()) # averageRating min = 8.0 and count = 780

# get the total number of films with a score of 8.0 or higher
print("Total Number of fils with a score of 8.0 or higer: " + str(films_scored_8_or_higer['averageRating'].count())) # 780