# Predict book genres

## Intro
This project aims to use Machine Learning models (ML) and Natural Language Processing (NLP) to predict a book genre based on it's description.

## Data
The original data comes from [Goodreads Book Datasets](https://www.kaggle.com/bahramjannesarr/goodreads-book-datasets-10m) in Kaggle. It was adapted using the script "get_book_genre.py".

The generated data is [here](https://www.kaggle.com/heryhelder/books-data). Download it and put into a "new_data" folder.

If you want to go from scratch, you need to download the Goodreads Book Datasets and process it using "get_book_genre.py" file, it took almost 24 hours to run on my PC, so be careful. The new generated data will be in the "new_data" folder.

All the analysis is in the "genre_analysis.ipynb" file.

## Dependencies
- Numpy
- Pandas
- NLTK
- Scikit-learn
- Regex
