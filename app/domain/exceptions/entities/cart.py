from dataclasses import dataclass

from app.domain.exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class CartException(ApplicationException):
    @property
    def message(self) -> str:
        return "Ошибка при использовании корзины!"


@dataclass(frozen=True, eq=False)
class ProductAlreadyInCartException(CartException):
    @property
    def message(self) -> str:
        return "Товар уже добавлен в корзину!"


@dataclass(frozen=True, eq=False)
class ProductNotInCartException(CartException):
    @property
    def message(self) -> str:
        return "Товар не добавлен в корзину!"
