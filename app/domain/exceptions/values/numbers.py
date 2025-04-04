from dataclasses import dataclass

from app.domain.exceptions.values.base import BaseValueObjectException


@dataclass
class NumberValueException(BaseValueObjectException):
    @property
    def message(self) -> str:
        return "Ошибка численного значения!"


@dataclass
class PositiveIntLTZeroException(NumberValueException):
    @property
    def message(self) -> str:
        return "Неотрицательные число не может быть меньше нуля!"


@dataclass
class PriceLEZeroException(NumberValueException):
    @property
    def message(self) -> str:
        return "Цена на товар должна быть больше нуля!"
