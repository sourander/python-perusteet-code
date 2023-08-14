from string import ascii_letters
from tests.conftest import skip_if_file_missing
from tests.conftest import PACKAGE_NAME as PN

@skip_if_file_missing(f"{PN}.strings", attr_name="count_vowels")
def test_count_vowels(attr):
    assert attr("") == 0
    assert attr("aeiouAEIOU") == 10
    assert attr("aeiouyäö" + "aeiouyäö".upper()) == 16
    assert attr("? H e l l o W o r l d !") == 3
    assert attr(ascii_letters) == 12

@skip_if_file_missing(f"{PN}.strings", attr_name="is_palindrome")
def test_is_palindrome(attr):
    assert attr("") == False
    assert attr("Ope, hikkaako kaakkihepo?!") == True
    assert attr("Ei hikkaa!") == False