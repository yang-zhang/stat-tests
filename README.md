### Install locally
```sh
python setup.py sdist
```
### Install using pip
```sh
pip install stat-tests
```

### To use
```py
>>> import stat_tests
```

### Single proportion confidence interval
If x out of n customers clicked through, what is the confidence interval of click through rate.
```py
>>> stat_tests.single_proportion_confidence_interval(x=200, n=1000)
(0.17520819870781754, 0.22479180129218249)
```

### Single proportion significant test
If x out of n customers are men, and the hypothesis is that 50% of the customers are men, does data support this hypothesis?
```py
>>> z_score, p_value = stat_tests.single_proportion_test(x=5123, n=10000, p_hypo=0.5)
>>> z_score, p_value
(2.460744684807139, 0.013864899319339763)
```
If x out of n customers are men, and the hypothesis is that more than 50% of the customers are men, does data support this hypothesis? 
```py
>>> z_score, p_value = stat_tests.single_proportion_test(x=5123, n=10000, p_hypo=0.5, one_side=True)
>>> z_score, p_value
(2.460744684807139, 0.0069324496596698815)
```

### Tow sample proportion significant test
If x1 out of n1 customers click through on Website Version A, x2 out of n2 customers click through on Website Version B, and the hypothesis is that the click through rates are the same, does data support this hypothesis?
```py
>>> z_score, p_value = stat_tests.two_sample_proportion_test(x1=20, n1=300, x2=21, n2=298)
>>> z_score, p_value 
(-0.18400991456652802, 0.85400567703455788)
```

