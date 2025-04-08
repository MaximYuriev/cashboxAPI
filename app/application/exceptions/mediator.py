from dataclasses import dataclass
from typing import Type

from app.application.commands.base import BaseCommand
from app.domain.events.base import BaseEvent
from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class MediatorException(ApplicationException):
    @property
    def message(self) -> str:
        return "Ошибка при использовании медиатора!"


@dataclass(frozen=True, eq=False)
class CommandHandlerNotRegisteredException(MediatorException):
    command_type: Type[BaseCommand]

    @property
    def message(self) -> str:
        return f"Не найден обработчик команды: '{self.command_type}'!"


@dataclass(frozen=True, eq=False)
class EventHandlerNotRegisteredException(MediatorException):
    event_type: Type[BaseEvent]

    @property
    def message(self) -> str:
        return f"Не найден обработчик события: '{self.event_type}'!"
