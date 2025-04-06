import uuid
from dataclasses import dataclass, field

from app.domain.entities.base import BaseEntity
from app.domain.entities.product_on_cart import ProductOnCart
from app.domain.exceptions.entities.cart import ProductAlreadyInCartException, ProductNotInCartException


@dataclass
class Cart(BaseEntity):
    cart_id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
    products_on_cart: list[ProductOnCart] = field(default_factory=list, kw_only=True)

    def add_product_on_cart(self, added_product: ProductOnCart) -> None:
        if added_product in self.products_on_cart:
            raise ProductAlreadyInCartException
        self.products_on_cart.append(added_product)

    def delete_product_from_cart(self, deleted_product: ProductOnCart) -> None:
        if deleted_product not in self.products_on_cart:
            raise ProductNotInCartException
        self.products_on_cart.remove(deleted_product)
