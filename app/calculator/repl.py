from app.calculation.calculation_factory import CalculationFactory

history = []

def run_repl():
    print("Welcome to Professional Calculator! Type 'help' for commands.")
    while True:
        command = input("Enter operation or command: ").strip().lower()
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "help":
            print("Supported: add, subtract, multiply, divide, history, exit")
        elif command == "history":
            for item in history:
                print(item)
        elif command in ["add", "subtract", "multiply", "divide"]:
            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                result = CalculationFactory.create(command, a, b)
                print("Result:", result)
                history.append(f"{command}({a}, {b}) = {result}")
            except ValueError as e:
                print("Error:", e)
        else:
            print("Unknown command. Type 'help' for available options.")
