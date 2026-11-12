# Static Analysis Issue Log

The line numbers below refer to the original `address_book_before.py` supplied in the assigned repository. Severity is based on the risk and impact of each finding; tool wording can vary by installed version.

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Unsafe pickle deserialization | Security (high) | 62–63 | `pickle.load()` can execute attacker-controlled code if a backup file is malicious. | Replaced pickle with JSON serialization/deserialization and checked that the restored top-level value is a dictionary. |
| Hard-coded credential-like value | Security / maintainability | 5 | `SYNC_PASSWORD` contains a literal password and is not used by the program. | Removed the unused hard-coded value. A real credential should be supplied securely and only if authentication is actually required. |
| Weak MD5 hash | Security | 18 | MD5 is an obsolete hash algorithm and can trigger Bandit weak-hash findings. | Replaced MD5 with SHA-256 for the deterministic contact identifier. The identifier is not used for password storage. |
| Overly broad exception | Bug / reliability | 32–33 | `except Exception` hides unrelated programming and runtime errors. | Replaced exception-based flow with an explicit membership check before updating a city. |
| Non-PEP 8 naming | Style / maintainability | 9–61 | CamelCase function names make the code inconsistent with Python conventions. | Renamed functions and parameters to snake_case. |
| Missing file encoding | Reliability | 50, 57, 62 | Text files use the platform's default encoding. | Added explicit UTF-8 encoding to CSV and JSON file operations. |
| Weak directory iteration style | Style | 46–47 | Indexing a range is less readable than iterating with `enumerate`. | Used `enumerate(..., start=1)` to print numbered entries. |
| Unprotected module execution | Maintainability | 82 | Importing the module runs the demo and creates files immediately. | Added the `if __name__ == "__main__":` entry-point guard. |

## Verification note

Run `python generate_reports.py` after installing the packages in `requirements.txt`. The script creates the genuine Pylint, Bandit, and Flake8 reports for both the original and cleaned files under `reports/before/` and `reports/after/`. Do not treat a report as clean until the generated output has been checked.
