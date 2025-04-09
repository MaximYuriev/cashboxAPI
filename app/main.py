from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.config import Config
from app.ioc import SQLAlchemyProvider, MediatorProvider, ProductCategoryProvider
from app.presentation.handlers.category import router

config = Config()
container = make_async_container(
    SQLAlchemyProvider(),
    MediatorProvider(),
    ProductCategoryProvider(),
    context={Config: config}
)
app = FastAPI()

app.include_router(router, prefix="/category", tags=["Category"])

setup_dishka(container, app)
