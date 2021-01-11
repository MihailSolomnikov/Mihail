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


class Student(Abiturient):

    def factory_method(self) -> ZaoStudent:
        return Student_one()


class ZaoStudent(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass


class Student_one(ZaoStudent):
    def operation(self) -> str:
        return "{Result of the Student_one is ZaoStudent}"


def client_code(creator: Abiturient) -> None:

    print(f"Client: it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Launched")
    client_code(Student())
