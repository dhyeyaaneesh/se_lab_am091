# Lab 6 – Code and Branch Coverage Analysis

Student: PES1UG24AM091

## Files
- `traffic_fine.py`: assigned application module.
- `CodeCoverageTest_PES1UG24AM091_application.py`: tests for line/code coverage.
- `BranchCoverageTest_PES1UG24AM091_application.py`: tests for decision branches.

## Install (Windows CMD)
```cmd
py -m pip install -r requirements.txt
```

## Stage 1 – Code coverage
```cmd
coverage erase
coverage run --source=traffic_fine -m pytest -q CodeCoverageTest_PES1UG24AM091_application.py
coverage report -m
```
Take a terminal screenshot showing passing tests and the coverage percentage. Save it as `code_coverage.png`. Commit the code coverage test file separately.

## Stage 2 – Branch coverage
```cmd
coverage erase
coverage run --branch --source=traffic_fine -m pytest -q BranchCoverageTest_PES1UG24AM091_application.py
coverage report -m
```
Take a terminal screenshot showing passing tests and the branch coverage percentage. Save it as `branch_coverage.png`. Commit the branch coverage test file separately.

`--source=traffic_fine` measures the assigned application rather than the test files.
