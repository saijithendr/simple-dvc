
import pytest


class NotInRange(Exception):
    def __init__(self, message='value is not in range'):
        self.message = message
        super().__init__(self.message)

def test_genric():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10,20):
            raise NotInRange
