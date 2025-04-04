from dataclasses import dataclass

from app.domain.exceptions.values.base import BaseValueObjectException


@dataclass(frozen=True, eq=False)
class TextValueException(BaseValueObjectException):
    @property
    def message(self) -> str:
        return "Ошибка текстового значения!"


@dataclass(frozen=True, eq=False)
class TextTooLongException(TextValueException):
    @property
    def message(self) -> str:
        return "Текст слишком длинный!"


@dataclass(frozen=True, eq=False)
class EmptyTextException(TextValueException):
    @property
    def message(self) -> str:
        return "Текст не может быть пустым!"


@dataclass(frozen=True, eq=False)
class EmptyNameException(TextValueException):
    @property
    def message(self) -> str:
        return "Имя не может быть пустым!"


@dataclass(frozen=True, eq=False)
class NameTooLongException(TextValueException):
    @property
    def message(self) -> str:
        return "Имя слишком длинное!"
