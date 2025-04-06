import datetime
import uuid
from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Text, Name


@dataclass
class Product(BaseEntity):
    name: Name
    description: Text
    quantity: NonNegativeInt
    price: Price
