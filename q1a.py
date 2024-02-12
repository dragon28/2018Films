import pandas as pd
import re

# read the title_basics_2018.csv file and load it into Pandas DataFrame
df_title_basics_2018 = pd.read_csv('./title_basics_2018.csv')

# display the dataframe structure, data and test the title_basics_2018.csv file was loaded correctly
print(df_title_basics_2018.head(8).to_string())

# filter the films by year of 2018 only
films_year_2018 = df_title_basics_2018[df_title_basics_2018['year'] == 2018]

# check the overall statistics of filtered data
print(films_year_2018.describe()) # mean of year is 2018

# filter out the category of the films in the 'genres' column that were 'Comedy'
#comedy = films_year_2018[films_year_2018['genres'] == 'Comedy']

# get the total number of films that categorized as 'Comedy'
#print(comedy['genres'].count()) # 800


# filter out the category of the films in the 'genres' column that contain the word 'Comedy'
comedy = films_year_2018[films_year_2018['genres'].str.contains(pat="Comedy|comedy",flags=re.IGNORECASE) == True]

# get the total number of films that categorized as 'Comedy'
print("Total number of films that categorized as 'Comedy': " + str(comedy['genres'].count())) # 2233