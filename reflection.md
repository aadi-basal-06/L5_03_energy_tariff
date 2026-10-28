# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis?

Static code analysis examines source code without executing it. It helps identify potential programming errors, security vulnerabilities, and style violations before deployment.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint checks code quality, documentation, naming, and potential programming errors. Bandit identifies common security vulnerabilities in Python. Flake8 checks formatting, style, and certain programming errors. Using all three provides complementary checks.

## 3. What issues were identified and fixed?

The original program contained unsafe eval() usage, a mutable default argument, broad exception handling, missing file encodings, missing documentation, and style violations. The revised program replaces eval() with numeric conversion, validates meter readings, uses context managers, handles specific exceptions, and improves documentation and formatting.

## 4. How did static analysis improve the program, and what are its limitations?

Static analysis helped identify security, quality, and style problems without executing the code. Pylint improved from 6.14/10 to 10.00/10, Bandit reported no remaining issues, and Flake8 reported no remaining violations. However, clean static analysis reports do not guarantee functional correctness, so the tariff calculations and input validation also need testing.
