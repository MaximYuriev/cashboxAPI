from dataclasses import dataclass, field

from app.application.commands.base import BaseCommand
from app.application.exceptions.mediator import EventHandlerNotRegisteredException, CommandHandlerNotRegisteredException
from app.application.handlers.commands.base import BaseCommandHandler
from app.application.handlers.events.base import BaseEventHandler
from app.domain.events.base import BaseEvent


@dataclass(eq=False)
class Mediator[ET, ER, CT, CR]:
    events_map: dict[ET, BaseEventHandler] = field(default_factory=dict, kw_only=True)
    commands_map: dict[ER, BaseCommandHandler] = field(default_factory=dict, kw_only=True)

    def register_event(self, event: ET, handler: BaseEventHandler) -> None:
        self.events_map[event] = handler

    def register_command(self, command: CT, handler: BaseCommandHandler) -> None:
        self.commands_map[command] = handler

    async def handle_event(self, event: BaseEvent) -> ER:
        event_type = event.__class__
        handler = self.events_map.get(event_type)

        if not handler:
            raise EventHandlerNotRegisteredException(event_type)

        return await handler.handle(event)

    async def handle_command(self, command: BaseCommand) -> CR:
        command_type = command.__class__
        handler = self.commands_map.get(command_type)

        if not handler:
            raise CommandHandlerNotRegisteredException(command_type)

        return await handler.handle(command)
