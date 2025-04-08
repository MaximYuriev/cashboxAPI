from app.application.commands.base import BaseCommand


class AddProductCategoryCommand(BaseCommand):
    name: str
    description: str
