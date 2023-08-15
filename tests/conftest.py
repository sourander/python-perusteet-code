import pytest
import importlib.util
import os

from dataclasses import dataclass
from typing import Callable

# Static, to be used in all tests
PACKAGE_NAME = os.getenv("PACKAGE_NAME") or "tasks"


@dataclass
class Package:
    module_path: str
    attr_name: str | None


def skip_if_file_missing(
    module_path: str, attr_name: str) -> any:
    """Decorator function with arguments:
    * Skips the pytest if module is not found
    * Skips the pytest if attr_name is wanted but not found

    Args:
        module_path (str): 
            The path of the package as you would use it in
            an import statement.
        attr_name (str): 
            The attribute we are trying to fetch.

    Example usage:
        @skip_if_file_missing("egg.ham.spam", "some_bool")
        def test_something(attr):
            assert attr == True

        The returned attr is essentially the same as:
        def f():
            from egg.ham.spam import some_bool as attr
            return attr
    """

    def decorator(test_func: callable):
        def wrapper(*args, **kwargs):
            # Init Package
            package = Package(module_path, attr_name)

            try:
                # Load module
                module = importlib.import_module(package.module_path)

                # Find the attribute (e.g. function) from the module
                func = getattr(module, attr_name)

            except ModuleNotFoundError:
                pytest.skip(
                    f"Skipping {test_func.__name__} because "
                    f"module '{package.module_path}' not found."
                )
            except AttributeError:
                pytest.skip(
                    f"Skipping {test_func.__name__} because "
                    f"attribute '{attr_name}' not found'"
                )

            return test_func(func, *args, **kwargs)

        return wrapper

    return decorator


def count_type_hints(f:Callable) -> int:
    return len(f.__annotations__.keys())