import pytest
from faker import Faker

from app.domain.exceptions.values.texts import EmptyNameException, NameTooLongException
from app.domain.values.texts import Name


def test_create_name_success(faker: Faker):
    value = faker.text(max_nb_chars=10)
    name = Name(value)

    assert name.value_to_generic_type == value


def test_create_empty_name():
    with pytest.raises(EmptyNameException):
        value = ""
        Name(value)


def test_create_too_long_name(faker: Faker):
    with pytest.raises(NameTooLongException):
        value = faker.text(max_nb_chars=500)
        Name(value)
