import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.entities.category import ProductCategory


@dataclass(frozen=True, eq=False)
class ProductCategoryRepository(ABC):
    @abstractmethod
    async def add_product_category(self, product_category: ProductCategory) -> None:
        pass

    @abstractmethod
    async def check_product_category_exist_by_name(self, name: str) -> bool:
        pass

    @abstractmethod
    async def get_category_by_id(self, product_category_id: uuid.UUID) -> ProductCategory | None:
        pass
