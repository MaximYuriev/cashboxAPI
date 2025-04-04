import uuid
from dataclasses import dataclass, field

from app.domain.values.numbers import PositiveInt, Price
from app.domain.values.texts import Text, Name


@dataclass
class Product:
    product_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    name: Name
    description: Text
    quantity: PositiveInt
    price: Price
