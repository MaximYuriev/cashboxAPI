import datetime
from decimal import Decimal

from app.domain.entities.product import Product
from app.domain.values.numbers import NonNegativeInt, Price
from app.domain.values.texts import Name, Text


def test_create_product_success():
    name = Name("name")
    description = Text("text")
    quantity = NonNegativeInt(1)
    price = Price(Decimal(1))

    product = Product(
        name=name,
        description=description,
        quantity=quantity,
        price=price,
    )

    assert product.name == name
    assert product.created_at.date() == datetime.date.today()
