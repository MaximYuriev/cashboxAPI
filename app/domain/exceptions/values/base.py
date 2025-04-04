from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass
class BaseValueObjectException(ApplicationException):
    @property
    def message(self) -> str:
        return "Базовая ошибка значения!"
