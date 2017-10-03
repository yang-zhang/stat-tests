### Install locally
```sh
python setup.py sdist
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
>>> import numpy as np
>>> data = 1.80 + 0.2 * np.random.randn(1000)
>>> st.one_sample_mean_confidence_interval(data, confidence=0.95)
(1.7980145129603369, 1.8228186217572906)
```
