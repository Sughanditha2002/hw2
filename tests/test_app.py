import pytest
from app.commands import CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand


def test_register_and_execute_multiply_command(capsys):
    handler = CommandHandler()
    multiply_command = MultiplyCommand(6, 7)

    
    handler.register_command("multiply", multiply_command)

    
    result = handler.execute_command("multiply")

    
    captured = capsys.readouterr()

    
    assert captured.out == "MultiplyCommand: 6 * 7 = 42\n"
    assert result == 42

def test_register_and_execute_divide_command(capsys):
    handler = CommandHandler()
    divide_command = DivideCommand(10, 2)

    
    handler.register_command("divide", divide_command)

    
    result = handler.execute_command("divide")

    
    captured = capsys.readouterr()

    
    assert captured.out == "DivideCommand: 10 / 2 = 5.0\n"
    assert result == 5.0

def test_divide_by_zero():
    handler = CommandHandler()
    divide_command = DivideCommand(10, 0)

    
    handler.register_command("divide_zero", divide_command)

    
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        handler.execute_command("divide_zero")

def test_register_and_execute_add_command(capsys):
    handler = CommandHandler()
    add_command = AddCommand(2, 3)

    
    handler.register_command("add", add_command)

    
    result = handler.execute_command("add")

    
    captured = capsys.readouterr()

    
    assert captured.out == "AddCommand: 2 + 3 = 5\n"
    assert result == 5

def test_register_and_execute_subtract_command(capsys):
    handler = CommandHandler()
    subtract_command = SubtractCommand(5, 2)

    
    handler.register_command("subtract", subtract_command)

    
    result = handler.execute_command("subtract")

    
    captured = capsys.readouterr()

   
    assert captured.out == "SubtractCommand: 5 - 2 = 3\n"
    assert result == 3

def test_execute_nonexistent_command():
    handler = CommandHandler()

    
    result = handler.execute_command("nonexistent")

    
    assert result is None