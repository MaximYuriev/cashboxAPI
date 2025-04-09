from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException
from starlette import status

from app.application.commands.category import AddProductCategoryCommand
from app.application.mediator import Mediator
from app.domain.exceptions.base import ApplicationException
from app.presentation.commons.response import APIResponse
from app.presentation.schemas.category import ProductCategoryResponseSchema, CreateProductCategorySchema

router = APIRouter()


@router.post("/")
@inject
async def create_category(
        product_category: CreateProductCategorySchema,
        mediator: FromDishka[Mediator],
) -> APIResponse[ProductCategoryResponseSchema]:
    try:
        product_category = await mediator.handle_command(
            command=AddProductCategoryCommand(**product_category.model_dump())
        )
    except ApplicationException as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    else:
        return APIResponse(
            detail="Категория товара успешно добавлена!",
            data=ProductCategoryResponseSchema.from_entity(product_category),
        )
