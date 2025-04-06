from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, UTC


@dataclass
class BaseEntity(ABC):
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
