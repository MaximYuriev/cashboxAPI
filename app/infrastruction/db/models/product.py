import decimal
import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.domain.entities.product import Product
from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Name, Text
from app.infrastruction.db.models.base import Base
from app.infrastruction.db.models.category import ProductCategoryModel


class ProductModel(Base):
    __tablename__ = "product"
    product_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]
    category_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey(ProductCategoryModel.category_id, ondelete="CASCADE")
    )
    quantity: Mapped[int]
    price: Mapped[decimal.Decimal]

    category: Mapped["ProductCategoryModel"] = relationship()

    @classmethod
    def from_entity(cls, product: Product) -> "ProductModel":
        return cls(
            product_id=product.product_id,
            name=product.name.value_to_generic_type,
            description=product.description.value_to_generic_type,
            category_id=product.category.category_id,
            quantity=product.quantity.value_to_generic_type,
            price=product.price.value_to_generic_type,
            created_at=product.created_at,
            updated_at=product.updated_at,
        )

    def to_entity(self) -> Product:
        return Product(
            product_id=self.product_id,
            name=Name(self.name),
            description=Text(self.description),
            category=self.category,
            quantity=NonNegativeInt(self.quantity),
            price=Price(self.price),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
