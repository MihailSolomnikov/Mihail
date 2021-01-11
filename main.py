from __future__ import annotations
from abc import ABC, abstractmethod


class Abiturient(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        # Вызываем фабричный метод, чтобы получить объект-продукт.
        product = self.factory_method()

        # Далее, работаем с этим продуктом.
        result = f"Creator: worked with {product.operation()}"

        return result
