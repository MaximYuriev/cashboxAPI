from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.repositories.product import ProductRepository
from app.domain.entities.product import Product
from app.infrastruction.db.models.product import ProductModel


@dataclass(frozen=True, eq=False)
class SQLAlchemyProductRepository(ProductRepository):
    _session: AsyncSession

    async def add_product(self, product: Product) -> None:
        model = ProductModel.from_entity(product)
        self._session.add(model)
        await self._session.commit()

    async def check_product_exist_by_name(self, name: str) -> bool:
        query = select(ProductModel).where(ProductModel.name == name)
        if await self._session.scalar(query):
            return True
        return False
