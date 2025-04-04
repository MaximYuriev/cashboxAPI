from dataclasses import dataclass
from decimal import Decimal

from app.domain.exceptions.values.numbers import PriceLEZeroException, PositiveIntLTZeroException
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class PositiveInt(BaseValueObject[int]):
    def validate(self) -> None:
        if self.value < 0:
            raise PositiveIntLTZeroException


@dataclass(frozen=True)
class Price(BaseValueObject[Decimal]):
    def validate(self) -> None:
        if self.value <= 0:
            raise PriceLEZeroException
