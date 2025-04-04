from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class BaseValueObjectException(ApplicationException):
    @property
    def message(self) -> str:
        return "Базовая ошибка значения!"
