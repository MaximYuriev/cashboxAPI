import uuid
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class BaseEntity(ABC):
    entity_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
