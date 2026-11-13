# Lab 7 – Fuzz Testing for Input Validation Bugs

Student: PES1UG24AM091

## Important naming note
The handout uses the generic names `processor.py` and `test_processor.py`.
The assigned GitHub Lab 7 repository actually supplies `traffic_fine.py` and
`test_traffic_fine.py`, so this submission retains the repository's filenames
and tests its three actual functions: `parse_ticket_id`, `total_fines`, and
`speed_excess`.

## Files
- `traffic_fine.py`: original buggy application for the initial failing run.
- `test_traffic_fine.py`: completed Hypothesis tests.
- `before/traffic_fine.py`: untouched copy of the original application.
- `fixed/traffic_fine.py`: hardened implementation to copy over after recording failures.
- `requirements.txt`: Hypothesis and pytest dependencies.
- `screenshots/`: save your own required terminal screenshots here.

## Install (Windows CMD)
```cmd
py -m pip install -r requirements.txt
```

## Step 1 – Run the original application
```cmd
py traffic_fine.py
```
Enter sample values when prompted, for example:
- `TF-2024-0456`
- `500,1200,300`
- `72/60`

Take a screenshot of the original application output. Save it as
`screenshots/original_output.png`.

## Step 2 – Run the completed Hypothesis tests against the original code
```cmd
py -m pytest -q test_traffic_fine.py
```
The original implementation is expected to fail some fuzz/property tests.
Capture the failing test output and save it as `screenshots/failing_tests.png`.
Do not copy the fixed file over until this screenshot is taken.

## Step 3 – Apply the fixes
From inside the `Lab-7` directory:
```cmd
copy /Y fixed\traffic_fine.py traffic_fine.py
```

## Step 4 – Run the fixed application
```cmd
py traffic_fine.py
```
Use the same sample inputs. Capture the successful application output as
`screenshots/fixed_output.png`.

## Step 5 – Rerun the Hypothesis tests
```cmd
py -m pytest -q test_traffic_fine.py
```
All tests should pass. Capture the passing output as
`screenshots/passing_tests.png`.

## What the fixes validate
- Ticket IDs must follow PREFIX-YYYY-SERIAL.
- Fine amounts must be non-negative integers; empty or malformed CSV values are rejected.
- Fine totals are capped at 10000.
- Speed readings must follow speed/limit, contain non-negative integers, and have a positive limit.
- Invalid inputs raise a clear ValueError instead of leaking TypeError, IndexError, or ZeroDivisionError.

## Submission
Submit the fixed `traffic_fine.py`, updated `test_traffic_fine.py`, and a PDF
containing the screenshots required by the lab handout.
