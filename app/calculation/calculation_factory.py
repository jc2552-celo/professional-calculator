from app.operation import operations

class CalculationFactory:
    @staticmethod
    def create(op, a, b):
        if op == "add":
            return operations.add(a, b)
        elif op == "subtract":
            return operations.subtract(a, b)
        elif op == "multiply":
            return operations.multiply(a, b)
        elif op == "divide":
            return operations.divide(a, b)
        else:
            raise ValueError("Invalid operation.")
