import pytest

from app.application.commands.category import AddProductCategoryCommand
from app.application.mediator import Mediator



@pytest.fixture(scope="session")
def mediator() -> Mediator:
    mediator = Mediator()

    mediator.register_command(
        command=AddProductCategoryCommand,
        handler=AddProductCategoryHandler()
    )

    return mediator