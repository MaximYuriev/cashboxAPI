from pydantic import BaseModel


class APIResponse[T](BaseModel):
    detail: str
    data: T | list[T] | None = None
