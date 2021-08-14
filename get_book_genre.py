# Import libraries
import pandas as pd
import numpy as np
import requests
import glob
import swifter

# Create empty dataframe
books_df = pd.DataFrame()

# Iterate through every CSV file and concatenate them into a single dataframe
for file in glob.glob("data/*.csv"):
    # Load only the "Name", "Authors", "PublishYear", "Description", "ISBN" and "Language" columns
    try:
        books_df = pd.concat([books_df, pd.read_csv(file, usecols=["Name", "Authors", "PublishYear", "Description", "ISBN", "Language"])], axis=0)
    except ValueError:
        continue

# Drop missing values (Nan)
books_df.dropna(subset=["ISBN", "Language", "Description"], inplace=True)

# Let's see the languages of the books in the dataset
print(books_df["Language"].value_counts().head(20))

# Change the language name to be more consistent. We are going to use only english, so we are going to set other languages to be nan values.
books_df["Language"] = books_df["Language"].apply(lambda x: "eng" if x in ["eng", "en-US", "en-GB", "en-CA"] else np.nan)

# Drop other languages
books_df.dropna(subset=["Language"], inplace=True)
books_df.reset_index(drop=True, inplace=True)

# Return book genres (from Google API, as a list) or set it to be np.nan
def get_genres(isbn):
    genres = np.nan
    url_base = "https://www.googleapis.com/books/v1/volumes?q=isbn:"

    r = requests.get(url=url_base+isbn)

    if r.status_code == requests.codes.ok and not r.json()["totalItems"] == 0:
        if "categories" in r.json()["items"][0]["volumeInfo"]:
            genres = r.json()["items"][0]["volumeInfo"]["categories"]

    return genres

# We are going to use "swifter" to choose the best way to perform the task.
# Since it's initially 10M books, it will take a long time to get the genres list for each book.
# It took more than 24 hours to run on my PC.
books_df["Genres"] = books_df["ISBN"].swifter.apply(lambda x: get_genres(x))

# Drop missing genres
books_df.dropna(subset=["Genres"], inplace=True)

# Save it to a new CSV file for analysis
books_df.to_csv("new_data/books_data.csv")