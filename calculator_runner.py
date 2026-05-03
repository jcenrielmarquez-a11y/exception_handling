from simple_calculator import SimpleCalculator
class CalculatorRunner(SimpleCalculator):
    def __init__(self):
        super().__init__()
        self.stored_value = None