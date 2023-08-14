# Import the function to be tested
from tasks.helloworld import hello_world

def test_hello_world():
    expected_output = "Hello World!"
    result = hello_world()
    assert result == expected_output