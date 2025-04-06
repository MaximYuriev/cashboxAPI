from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.entities.product import Product
from app.domain.values.numbers import PositiveInt


@dataclass
class ProductOnCart(BaseEntity):
    product: Product
    quantity_on_cart: PositiveInt = field(compare=False)
