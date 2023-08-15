# Import the function to be tested
from tasks.helloworld import hello_world
from conftest import count_type_hints

def test_hello_world():
    expected_output = "Hello World!"
    result = hello_world()
    assert result == expected_output
    assert count_type_hints(hello_world) == 1