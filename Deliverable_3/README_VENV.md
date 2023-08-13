# Using Virtual Environments and Requirements

Virtual environments allow isolated execution of a project under specific conditions, usually libraries or packages with specific versions.

## Instructions to Install a Virtual Environment

### Windows

1. Open the command prompt or PowerShell.
2. Navigate to your project directory using the command `cd project/path`.
3. Create a new virtual environment using the following command:

python -m venv environment_name

4. Activate the virtual environment:

environment_name\Scripts\activate

Also if you have Linux you can do this:


### Linux

1. Open a terminal.
2. Navigate to your project directory using the command `cd project/path`.
3. Create a new virtual environment using the following command:

python3 -m venv environment_name

4. Activate the virtual environment:

source environment_name/bin/activate


## requirements.txt File

The `requirements.txt` file contains a list of packages and their versions that are necessary to run the notebook.

To install the packages in your virtual environment, run the following command after activating your environment:

pip install -r requirements.txt


Remember to update this file each time you add or modify packages in your project.

---

This document is part of a deliverable and provides instructions for creating and using virtual environments, as well as installing required packages using `requirements.txt`.
[Title](requirements.txt)




## Using Tox and Poetry for Managing Virtual Environments and Testing

Tox and Poetry are powerful tools that help manage virtual environments, test code with various Python versions, and handle dependencies effectively.

## Setting Up Tox and Poetry

1. **Install Tox and Poetry:**

   Make sure you have both Tox and Poetry installed globally on your system:

   ```bash
   pip install tox poetry

Create a pyproject.toml File:

In your project directory, create a pyproject.toml file if you don't already have one. This is where Poetry will manage your project's dependencies.

# Using Tox for Testing
1.Create a tox.ini File:

Create a tox.ini file in your project directory. This file defines the test environments and configurations.

[tox]
envlist = py36, py37, py38

[testenv]
deps =
    poetry
commands =
    poetry install -v
    poetry run pytest

2.Run Tests with Tox:

Open a terminal and navigate to your project directory. Run the following command to execute tests with different Python versions:

tox

Tox will create virtual environments for each specified Python version and run your tests.