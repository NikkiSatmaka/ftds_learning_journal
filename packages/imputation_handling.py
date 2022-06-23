#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

"""
Useful functions to handle missing values
"""


def prepare_imputation(data, variable, *args):
    """
    Prepare data for imputation

    Parameters
    ----------
    data : pandas.DataFrame
        Dataframe to be prepared for imputation
    variable : list
        List of columns to be imputed
    *args :
        List of special keywords representing the missing values

    Returns
    -------
    pandas.DataFrame
        Dataframe prepared for imputation
    """

    if data is None or variable is None:
        raise ValueError('data and variable must be specified')
    
    # prepare output dataframe
    output_data = data.copy()

    # replace missval with nan for features in impute_cols
    for col in variable:
        for missval in args:
            output_data[col] = output_data[col].replace(missval, np.nan)

    return output_data


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
    
    # prepare output dataframe
    output_data = data.copy()

    output_data[variable+'_mean'] = output_data[variable].fillna(mean_value)
    output_data[variable+'_median'] = output_data[variable].fillna(median_value)
    output_data[variable+'_zero'] = output_data[variable].fillna(0)

    return output_data

