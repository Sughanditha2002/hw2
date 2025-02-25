import pytest
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.commands.menu import MenuCommand


def test_add_command():
    add_command = AddCommand(3, 5)
    assert add_command.execute() == 8


def test_subtract_command():
    subtract_command = SubtractCommand(10, 4)
    assert subtract_command.execute() == 6


def test_multiply_command():
    multiply_command = MultiplyCommand(6, 7)
    assert multiply_command.execute() == 42


def test_divide_command():
    divide_command = DivideCommand(20, 5)
    assert divide_command.execute() == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_command = DivideCommand(10, 0)
        divide_command.execute()


def test_menu_command(capsys):
    
    menu_command = MenuCommand()
    
   
    menu_command.execute()
    
    
    captured = capsys.readouterr()
    
    assert captured.out == "Menu\n"