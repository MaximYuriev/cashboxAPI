from dataclasses import dataclass

from app.application.commands.product import AddProductCommand
from app.application.exceptions.category import ProductCategoryNotFoundException
from app.application.exceptions.product import ProductAlreadyExistException
from app.application.handlers.commands.base import BaseCommandHandler
from app.application.interfaces.repositories.category import ProductCategoryRepository
from app.application.interfaces.repositories.product import ProductRepository
from app.domain.entities.product import Product
from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Name, Text


@dataclass(frozen=True, eq=False)
class AddProductCommandHandler(BaseCommandHandler):
    product_repository: ProductRepository
    product_category_repository: ProductCategoryRepository

    async def handle(self, command: AddProductCommand) -> Product:
        if await self.product_repository.check_product_exist_by_name(command.name):
            raise ProductAlreadyExistException(command.name)

        category = await self.product_category_repository.get_category_by_id(command.category_id)
        if category is None:
            raise ProductCategoryNotFoundException(command.category_id)

        product = Product(
            name=Name(command.name),
            description=Text(command.description),
            quantity=NonNegativeInt(command.quantity),
            price=Price(command.price),
            category=category,
        )

        await self.product_repository.add_product(product)

        return product
