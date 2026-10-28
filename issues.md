# Lab 5: Static Code Analysis — Issue Documentation

## Issue Table

| Issue | Type | Line(s) Before Fix | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe evaluation with eval | Security — Medium | 63 | Bandit B307 identified eval as potentially insecure because it can execute arbitrary Python expressions. | Replaced eval with float conversion and numeric input validation. |
| Mutable default argument | Bug / Code quality | 12 | The default history list was shared between calls, allowing unexpected state to persist. | Changed the default to None and initialized the history safely. |
| Bare exception handler | Code quality / Reliability | 44 | The broad exception handler could hide unrelated programming errors. | Replaced it with specific exception handling and an informative error. |
| Missing file encoding and context managers | Code quality / Reliability | 42, 48 | File operations omitted explicit encodings and did not consistently manage resources safely. | Used UTF-8 and with statements. |
| Missing documentation | Maintainability | Multiple | The module and functions lacked docstrings. | Added module and function docstrings. |
| Global statements | Maintainability | 27, 40 | Functions reassigned global state directly. | Updated the existing rate list in place and updated meter data without rebinding the dictionary. |
| Negative meter readings | Functional correctness | 56, 63 | Negative units could reduce accumulated consumption and produce misleading bills. | Added non-negative reading validation and corrected the demonstration input. |
| Flake8 formatting violations | Style | Multiple | The original file had spacing, line-length, and unused-import violations. | Removed the unused import and reformatted the code. |

## Report Summary

Record the actual measurements from the generated reports:

- Initial Pylint score: 6.14/10
- Final Pylint score: [Fill in from reports/after/pylint_report.txt]
- Initial Bandit findings: 1 medium-severity finding
- Final Bandit findings: [Fill in from reports/after/bandit_report.txt]
- Initial Flake8 violations: 12 reported violations
- Final Flake8 violations: [Fill in from reports/after/flake8_report.txt]
