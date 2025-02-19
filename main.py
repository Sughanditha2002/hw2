from abc import ABC, abstractmethod

# Define the Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Define individual command classes for each operation
class AddCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return f"The result of {self.a} add {self.b} is equal to {self.a + self.b}"

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return f"The result of {self.a} subtract {self.b} is equal to {self.a - self.b}"

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        return f"The result of {self.a} multiply {self.b} is equal to {self.a * self.b}"

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def execute(self):
        if self.b == 0:
            return "An error occurred: Cannot divide by zero"
        return f"The result of {self.a} divide {self.b} is equal to {self.a / self.b}"

# MenuCommand to display the available operations
class MenuCommand(Command):
    def execute(self):
        return "Available operations: add, subtract, multiply, divide, menu"

# CommandHandler to manage the operations
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, operation, command):
        self.commands[operation] = command

    def execute_command(self, operation):
        if operation in self.commands:
            return self.commands[operation].execute()
        else:
            return "Unknown operation."

# Perform calculation based on input
def perform_calculation(a_string, b_string, operation_string):
    handler = CommandHandler()

    # Try converting inputs to integers and handling invalid inputs
    try:
        a = int(a_string)
        b = int(b_string)
    except ValueError:
        return f"Invalid number input: {a_string} or {b_string} is not a valid number."

    # Register and execute commands based on the operation
    if operation_string == 'add':
        handler.register_command('add', AddCommand(a, b))
    elif operation_string == 'subtract':
        handler.register_command('subtract', SubtractCommand(a, b))
    elif operation_string == 'multiply':
        handler.register_command('multiply', MultiplyCommand(a, b))
    elif operation_string == 'divide':
        handler.register_command('divide', DivideCommand(a, b))
    else:
        return f"Unknown operation: {operation_string}"

    result = handler.execute_command(operation_string)
    return result
