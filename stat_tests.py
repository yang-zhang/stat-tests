from __future__ import print_function

import numpy as np
import scipy.stats
import statsmodels.stats.proportion


def one_sample_mean_confidence_interval(data,
                                        confidence_interval_size=0.95):
    '''One-sample mean confidence interval
    '''
    a = np.array(data)
    n = len(a)
    mean_ = a.mean()
    standard_error = np.sqrt( (a-mean_).sum() / n*(n-1))
    alpha = 1 - confidence_interval_size
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = mean_ - z_critical * standard_error, mean_ + \
        z_critical * standard_error
    return confidence_interval


# https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
def _mean_confidence_interval(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m+h


def one_sample_proportion_confidence_interval(n_successes, n_trials,
                                              confidence_interval_size=0.95):
    '''One-sample proportion confidence interval

    For example, if `n_successes` out of `n_trials` customers clicked the link, what is the confidence interval of click through rate?

    Parameters:
    n_successes: number of successes
    n_trials: number of trials
    confidence_interval_size: float number from (0, 1)

    Returns:
    confidence_interval
    '''
    p_hat = n_successes / n_trials
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n_trials)
    alpha = 1 - confidence_interval_size
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = p_hat - z_critical * standard_error, p_hat + \
        z_critical * standard_error
    return confidence_interval


def _one_sample_proportion_ttest(n_successes, n_trials, p_hypo,
                                 one_side=False):
    a = [1] * n_successes + [0] * (n_trials - n_successes)
    return scipy.stats.ttest_1samp(a, popmean=p_hypo)


def one_sample_proportion_test(n_successes, n_trials, p_hypo, one_side=False):
    '''One-sample proportion significant test

    For example, if `n_successes` out of `n_trials` customers clicked the link, and the hypothesis is that the click through rate is `p_hypo`, does data support this hypothesis?

    Parameters:
    n_successes: number of successes
    n_trials: number of trials
    p_hypo: hypothetical proportion
    one_side: if True, do one side test

    Returns:
    z_score, p_value
    '''
    p_hat = n_successes / n_trials
    standard_error = np.sqrt(p_hat * (1 - p_hat) / n_trials)
    z = (p_hat - p_hypo) / standard_error
    p_value = 1 - scipy.stats.norm.cdf(abs(z))
    if not one_side:
        p_value *= 2
    return z, p_value


def two_sample_proportion_test(n_successes_1, n_trials_1, n_successes_2,
                               n_trials_2):
    '''Two-sample proportion significant test

    For example, if `n_successes_1` out of `n_trials_1` customers click through on Website Version A, `n_successes_2` out of `n_trials_2` customers click through on Website Version B, and the hypothesis is that the click through rates are the same, does data support this hypothesis?

    Parameters:
    n_successes_1: number of successes in Test-1
    n_trials_1: number of trials in Test-1
    n_successes_2: number of successes in Test-2
    n_trials_2: number of trials in Test-2

    Returns:
    z_score, p_value
    '''
    z, p_value = statsmodels.stats.proportion.proportions_ztest((n_successes_1, n_successes_2), (n_trials_1, n_trials_2))
    return z, p_value


def one_sample_sample_mean_test(sample):
    '''One sample test of mean

    '''
    pass


def paired_sample_mean_test(sample):
    '''Paired sample test of mean

    '''
    pass

