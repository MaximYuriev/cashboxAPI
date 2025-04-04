from dataclasses import dataclass

from app.domain.exceptions.values.base import BaseValueObjectException


@dataclass
class TextValueException(BaseValueObjectException):
    @property
    def message(self) -> str:
        return "Ошибка текстового значения!"


@dataclass
class TextTooLongException(TextValueException):
    @property
    def message(self) -> str:
        return "Текст слишком длинный!"


@dataclass
class EmptyTextException(TextValueException):
    @property
    def message(self) -> str:
        return "Текст не может быть пустым!"


@dataclass
class EmptyNameException(TextValueException):
    @property
    def message(self) -> str:
        return "Имя не может быть пустым!"


@dataclass
class NameTooLongException(TextValueException):
    @property
    def message(self) -> str:
        return "Имя слишком длинное!"
