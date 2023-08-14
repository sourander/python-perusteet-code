from mypy import api
from tests.conftest import PACKAGE_NAME

def test_mypy():

    normal_msg, error_msg, exit_status= api.run([PACKAGE_NAME])

    assert not exit_status, normal_msg