from dataclasses import dataclass

from app.application.commands.category import AddProductCategoryCommand
from app.application.exceptions.category import ProductCategoryAlreadyExistException
from app.application.handlers.commands.base import BaseCommandHandler
from app.application.interfaces.repositories.category import ProductCategoryRepository
from app.domain.entities.category import ProductCategory
from app.domain.values.texts import Name, Text


@dataclass(frozen=True, eq=False)
class AddProductCategoryHandler(BaseCommandHandler):
    product_category_repository: ProductCategoryRepository

    async def handle(self, command: AddProductCategoryCommand) -> ProductCategory:
        if await self.product_category_repository.check_product_category_exist_by_name(command.name):
            raise ProductCategoryAlreadyExistException(command.name)

        name = Name(command.name)
        description = Text(command.description)
        product_category = ProductCategory(
            name=name,
            description=description
        )

        await self.product_category_repository.add_product_category(product_category)

        return product_category
