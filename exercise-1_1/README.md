# Python Addition Program

**This repository contains the deliverables for Exercise 1.1 of the "Python for Web Developers" specialization course.**

This exercise covers setting up Python, creating virtual environments, writing a simple Python script, managing dependencies, and documenting your work.

---

This is a simple Python program that prompts the user to enter two numbers and prints their sum.

## Files

- `add.py`: Main script that asks for two numbers and prints their sum.
- `requirements.txt`: Lists Python packages required for the environment (mainly for development or if using IPython, not strictly needed for running `add.py`).

## Setup

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone <your-repo-url>
   cd exercise-1_1
   ```

2. **(Optional) Create a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies** (if you want to use the development environment):

   ```bash
   pip install -r requirements.txt
   ```

   > Note: The `add.py` script itself does not require any external packages.

## Usage

Run the script with Python:

```bash
python add.py
```

You will be prompted to enter two numbers. The program will then print their sum.

## Example

```
Enter first number: 5
Enter second number: 7
12
```

## Notes

- The `env/` directory contains the Python virtual environment and can be ignored.
- The `.gitignore` file in `env/` ensures environment files are not tracked by git.
