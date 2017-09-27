from __future__ import print_function

import numpy as np
import scipy.stats
import statsmodels.stats.proportion


def find_confidence_interval(x, n, confidence_interval_size):
    p_hat = x / n
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n)
    alpha = 1 - confidence_interval_size
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = p_hat - z_critical * standard_error, p_hat + \
        z_critical * standard_error
    return confidence_interval


def single_proportion_ztest(x, n, p_hypo=0.5, prop_var=None, one_side=False):
    p_hat = x / n
    if not prop_var:
        prop_var = p_hat
    standard_error = np.sqrt(prop_var * (1 - prop_var) / n)
    z = (p_hat - p_hypo) / standard_error
    p_value = 1 - scipy.stats.norm.cdf(abs(z))
    if not one_side:
        p_value *= 2
    return z, p_value

def
