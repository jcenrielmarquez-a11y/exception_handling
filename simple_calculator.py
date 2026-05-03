class SimpleCalculator:
    def calculate(self, num_1, num_2, operation):
        if operation == "+":
            return num_1 + num_2
        elif operation == "-":
            return num_1 - num_2
        elif operation == "*":
            return num_1 * num_2
        elif operation == "/":
            if num_2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return num_1 / num_2
        else:
            raise ValueError("Invalid operation. Please use +, -, *, or /.")
      