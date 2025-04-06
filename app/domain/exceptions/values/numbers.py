from dataclasses import dataclass

from app.domain.exceptions.values.base import BaseValueObjectException


@dataclass(frozen=True, eq=False)
class NumberValueException(BaseValueObjectException):
    @property
    def message(self) -> str:
        return "Ошибка численного значения!"


@dataclass(frozen=True, eq=False)
class NonNegativeIntLTZeroException(NumberValueException):
    @property
    def message(self) -> str:
        return "Неотрицательные число не может быть меньше нуля!"


@dataclass(frozen=True, eq=False)
class PriceLEZeroException(NumberValueException):
    @property
    def message(self) -> str:
        return "Цена на товар должна быть больше нуля!"


@dataclass(frozen=True, eq=False)
class PositiveIntLEZeroException(NumberValueException):
    @property
    def message(self) -> str:
        return "Положительное число должно быть больше нуля!"
