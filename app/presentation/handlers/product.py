from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException
from starlette import status

from app.application.commands.product import AddProductCommand
from app.application.mediator import Mediator
from app.domain.exceptions.base import ApplicationException
from app.presentation.commons.response import APIResponse
from app.presentation.schemas.product import CreateProductSchema, ProductResponseSchema

router = APIRouter()


@router.post("/")
@inject
async def create_product(
        product_schema: CreateProductSchema,
        mediator: FromDishka[Mediator],
) -> APIResponse[ProductResponseSchema]:
    try:
        command = AddProductCommand(**product_schema.model_dump())
        product = await mediator.handle_command(command)
    except ApplicationException as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=exc.message)
    else:
        return APIResponse(detail="Товар успешно добавлен!", data=ProductResponseSchema.from_entity(product))
