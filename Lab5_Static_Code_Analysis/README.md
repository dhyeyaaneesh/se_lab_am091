# Lab 5 – Static Code Analysis

This folder contains the assigned address-book program, a cleaned version, the issue log, reflection answers, and a script to generate before/after reports.

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py generate_reports.py
py address_book.py
```

If PowerShell blocks virtual-environment activation, run the tools without activating it using `py -m pip install -r requirements.txt` and `py generate_reports.py`.

The report generator writes:

- `reports/before/pylint_report.txt`
- `reports/before/bandit_report.txt`
- `reports/before/flake8_report.txt`
- `reports/after/pylint_report.txt`
- `reports/after/bandit_report.txt`
- `reports/after/flake8_report.txt`

Review the generated reports and check that the final Pylint score is above 9.5, Bandit findings are addressed, and Flake8 reports no remaining formatting errors. Tool versions can affect exact wording and scores.

## Files

- `address_book_before.py`: original assigned program, retained for comparison.
- `address_book.py`: revised program.
- `issues.md`: issue table and fixes.
- `reflection.md`: four reflection responses.
- `generate_reports.py`: creates the six report files using the installed tools.
