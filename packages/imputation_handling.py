#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
Useful functions to handle missing values
"""


def prepare_imputation(data, variable):
    """
    Prepare data for imputation
    
    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be prepared for imputation
    variable : list
        List of columns to be imputed

    Returns
    -------
    pandas.DataFrame
        Dataframe prepared for imputation
    """
    
    if data is None or variable is None:
        raise ValueError('data and variable must be specified')

    # replace 'unknown' with nan for features in impute_cols
    for col in variable:
        data[col] = data[col].replace('unknown', np.nan)
    
    return data


def impute_na(data, variable, mean_value, median_value):
    """
    Function to Fill Missing Values with Zeroes, Mean, and Median

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be imputed
    variable : str
        Column to be imputed
    mean_value : float  
        Mean value to be used for imputation
    median_value : float
        Median value to be used for imputation

    Returns
    -------
    pandas.DataFrame
        Dataframe with imputed values
    """

    data[variable+'_mean'] = data[variable].fillna(mean_value)
    data[variable+'_median'] = data[variable].fillna(median_value)
    data[variable+'_zero'] = data[variable].fillna(0)

    return data
