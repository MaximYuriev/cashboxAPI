from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.config import Config
from app.ioc import SQLAlchemyProvider, MediatorProvider, ProductCategoryProvider, ProductProvider
from app.presentation.handlers.category import router as category_router
from app.presentation.handlers.product import router as product_router

config = Config()
container = make_async_container(
    SQLAlchemyProvider(),
    MediatorProvider(),
    ProductCategoryProvider(),
    ProductProvider(),
    context={Config: config}
)

app = FastAPI()

app.include_router(category_router, prefix="/category", tags=["Category"])
app.include_router(product_router, prefix="/product", tags=["Product"])

setup_dishka(container, app)
