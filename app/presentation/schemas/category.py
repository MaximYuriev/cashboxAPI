import datetime
import uuid

from pydantic import BaseModel

from app.domain.entities.category import ProductCategory


class ProductCategoryResponseSchema(BaseModel):
    category_id: uuid.UUID
    name: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @classmethod
    def from_entity(cls, product_category: ProductCategory) -> "ProductCategoryResponseSchema":
        return cls(
            category_id=product_category.category_id,
            name=product_category.name.value_to_generic_type,
            description=product_category.description.value_to_generic_type,
            created_at=product_category.created_at,
            updated_at=product_category.updated_at,
        )


class CreateProductCategorySchema(BaseModel):
    name: str
    description: str
