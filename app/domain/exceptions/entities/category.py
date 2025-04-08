from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class ProductCategoryException(ApplicationException):
    @property
    def message(self) -> str:
        return "Ошибка при использовании категорий товара!"
