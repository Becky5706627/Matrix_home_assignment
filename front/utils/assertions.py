from typing import Any, Optional


class AssertionHandler:

    @staticmethod
    def assert_equal(actual: Any, expected: Any, message: Optional[str] = None) -> None:
        if message is None:
            message = f"Expected {expected}, but got {actual}."
        assert actual == expected, message

    @staticmethod
    def assert_true(condition: bool, message: Optional[str] = None):
        if message is None:
            message = f"Expected condition to be True, but it was not. condition: {condition}"
        assert condition, message
