# Airbnb Reviews Analysis
## Purpose
The purpose of repo is to explore 3 approaches for getting key information from guest reviews.

The 3 approaches include:
1. LDA - automatic topic discovery
2. TF-IDF - obtaining relevant keywords
3. Text Summarisation - obtaining most informative sentences

## Set up
Download dataset
```
$ mkdir amsterdam
$ cd amsterdam
$ wget http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2019-05-06/visualisations/reviews.csv
```

## Notebooks
1. [Data Cleaning, Feature Engineering, TfIdf](./Data%20Cleaning,%20Feature%20Engineering,%20TfIdf.ipynb)

    **_Purpose:_** used to clean reviews (include filtering out non-English reviews) and applied Approach#2 TF-IDF on cleaned reviews.

2. [Colab - FastText Language Identification](./Colab%20-%20FastText%20Language%20Identification.ipynb)

    **_Purpose:_** used to obtain languages of reviews. Only English reviews are kept for this purpose

3. [LDA](./LDA.ipynb)

    **_Purpose:_** Approach#1 - identifying topics automatically

4. [Text Summarisation](./Text%20Summarisation.ipynb)

    **_Purpose:_** Approach#3 - create GloVe embeddings and applied TextRank algorithm to determine how informative each sentence is.

## Credits
- [InsideAirbnb](http://insideairbnb.com/get-the-data.html) - Data source
- [Facebook Research](https://fasttext.cc/docs/en/language-identification.html) - fastText pretrained language model
- [Stanford NLP Group](https://nlp.stanford.edu/projects/glove/) - GloVe word embeddings
