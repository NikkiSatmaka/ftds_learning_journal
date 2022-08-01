#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Useful functions to preprocess text data
"""

import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import spacy


def combine_text(data, combined_col, *args):
    """
    Combine text features into one feature

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to process
    combined_col : str
        Name of feature for combined text
    *args :
        List of features to combine. A feature can only be called once

    Returns
    -------
    pandas.DataFrame
        Dataframe with combined text

    """

    # validation check
    if data is None or combined_col is None:
        raise ValueError('`data` and `combined_col` must be specified')

    # validation check
    if combined_col in data:
        raise AttributeError(f'The feature `{combined_col}` already exist. Use new feature name')

    # prepare output data
    output_data = data.copy()

    # loop through features to combine
    for col in args:
        if combined_col not in output_data:
            output_data['news'] = output_data[col]
            output_data = output_data.drop([col], axis=1)
            continue
        output_data['news'] = output_data['news'] + '\n' + output_data[col]
        output_data = output_data.drop([col], axis=1)

    return output_data


def clean_text(text):
    """
    Clean text for NLP
        - Lowercase text
        - Strip unneeded characters

    Parameters
    ----------
    text : str
        Text to process

    Returns
    -------
    str
        Cleaned text
    """

    # preprocess text
    text_cleaned = text.lower()  # convert to lowercase
    text_cleaned = re.sub(r"@[A-Za-z0-9_]+", " ", text_cleaned)  # remove mention
    text_cleaned = re.sub(r"#[A-Za-z0-9_]+", " ", text_cleaned)  # remove hashtags
    text_cleaned = re.sub(r"\n", " ", text_cleaned)  # remove newline
    text_cleaned = re.sub(r"http\S+", " ", text_cleaned)  # remove link
    text_cleaned = re.sub(r"www\S+", " ", text_cleaned)  # remove link
    text_cleaned = re.sub(r"[^A-Za-z\s]", " ", text_cleaned)  # remove non-alpha characters aside from whitespace

    return text_cleaned


def strip_stopwords(text, stopwords=set(stopwords.words('english'))):
    """
    Strip stopwords from text for NLP

    Parameters
    ----------
    text : str
        Text to process
    stopwords : list-like
        List of stopwords. English from NLTK by default

    Returns
    -------
    str
        Text stripped of stopwords
    """

    # tokenize processed_text
    tokens = word_tokenize(text)

    # remove stopwords
    text_stopped = [token for token in tokens if token not in stopwords]

    return ' '.join(text_stopped)


def stem_text(text, stemmer=PorterStemmer()):
    """
    Stem text for NLP

    Parameters
    ----------
    text : str
        Text to process
    stemmer : stemmer object
        Stemmer object. PorterStemmer by default

    Returns
    -------
    str
        Lemmatized text
    """

    # tokenize processed_text
    tokens = word_tokenize(text)

    # stem text
    text_stemmed = [stemmer.stem(token) for token in tokens]

    return ' '.join(text_stemmed)


def lemmatize_text(text, lemmatizer=spacy.load('en_core_web_sm')):
    """
    Lemmatize text for NLP

    Parameters
    ----------
    text : str
        Text to process
    lemmatizer : lemmatizer object
        Lemmatizer object. Only accepts spacy object

    Returns
    -------
    str
        preprocessed text
    """
    if 'spacy' not in str(type(lemmatizer)):
        raise ValueError('lemmatizer only exceps spacy object')

    doc = lemmatizer(text)

    # lemmatize text
    text_lemmatized = [token.lemma_ for token in doc]

    return ' '.join(text_lemmatized)
