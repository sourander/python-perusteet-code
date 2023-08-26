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