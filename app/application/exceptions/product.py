from dataclasses import dataclass

from app.domain.exceptions.entities.product import ProductException


@dataclass(frozen=True, eq=False)
class ProductAlreadyExistException(ProductException):
    name: str

    @property
    def message(self) -> str:
        return f"Товар с таким названием '{self.name}' уже существует!"
