import datetime
import uuid
from dataclasses import dataclass, field

from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Text, Name


@dataclass
class Product:
    product_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    name: Name
    description: Text
    quantity: NonNegativeInt
    price: Price
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now, kw_only=True)
    updated_at: datetime.datetime = field(default_factory=datetime.datetime.now, kw_only=True)
