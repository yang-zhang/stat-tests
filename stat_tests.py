from __future__ import print_function

import numpy as np
import scipy.stats
import statsmodels.stats.proportion


def single_proportion_confidence_interval(x, n, confidence_interval_size=0.95):
    '''Single proportion confidence interval.

    For example, if x out of n customers clicked the link , what is the \
    confidence interval of click through rate.

    Parameters:
    x: number of samples of interest
    n: number of total samples
    confidence_interval_size: 0 to 1

    Returns:
    confidence_interval
    '''
    p_hat = x / n
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n)
    alpha = 1 - confidence_interval_size
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = p_hat - z_critical * standard_error, p_hat + \
        z_critical * standard_error
    return confidence_interval


def single_proportion_test(x, n, p_hypo=0.5, one_side=False):
    '''Single proportion ztest.

    For example, if x out of n customers are men, and the hypothesis is that\
    50% of the customers are men, does data support this hypothesis?

    Parameters:
    x: number of samples of interest
    n: number of total samples
    p_hypo: hypothetical proportion
    one_side: if True, do one side test

    Returns:
    z: z score
    p: p_value
    '''
    p_hat = x / n
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n)
    z = (p_hat - p_hypo) / standard_error
    p_value = 1 - scipy.stats.norm.cdf(abs(z))
    if not one_side:
        p_value *= 2
    return z, p_value


