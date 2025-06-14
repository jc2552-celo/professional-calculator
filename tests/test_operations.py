import pytest
from app.operation import operations

@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0)])
def test_add(a, b, expected):
    assert operations.add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [(4, 2, 2), (10, 5, 2)])
def test_divide(a, b, expected):
    assert operations.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        operations.divide(1, 0)
