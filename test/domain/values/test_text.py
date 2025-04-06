import pytest
from faker import Faker

from app.domain.exceptions.values.texts import EmptyTextException, TextTooLongException
from app.domain.values.texts import Text


def test_create_text_success(faker: Faker):
    value = faker.text(max_nb_chars=100)
    text = Text(value)

    assert text.value_to_generic_type == value


def test_create_empty_text():
    with pytest.raises(EmptyTextException):
        value = ""
        Text(value)


def test_create_too_long_text(faker: Faker):
    with pytest.raises(TextTooLongException):
        value = faker.text(max_nb_chars=500)
        Text(value)
