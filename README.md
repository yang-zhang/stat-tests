# stat-tests
Easy-to-use statistical tests in Python

### Install locally
```sh
python setup.py sdist
```
### Install using pip
```sh
pip install stat-tests
```

## To use
```py
>>> import stat_tests
```

### Single proportion confidence interval
For example, if x out of n customers clicked the link , what is the confidence interval of click through rate.
```py
>>> stat_tests.single_proportion_confidence_interval(x=200, n=1000)
(0.17520819870781754, 0.22479180129218249)
```

### Single proportion significant test
For example, if x out of n customers are men, and the hypothesis is that 50% of the customers are men, does data support this hypothesis?
```py
>>> stat_tests.single_proportion_test(x=5123, n=10000, p_hypo=0.5)
(2.460744684807139, 0.013864899319339763)

>>> stat_tests.single_proportion_test(x=5123, n=10000, p_hypo=0.5, one_side=True)
(2.460744684807139, 0.0069324496596698815)
```

### Tow sample proportion significant test
For example, if x1 out of n1 customers click through on Website Version A, x2 out of n2 customers click through on Website Version B, and the hypothesis is that the click through rates are the same, does data support this hypothesis?
```py
>>> stat_tests.two_sample_proportion_test(x1=20, n1=300, x2=21, n2=298)
(-0.18400991456652802, 0.85400567703455788)
```

