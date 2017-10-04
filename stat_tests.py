from __future__ import print_function

import numpy as np
import pandas as pd
import scipy.stats
import statsmodels.stats.proportion
import sklearn.metrics


def one_sample_proportion_confidence_interval(n_successes, n_trials,
                                              confidence=0.95):
    '''One-sample proportion confidence interval

    For example, if `n_successes` out of `n_trials` customers clicked the link, what is the confidence interval of click through rate?

    Parameters:
    n_successes: number of successes
    n_trials: number of trials
    confidence: float number from (0, 1)

    Returns:
    confidence_interval
    '''
    p_hat = n_successes / n_trials
    standard_error_of_mean = np.sqrt(p_hat * (1 - p_hat) / n_trials)
    alpha = 1 - confidence
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = p_hat - z_critical * standard_error_of_mean, p_hat +\
        z_critical * standard_error_of_mean
    return confidence_interval


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


def _one_sample_proportion_test_t(n_successes, n_trials, p_hypo,
                                  one_side=False):
    a = [1] * n_successes + [0] * (n_trials - n_successes)
    return scipy.stats.ttest_1samp(a, popmean=p_hypo)


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


def one_sample_mean_confidence_interval(data,
                                        confidence=0.95):
    '''One-sample mean confidence interval

    For example, if `data` is the heights of a group of men, what is the confidence interval of size `confidence` for the mean of the heights?

    Parameters:
    data
    confidence: float number from (0, 1)

    Returns:
    confidence_interval
    '''
    a = np.array(data)
    n = len(a)
    mean_ = a.mean()
    sample_standard_devication = sum((a - mean_) ** 2) /  (n-1)
    standard_error_of_mean = np.sqrt(sample_standard_devication / n)
    alpha = 1 - confidence
    z_critical = scipy.stats.norm.ppf(1 - alpha / 2)
    confidence_interval = mean_ - z_critical * standard_error_of_mean,\
        mean_ + z_critical * standard_error_of_mean
    return confidence_interval


# https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
def _one_sample_mean_confidence_interval_t(data, confidence=0.95):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t._ppf((1+confidence)/2., n-1)
    return m-h, m+h


def one_sample_mean_test(data, m_hypo):
    '''One-sample test of mean
    For example, if `data` is the heights of a group of men, and the hypothesis is that the mean of the heights is `m_hypo`, does data support this hypothesis?

    Parameters:
    data
    m_hypo: hypothetical mean

    Returns:
    t_score, p_value
    '''
    a = np.array(data)
    t, p_value = scipy.stats.ttest_1samp(a, popmean=m_hypo)
    return t, p_value


def two_sample_mean_test(data1, data2):
    '''Two-sample test of mean
    For example, if `data1` is the heights of a group of men, `data2` is the heights of a group of women, and the hypothesis is that the means of men and women are the same, does data support this hypothesis?

    Parameters:
    data1, data2

    Returns:
    t_score, p_value
    '''
    a, b = np.array(data1), np.array(data2)
    t, p_value = scipy.stats.ttest_ind(a, b)
    return t, p_value


def multi_sample_mean_test(data_sets):
    '''Multi-sample test of mean
    For example, if `data1` is the heights of football team A, `data2` is the heights of football team B, `data3` is the heights of football team C, and the hypothesis is that the means of the teams are the same, does data support this hypothesis?

    Parameters:
    data_sets

    Returns:
    f_score, p_value
    '''
    f, p_value = scipy.stats.f_oneway(*data_sets)
    return f, p_value


def paired_sample_mean_test(data1, data2):
    '''Paired-sample test of mean
    For example, if `data1` is the heights of a group of men in the morning, `data2` is the heights of the same group of men in the evening (with the same order), and the hypothesis is that the heights of morning and evening are the same, does data support this hypothesis?

    Parameters:
    data1, data2

    Returns:
    t_score, p_value

    '''
    a, b = np.array(data1), np.array(data2)
    t, p_value = scipy.stats.ttest_rel(a, b)
    return t, p_value


def correlation_coef(data1, data2):
    '''Correlation coefficient and non-correlation test for two continuous variables
    For example, if `data1` is the English test score of a group of students, `data2` is the Math test score of the same group of students, are the two scores correlated? Null hypothesis is non-correlation.

    Parameters:
    data1, data2

    Returns:
    Pearson correlation coefficient, p-value of non-correlation test
    '''
    x, y = np.array(data1), np.array(data2)
    r, p_value = scipy.stats.pearsonr(x, y)
    return r, p_value


def make_contingency(data1, data2):
    '''Make contingency table of two categorical data sets
    '''
    df = pd.DataFrame({
        '_': 0,
        'data1': data1,
        'data2': data2,
    })
    contingency_table = df.pivot_table(
        values='_',
        columns='data1',
        index='data2',
        aggfunc='count')

    return contingency_table


def chisq(data1, data2):
    '''Chi-squred test for two categorical variables
    For example, if `data1` is the blood type of a group of people, `data2` is the gender of the same group of people, are blood type and gender correlated?  Null hypothesis is non-correlation.

    Parameters:
    data1, data2

    Returns:
    chi2_score, p-value of non-correlation test

    '''
    contingency_table = make_contingency(data1, data2)
    chi2, p_value, _, _ = scipy.stats.chi2_contingency(contingency_table)
    return chi2, p_value


def joint_entropy(x, y):
    '''Joint entropy of two categorical variables.
    '''
    df = pd.DataFrame(np.stack((x, y), axis=1))
    df.columns = ['a', 'b']
    df_value_counts_joined = df.groupby(['a', 'b']).size().reset_index().\
        rename(columns={0:  'count'})
    value_counts_joined = df_value_counts_joined['count']
    return scipy.stats.entropy(value_counts_joined)


def mutual_information(data1, data2):
    '''Mutual information of two categorical variables
    For example, if `data1` is the blood type of a group of people, `data2` is the gender of the same group of people, are blood type and gender mutually dependent?

    Parameters:
    data1, data2

    Returns:
    mutual_information
    '''

    H1 = scipy.stats.entropy(np.bincount(data1))
    H2 = scipy.stats.entropy(np.bincount(data2))
    mutual_information = H1 + H2 - joint_entropy(data1, data2)
    return mutual_information


def _mutual_information_sklearn(data1, data2):
    return sklearn.metrics.mutual_info_score(data1, data2)
