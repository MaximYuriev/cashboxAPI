from dataclasses import dataclass

from app.domain.exceptions.values.texts import TextTooLongException, EmptyTextException, EmptyNameException, \
    NameTooLongException
from app.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Text[T:str](BaseValueObject):
    def validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyTextException
        if len(self.value) > 255:
            raise TextTooLongException


@dataclass(frozen=True)
class Name[T:str](BaseValueObject):
    def validate(self) -> None:
        if len(self.value) == 0:
            raise EmptyNameException
        elif len(self.value) > 100:
            raise NameTooLongException
