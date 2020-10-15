import numpy as np
import pandas as pd


def get_gaussian_region(mean, variance):
    lb = mean - 2 * np.sqrt(variance)
    ub = mean + 2 * np.sqrt(variance)
    return mean, lb, ub


def combine_trials(df_list, x_col):
    df_list = sorted(df_list, key=lambda x: len(x), reverse=True)
    merged_df = df_list[0]
    if not all([len(df) == len(merged_df) for df in df_list]):
        print("trials are not all the same length!")
    for df in df_list[1:]:
        merged_df = pd.merge_asof(merged_df, df, on=x_col, direction='nearest')
    merged_df.fillna(method='ffill')
    return merged_df
