from __future__ import print_function

import numpy as np
import scipy.stats


def find_confidence_interval(x, n, confidence_interval_size):
    p_hat = x / n
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n)
    alpha = 1 - confidence_interval_size
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = p_hat - z_critical * standard_error, p_hat + \
        z_critical * standard_error
    return confidence_interval
