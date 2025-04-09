from dataclasses import dataclass

from app.application.commands.base import BaseCommand


@dataclass(frozen=True, eq=False)
class AddProductCategoryCommand(BaseCommand):
    name: str
    description: str
