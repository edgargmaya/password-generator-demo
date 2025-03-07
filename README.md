# Password Generator Demo

This project demonstrates how to build a **Python module** that:

- Generates random passwords with various parameters (functions in `password_generator/generator.py`).
- Allows running unit and integration tests.
- Includes linting with `pylint` and security analysis with `bandit`.
- Is published to a private repository using GitHub Actions.

## Structure

- `password_generator/` contains the source code (main module).
- `tests/` contains the unit and integration tests.
- `setup.py` and `requirements.txt` manage installation and dependencies.
- `.github/workflows/` contains the GitHub Actions configuration files.

## Usage

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```