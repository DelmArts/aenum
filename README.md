# Report for Assignment 1 resit

## Project chosen

Name: aenum

URL: https://github.com/ethanfurman/aenum

Number of lines of code and the tool used to count it: 3241 (`lizard aenum -x"*test*"`)

Programming language: Python

## Coverage measurement with existing tool

`coverage.py` was run to analyze the existing coverage:

![coverage_initial.png](coverage_initial.png)

### Function 1

`aenum/_enum.py:bin()`: 0% branch coverage

![coverage_initial_fun1.png](coverage_initial_fun1.png)

### Function 2:

`aenum/_enum.py:bits()`: 0% branch coverage

![coverage_initial_fun2.png](coverage_initial_fun2.png)

## Coverage improvement

### Individual tests

### Function 1

Tests ([aenum/test_sep.py:5](aenum/test_sep.py#L5)):

![tests_fun1.png](tests_fun1.png)

Initial coverage: 0% branch coverage

![coverage_initial_fun1.png](coverage_initial_fun1.png)

Improvement: 100% branch coverage

![coverage_after_fun1.png](coverage_after_fun1.png)

### Function 2

Tests ([aenum/test_sep.py:19](aenum/test_sep.py#L19)):

![tests_fun2.png](tests_fun2.png)

Initial coverage: 0% branch coverage

![coverage_initial_fun2.png](coverage_initial_fun2.png)

Improvement: 100% branch coverage

![coverage_after_fun2.png](coverage_after_fun2.png)

### Overall

Initial: 84% _line_ coverage on `_enum.py`

![coverage_initial.png](coverage_initial.png)

Improvement: 85% _line_ coverage on `_enum.py`

![coverage_after.png](coverage_after.png)
