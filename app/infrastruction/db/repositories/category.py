import uuid
from dataclasses import dataclass

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.repositories.category import ProductCategoryRepository
from app.domain.entities.category import ProductCategory
from app.infrastruction.db.models.category import ProductCategoryModel


@dataclass(frozen=True, eq=False)
class SQLAlchemyProductCategoryRepository(ProductCategoryRepository):
    _session: AsyncSession

    async def add_product_category(self, product_category: ProductCategory) -> None:
        model = ProductCategoryModel.from_entity(product_category)
        self._session.add(model)
        await self._session.commit()

    async def get_category_by_id(self, product_category_id: uuid.UUID) -> ProductCategory | None:
        model = await self._get_model(product_category_id)
        if model is not None:
            return model.to_entity()

    async def check_product_category_exist_by_name(self, name: str) -> bool:
        query = select(ProductCategoryModel).where(ProductCategoryModel.name == name)
        if await self._session.scalar(query):
            return True
        return False

    async def _get_model(self, product_category_id: uuid.UUID) -> ProductCategoryModel | None:
        query = select(ProductCategoryModel).where(ProductCategoryModel.category_id == product_category_id)
        return await self._session.scalar(query)
