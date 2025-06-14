# 🧮 Professional Calculator CLI (Python)

This is a modular, command-line calculator application written in Python. It supports basic arithmetic operations in an interactive REPL interface, includes robust error handling, and maintains a history of calculations. It also features 100% automated testing with GitHub Actions integration.

## 🚀 Features

- ✅ REPL (Read-Eval-Print Loop) command-line interface
- ➕ Supports: `add`, `subtract`, `multiply`, `divide`
- 🧠 Input validation and division-by-zero handling
- 🗂️ Tracks calculation history per session
- 🔁 Special commands: `help`, `history`, `exit`
- ✅ Unit + parameterized tests with `pytest`
- 🧪 Integrated CI with GitHub Actions and test coverage checks

## 🛠️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/jc2552-celo/professional-calculator.git
cd professional-calculator

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

## ▶️ How to Use

After activating your virtual environment and installing dependencies:

```bash
python main.py

You will be prompted to enter an operation and numbers. Example:
Enter operation or command: add
First number: 5
Second number: 3
Result: 8.0

Available commands: add, subtract, multiply, divide, history, help, exit

🧪 Running Tests with Coverage
bash
Copy code
PYTHONPATH=. pytest --cov=app tests/

📦 Project Structure
app/
├── calculator/         # REPL logic
├── calculation/        # Factory for operation execution
├── operation/          # Arithmetic functions
tests/                  # Unit and parameterized test cases
main.py                 # Entry point for the calculator

✅ GitHub Actions
This project includes CI configuration to:

Automatically run all tests on every push

Enforce minimum test coverage (--fail-under=38)

