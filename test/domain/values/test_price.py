import pytest
from faker.proxy import Faker

from app.domain.exceptions.values.numbers import PriceLEZeroException
from app.domain.values.numbers import Price


def test_create_price_success(faker: Faker):
    value = faker.pydecimal(min_value=1, right_digits=2)
    price = Price(value)

    assert price.value_to_generic_type == value


def test_create_price_le_zero(faker: Faker):
    with pytest.raises(PriceLEZeroException):
        value = faker.pydecimal(max_value=0, right_digits=2)
        Price(value)
