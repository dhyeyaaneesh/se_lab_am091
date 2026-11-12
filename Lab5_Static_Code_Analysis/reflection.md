# Lab 5 – Reflection

> The supplied three-page handout explains that a reflection is required but does not include the four reflection questions themselves. The responses below address four relevant reflection prompts; adjust the headings if your instructor provided a separate question sheet.

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without running the program. It helps identify potential bugs, insecure coding practices, and style problems early. This makes code easier to maintain and reduces the chance that avoidable issues reach users.

## 2. What is the difference between Pylint, Flake8, and Bandit?

Pylint checks broader code quality, including naming, unused code, documentation, and possible logical problems. Flake8 focuses mainly on Python style and formatting rules. Bandit scans Python code for common security risks, such as unsafe deserialization and weak cryptographic choices. They complement one another because they focus on different kinds of problems.

## 3. Which issues were most important, and how were they fixed?

The most important issue was restoring backups with `pickle.load()`, because loading an untrusted pickle file can execute malicious code. I replaced the pickle backup with JSON. I also removed a hard-coded credential-like value, replaced MD5 with SHA-256, and removed a broad exception handler by checking whether the contact exists before updating it. Style improvements included snake_case names, explicit UTF-8 encoding, and a main guard.

## 4. What did you learn from using static analysis tools?

I learned that code can appear to work while still containing security, reliability, and maintainability problems. Running multiple tools gives a more complete review than relying on program output alone. The tools identify potential issues, but the developer still needs to understand each warning, decide whether it applies, make a suitable change, and rerun the checks to verify the result.
