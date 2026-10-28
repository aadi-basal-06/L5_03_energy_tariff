# Lab 5: Static Code Analysis — Issue Documentation

| Issue | Type | Original Location | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe eval() | Security — Medium | Line 63 | Bandit B307 identified potentially unsafe expression evaluation. | Replaced eval() with float conversion. |
| Mutable default argument | Code quality | Line 12 | A shared default list could retain state between function calls. | Used None and initialized the list safely. |
| Bare exception handler | Code quality | Line 44 | A bare except could hide unrelated errors. | Used specific exception handling. |
| Missing file encoding | Reliability | Lines 42, 48 | File operations did not specify encoding or consistently manage resources. | Used UTF-8 and context managers. |
| Missing docstrings | Maintainability | Multiple | Module and functions lacked documentation. | Added docstrings. |
| Global statements | Maintainability | Lines 27, 40 | Functions modified global state directly. | Updated existing mutable objects in place. |
| Negative meter readings | Functional correctness | Multiple | Negative consumption could produce invalid totals. | Added input validation. |
| Formatting violations | Style | Multiple | Flake8 identified spacing, line-length, and unused-import issues. | Corrected formatting and removed unused imports. |

## Analysis Results

| Tool | Before | After |
|---|---|---|
| Pylint | 6.14/10 | 10.00/10 |
| Bandit | 1 medium-severity finding | 0 findings |
| Flake8 | 12 violations | 0 violations |
