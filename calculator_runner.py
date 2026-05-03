from simple_calculator import SimpleCalculator
class CalculatorRunner(SimpleCalculator):
    def __init__(self):
        super().__init__()
        self.stored_value = None

    def run(self):
        print("=== Simple Calculator ===")
        while True:
            try:
                if self.stored_value is not None:
                    choice = input("Use stored value as first number? [y/n]: ").strip().lower()
                    num_1 = self.stored_value if choice == "y" else float(input("Enter first number: "))
                else:
                    num_1 = float(input("Enter first number: "))

                num_2 = float(input("Enter second number: "))
                operation = input("Choose operation (+, -, *, /): ").strip()

                result = self.calculate(num_1, num_2, operation)
                print(f"Result = {result}")