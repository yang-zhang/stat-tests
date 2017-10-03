### Install locally
```sh
python setup.py install
```
### Install using pip
```sh
pip install stat-tests
```

### To import
```py
>>> import stat_tests as st
```

### One-sample proportion confidence interval
For example, if `n_successes` out of `n_trials` customers clicked the link, what is the confidence interval of click through rate?
```py
>>> st.one_sample_proportion_confidence_interval(n_successes=200, n_trials=1000, confidence=0.95)
(0.17520819870781754, 0.22479180129218249)
```

### One-sample proportion significant test
For example, if `n_successes` out of `n_trials` customers clicked the link, and the hypothesis is that the click through rate is `p_hypo`, does data support this hypothesis?
```py
>>> z_score, p_value = st.one_sample_proportion_test(n_successes=5123, n_trials=10000, p_hypo=0.5)
>>> z_score, p_value
(2.460744684807139, 0.013864899319339763)
```
If x out of n customers are men, and the hypothesis is that more than 50% of the customers are men, does data support this hypothesis?
```py
>>> z_score, p_value = st.one_sample_proportion_test(n_successes=5123, n_trials=10000, p_hypo=0.5, one_side=True)
>>> z_score, p_value
(2.460744684807139, 0.0069324496596698815)
```

### Two-sample proportion significant test
For example, if `n_successes_1` out of `n_trials_1` customers click through on Website Version A, `n_successes_2` out of `n_trials_2` customers click through on Website Version B, and the hypothesis is that the click through rates are the same, does data support this hypothesis?
```py
>>> z_score, p_value = st.two_sample_proportion_test(n_successes_1=20, n_trials_1=300, n_successes_2=21, n_trials_2=298)
>>> z_score, p_value
(-0.18400991456652802, 0.85400567703455788)
```

### One-sample mean confidence interval
For example, if `data` is the heights of a group of men, what is the confidence interval of size `confidence` for the mean of the heights?
```py
>>> data = 1.80 + 0.2 * np.random.randn(1000)
>>> st.one_sample_mean_confidence_interval(data, confidence=0.95)
(1.7980145129603369, 1.8228186217572906)
```

### One-sample test of mean
For example, if `data` is the heights of a group of men, and the hypothesis is that the mean of the heights is `m_hypo`, does data support this hypothesis?
```py
>>> data = 1.80 + 0.2 * np.random.randn(1000)
>>> t_score, p_value = st.one_sample_mean_test(data, p_hypo=1.78)
>>> t_score, p_value
(4.8430777499530517, 1.4808428763412875e-06)
```

### Two-sample test of mean
For example, if `data1` is the heights of a group of men, `data2` is the heights of a group of women, and the hypothesis is that the means of men and women are the same, does data support this hypothesis?

```py
>>> data1 = 1.80 + 0.2 * np.random.randn(1000)
>>> data2 = 1.70 + 0.2 * np.random.randn(1000)
>>> t_score, p_value = st.two_sample_mean_test(data1, data2)
>>> t_score, p_value
(11.720297373853812, 9.9185358995527835e-31)
```

### Paired-sample test of mean
For example, if `data1` is the heights of a group of men in the morning, `data2` is the heights of the same group of men in the evening (with the same order), and the hypothesis is that the heights of morning and evening are the same, does data support this hypothesis?
```py
>>> data1 = 1.80 + 0.2 * np.random.randn(1000)
>>> data2 = data1 + 0.01 + 0.01 * np.random.randn(len(data1))
>>> t_score, p_value = st.paired_sample_mean_test(data1, data2)
>>> t_score, p_value
(-34.149842899654423, 5.452067026533736e-170)

>>> data2 = data1 + 0.01 * np.random.randn(len(data1))
>>> t_score, p_value = st.paired_sample_mean_test(data1, data2)
>>> t_score, p_value
(-0.43398665574510392, 0.66439183811383029)
```

### Correlation coefficient and non-correlation test
For example, if `data1` is the English test score of a group of students, `data2` is the Math test score of the same group of students, are the two scores correlated?
```py
>>> data1 = 3 + 0.2 * np.random.randn(1000)
>>> data2 = 3 + 0.2 * np.random.randn(1000)
>>> r, p_value = st.correlation_coef(data1, data2)
>>> r, p_value
(0.0031232102929028708, 0.92142308109769133)

>>> data2 = data1 + 0.5 * np.random.randn(len(data1))
>>> r, p_value = st.correlation_coef(data1, data2)
>>> r, p_value
(0.37799832675973383, 2.566197851682784e-35)
```





