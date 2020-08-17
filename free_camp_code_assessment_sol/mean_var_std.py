import numpy as np

def calculate(lists):
    new_value = np.array(lists).reshape(3,3)
    row_mean = np.mean(new_value, axis=0)
    col_mean = np.mean(new_value, axis= 1)
    agg_mean = np.mean(new_value)


    row_std = np.std(new_value, axis= 0)
    col_std = np.std(new_value, axis=1)
    agg_std = np.std(new_value)


    row_var = np.var(new_value, axis=0)
    col_var = np.var(new_value, axis=1)
    agg_var = np.var(new_value)


    row_sum = np.sum(new_value, axis=0)
    col_sum = np.sum(new_value, axis=1)
    agg_sum = np.sum(new_value)


    row_max = np.max(new_value, axis=0)
    col_max = np.max(new_value, axis=1)
    agg_max = np.max(new_value)


    row_min = np.min(new_value, axis=0)
    col_min = np.min(new_value, axis=1)
    agg_min = np.min(new_value)

    calculations = {'mean': [row_mean, col_mean, agg_mean], 'variance': [row_var, col_var, agg_var], 'standard deviation': [row_std, col_std, agg_std], 'max': [row_max, col_max, agg_max], 'min': [row_min, col_min, agg_min], 'sum': [row_sum, col_sum, agg_sum]}

    return calculations
