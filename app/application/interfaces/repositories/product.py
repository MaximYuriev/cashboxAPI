from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.entities.product import Product


@dataclass(frozen=True, eq=False)
class ProductRepository(ABC):
    @abstractmethod
    async def add_product(self, product: Product) -> None:
        pass

    @abstractmethod
    async def check_product_exist_by_name(self, name: str) -> bool:
        pass
