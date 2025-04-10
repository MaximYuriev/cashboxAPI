from typing import AsyncIterable

from dishka import Provider, from_context, Scope, provide
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession

from app.application.commands.category import AddProductCategoryCommand
from app.application.commands.product import AddProductCommand
from app.application.handlers.commands.category import AddProductCategoryHandler
from app.application.handlers.commands.product import AddProductCommandHandler
from app.application.interfaces.repositories.category import ProductCategoryRepository
from app.application.interfaces.repositories.product import ProductRepository
from app.application.mediator import Mediator
from app.config import Config
from app.infrastruction.db.repositories.category import SQLAlchemyProductCategoryRepository
from app.infrastruction.db.repositories.product import SQLAlchemyProductRepository


class SQLAlchemyProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def get_async_engine(self, config: Config) -> AsyncEngine:
        return create_async_engine(config.postgres.db_url, echo=False)

    @provide(scope=Scope.APP)
    def get_async_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False)

    @provide(scope=Scope.REQUEST)
    async def get_session(self, session_maker: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        async with session_maker() as session:
            yield session


class MediatorProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def init_mediator(
            self,
            add_product_category_command_handler: AddProductCategoryHandler,
            add_product_command_handler: AddProductCommandHandler,
    ) -> Mediator:
        mediator = Mediator()

        mediator.register_command(
            command=AddProductCategoryCommand,
            handler=add_product_category_command_handler,
        )

        mediator.register_command(
            command=AddProductCommand,
            handler=add_product_command_handler,
        )

        return mediator


class ProductCategoryProvider(Provider):
    scope = Scope.REQUEST

    product_category_repository = provide(SQLAlchemyProductCategoryRepository, provides=ProductCategoryRepository)
    add_product_category_handler = provide(AddProductCategoryHandler)


class ProductProvider(Provider):
    scope = Scope.REQUEST

    product_repository = provide(SQLAlchemyProductRepository, provides=ProductRepository)
    add_product_command_handler = provide(AddProductCommandHandler)
