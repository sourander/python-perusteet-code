from string import ascii_letters
from tests.conftest import skip_if_file_missing
from tests.conftest import PACKAGE_NAME as PN
from tests.conftest import count_type_hints


@skip_if_file_missing(f"{PN}.strings", attr_name="is_a_in_b")
def test_generate_zip_name(attr):
    assert attr("kar hu", "Oho, KAR HU!") == True
    assert attr("aaa", "bbb") == False
    assert attr("", "Non empty string") == False
    assert count_type_hints(attr) >= 3

@skip_if_file_missing(f"{PN}.strings", attr_name="generate_zip_name")
def test_generate_zip_name(attr):
    assert attr("myApp", "1.0", "x86_64", "zip") == "myApp-1.0-x86_64.zip"
    assert count_type_hints(attr) >= 5

@skip_if_file_missing(f"{PN}.strings", attr_name="count_vowels")
def test_count_vowels(attr):
    assert attr("") == 0
    assert attr("aeiouAEIOU") == 10
    assert attr("aeiouyäö" + "aeiouyäö".upper()) == 16
    assert attr("? H e l l o W o r l d !") == 3
    assert attr(ascii_letters) == 12
    assert count_type_hints(attr) >= 2

@skip_if_file_missing(f"{PN}.strings", attr_name="is_palindrome")
def test_is_palindrome(attr):
    assert attr("") == False
    assert attr("!!!!!") == False
    assert attr("ÖäÖ") == True
    assert attr("Ope, hikkaako kaakkihepo?!") == True
    assert attr("Ei hikkaa!") == False
    assert count_type_hints(attr) >= 2