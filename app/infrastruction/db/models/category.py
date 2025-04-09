import uuid

from sqlalchemy.orm import Mapped, mapped_column

from app.domain.entities.category import ProductCategory
from app.domain.values.texts import Name, Text
from app.infrastruction.db.models.base import Base


class ProductCategoryModel(Base):
    __tablename__ = "product_category"
    category_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str]

    @classmethod
    def from_entity(cls, category: ProductCategory) -> "ProductCategoryModel":
        return cls(
            category_id=category.category_id,
            name=category.name.value_to_generic_type,
            description=category.description.value_to_generic_type,
            created_at=category.created_at,
            updated_at=category.updated_at,
        )

    def to_entity(self) -> ProductCategory:
        return ProductCategory(
            category_id=self.category_id,
            name=Name(self.name),
            description=Text(self.description),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
