
import pytest

""" If the value of any variable is in not in range, then creating custom error"""

class NotInRange(Exception):
    def __init__(self, message = "Given Value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 4
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
    