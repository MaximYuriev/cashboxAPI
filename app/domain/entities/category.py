import uuid
from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.values.texts import Name, Text


@dataclass
class ProductCategory(BaseEntity):
    category_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    name: Name
    description: Text
