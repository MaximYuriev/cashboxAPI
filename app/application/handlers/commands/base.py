from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.application.commands.base import BaseCommand
from app.domain.entities.base import BaseEntity


@dataclass(frozen=True, eq=False)
class BaseCommandHandler[CT:BaseCommand, CR:BaseEntity](ABC):
    @abstractmethod
    async def handle(self, command: CT) -> CR:
        pass
