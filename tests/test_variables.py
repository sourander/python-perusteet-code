import pytest
import importlib.util

from tests.conftest import PACKAGE_NAME as PN
from tests.conftest import skip_if_file_missing


def test_variables():
    try:
        variables = importlib.import_module(f"{PN}.variables")
    except ModuleNotFoundError:
        pytest.skip(
            f"Skipping test_variable_types because "
            f"you have not yet created {PN}/variables.py"
        )

    names = [
        ("my_integer", int),
        ("my_float", float),
        ("my_string", str),
        ("my_boolean", bool),
        ("my_list", list),
        ("my_tuple", tuple),
        ("my_dict", dict),
        ("my_bytes", bytes),
    ]

    for (n, t) in names:
        var = getattr(variables, n)
        assert isinstance(var, t), f"The variable {n} is of wrong type!"
        if not var:
            raise ValueError(f"A variable {n} should have a non-empty value!")
