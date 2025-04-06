import pytest
from logic.snack_machine import SnackMachine

@pytest.fixture
def snack_machine():
    """Fixture to create a SnackMachine instance."""
    return SnackMachine()

def test_initial_state(snack_machine):
    """Test that the initial state of the SnackMachine is correct."""
    assert snack_machine.one_cent_count == 0
    assert snack_machine.ten_cent_count == 0
    assert snack_machine.quarter_count == 0
    assert snack_machine.one_dollar_count == 0
    assert snack_machine.five_dollar_count == 0
    assert snack_machine.twenty_dollar_count == 0

def test_insert_money(snack_machine):
    """Test the insert_money method to ensure money is correctly added."""
    snack_machine.insert_money(1, 2, 3, 4, 5, 6)

    assert snack_machine.one_cent_count == 1
    assert snack_machine.ten_cent_count == 2
    assert snack_machine.quarter_count == 3
    assert snack_machine.one_dollar_count == 4
    assert snack_machine.five_dollar_count == 5
    assert snack_machine.twenty_dollar_count == 6

def test_insert_multiple_times(snack_machine):
    """Test inserting money multiple times."""
    snack_machine.insert_money(1, 0, 0, 0, 0, 0)
    snack_machine.insert_money(0, 1, 0, 0, 0, 0)
    
    assert snack_machine.one_cent_count == 1
    assert snack_machine.ten_cent_count == 1
    assert snack_machine.quarter_count == 0
    assert snack_machine.one_dollar_count == 0
    assert snack_machine.five_dollar_count == 0
    assert snack_machine.twenty_dollar_count == 0

def test_insert_large_amounts(snack_machine):
    """Test inserting large amounts of money."""
    snack_machine.insert_money(1000, 1000, 1000, 1000, 1000, 1000)
    
    assert snack_machine.one_cent_count == 1000
    assert snack_machine.ten_cent_count == 1000
    assert snack_machine.quarter_count == 1000
    assert snack_machine.one_dollar_count == 1000
    assert snack_machine.five_dollar_count == 1000
    assert snack_machine.twenty_dollar_count == 1000
