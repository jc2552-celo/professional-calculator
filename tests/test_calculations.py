import pytest
from app.calculation.calculation_factory import CalculationFactory

def test_create_add():
    assert CalculationFactory.create("add", 2, 3) == 5

def test_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("mod", 1, 2)
