import random

import pytest

from app.domain.exceptions.values.numbers import NonNegativeIntLTZeroException
from app.domain.values.numbers import NonNegativeInt


def test_create_non_negative_int_success():
    value = random.randint(0, 100)
    number = NonNegativeInt(value)

    assert number.value_to_generic_type == value


def test_create_non_negative_int_with_negative_value():
    with pytest.raises(NonNegativeIntLTZeroException):
        value = random.randint(-100, -1)
        NonNegativeInt(value)
