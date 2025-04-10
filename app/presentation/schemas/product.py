import datetime
import decimal
import uuid

from pydantic import BaseModel

from app.domain.entities.product import Product
from app.presentation.schemas.category import ProductCategoryResponseSchema


class ProductResponseSchema(BaseModel):
    product_id: uuid.UUID
    name: str
    description: str
    category: ProductCategoryResponseSchema
    quantity: int
    price: decimal.Decimal
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @classmethod
    def from_entity(cls, product: Product) -> "ProductResponseSchema":
        return cls(
            product_id=product.product_id,
            name=product.name.value_to_generic_type,
            description=product.description.value_to_generic_type,
            category=ProductCategoryResponseSchema.from_entity(product.category),
            quantity=product.quantity.value_to_generic_type,
            price=product.price.value_to_generic_type,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )


class CreateProductSchema(BaseModel):
    name: str
    description: str
    category_id: uuid.UUID
    quantity: int
    price: decimal.Decimal
