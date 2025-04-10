import decimal
import uuid
from dataclasses import dataclass

from app.application.commands.base import BaseCommand


@dataclass(frozen=True, eq=False)
class AddProductCommand(BaseCommand):
    name: str
    description: str
    category_id: uuid.UUID
    quantity: int
    price: decimal.Decimal
