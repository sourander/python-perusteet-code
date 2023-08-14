from tests.conftest import skip_if_file_missing
from tests.conftest import PACKAGE_NAME as PN

@skip_if_file_missing(f"{PN}.strings", attr_name="count_vowels")
def test_count_vowels(attr):
    assert attr("") == 0

    assert attr("aeiouyäö" + "aeiouyäö".upper()) == 16

    assert attr("aeiouAEIOU") == 10

    assert attr("Hello World!") == 3

    assert attr("AaEeIiOoUu") == 10
