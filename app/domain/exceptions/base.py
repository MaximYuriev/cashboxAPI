from dataclasses import dataclass


@dataclass
class ApplicationException:
    @property
    def message(self) -> str:
        return "Ошибка в работе приложения!"
