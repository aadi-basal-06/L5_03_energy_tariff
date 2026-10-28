# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program. It helps identify potential programming errors, security vulnerabilities, and style violations early in development. This makes it easier to detect problems before the software is deployed and improves code quality and maintainability.

## 2. What are the differences between Pylint, Bandit, and Flake8?

Pylint focuses on code quality, naming conventions, documentation, possible programming errors, and maintainability.

Bandit examines Python source code for common security problems. In this lab, it identified the use of eval(), which can execute arbitrary Python expressions.

Flake8 checks Python style and reports problems such as incorrect spacing, excessive line length, and unused imports.

Using all three tools provides complementary checks because each tool focuses on different aspects of the code.

## 3. What issues did you identify and how did you fix them?

The original code used a mutable default list in record_reading(), which could cause reading history to persist unexpectedly across calls. I changed the default to None and initialized the history safely.

Bandit identified eval() as a medium-severity security finding. I replaced it with float conversion and input validation so the program accepts numeric readings without evaluating arbitrary Python expressions.

I also replaced bare exception handling with specific exceptions, used context managers and UTF-8 encoding for file operations, added docstrings, and corrected formatting violations.

Additionally, I added validation to reject negative readings because negative electricity consumption is not meaningful for this application.

## 4. How did static analysis improve the program, and what are its limitations?

Static analysis helped identify security risks, code quality problems, and style violations without requiring the program to be executed. Comparing the before and after reports provides evidence of which findings were addressed.

However, a clean static analysis report does not guarantee that a program is completely correct or secure. Static analysis may miss logical errors and unexpected runtime behaviour. For that reason, I also compiled and ran the program and tested the tariff calculations and input validation.
