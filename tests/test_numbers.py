import pytest

from tests.conftest import skip_if_file_missing
from tests.conftest import PACKAGE_NAME as PN
from tests.conftest import count_type_hints


@skip_if_file_missing(f"{PN}.numbers", attr_name="celsius_to_fahrenheit")
def test_celsius_to_fahrenheit(attr):
    assert attr(0) == 32
    assert attr(100) == 212
    assert attr(-40) == -40
    assert attr(37) == 98.6
    assert count_type_hints(attr) >= 2

@skip_if_file_missing(f"{PN}.numbers", attr_name="divisible_with_all")
def test_divisible_with_all(attr):
    assert attr(10, 2, 5) == True
    assert attr(10, 2, 3) == False
    assert attr(10, 3, 5) == False
    assert attr(10, 1, 10) == True

@skip_if_file_missing(f"{PN}.numbers", attr_name="divisible_with_all")
def test_divisible_with_all_raises(attr):
    with pytest.raises(TypeError) as excinfo:  
        attr(1, 1, "kissa", 4)

@skip_if_file_missing(f"{PN}.numbers", attr_name="collatz")
def test_collatz(attr):
    assert attr(1) == [1]
    assert attr(2) == [2, 1]
    assert attr(3) == [3, 10, 5, 16, 8, 4, 2, 1]
    assert attr(4) == [4, 2, 1]
    assert attr(5) == [5, 16, 8, 4, 2, 1]
    assert attr(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]