from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime, UTC

from app.domain.events.base import BaseEvent


@dataclass
class BaseEntity(ABC):
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
    updated_at: datetime = field(default_factory=lambda: datetime.now(UTC), kw_only=True)
    _events: list[BaseEvent] = field(default_factory=list, kw_only=True)
