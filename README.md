# stat-tests
Easy-to-use statistical tests in Python

### Install locally
```sh
python setup.py sdist
```
<!--- 
### Install using pip
```sh
pip install stat-tests
```
--> 

## To use

```py
>>> import stat_tests
```

### Single proportion confidence interval
For example
```py
>>> stat_tests.single_proportion_confidence_interval(200, 1000)
(0.17520819870781754, 0.22479180129218249)
```

### Single proportion significant test
For example
```py
>>> stat_tests.single_proportion_test(5123, 10000, p_hypo=0.5)
(2.460744684807139, 0.013864899319339763)

>>> stat_tests.single_proportion_test(5123, 10000, p_hypo=0.5, one_side=True)
(2.460744684807139, 0.0069324496596698815)
```



