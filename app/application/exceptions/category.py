import uuid
from dataclasses import dataclass

from app.domain.exceptions.entities.category import ProductCategoryException


@dataclass(frozen=True, eq=False)
class ProductCategoryAlreadyExistException(ProductCategoryException):
    name: str

    @property
    def message(self) -> str:
        return f"Категория товара с таким названием '{self.name}' уже существует!"


@dataclass(frozen=True, eq=False)
class ProductCategoryNotFoundException(ProductCategoryException):
    category_id: uuid.UUID

    @property
    def message(self) -> str:
        return f"Категория товара с id: '{self.category_id}' не найдена!"
