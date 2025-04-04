from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseValueObject[T](ABC):
    value: T

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self) -> None:
        pass

    @property
    def value_to_generic_type(self) -> T:
        return self.value
