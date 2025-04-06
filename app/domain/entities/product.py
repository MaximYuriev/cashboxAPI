import uuid
from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.entities.category import ProductCategory
from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Text, Name


@dataclass
class Product(BaseEntity):
    product_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    name: Name
    description: Text = field(compare=False)
    category: ProductCategory = field(compare=False)
    quantity: NonNegativeInt = field(compare=False)
    price: Price = field(compare=False)
