from abc import ABC, abstractmethod
from typing import Sequence

from .entyty import User


class BaseUserRepository(ABC):
    @abstractmethod
    def all(self) -> Sequence[User]:
        ...

    @abstractmethod
    def get(self, id_user: int) -> User:
        ...

    @abstractmethod
    def get_or_none(self, id_user: int) -> User | None:
        try:
            self.get(id_user)
        except Exception as e:
            return None

    @abstractmethod
    def add(self, user: User) -> None:
        ...

    @abstractmethod
    def delete(self, id_user: int) -> None:
        ...

    @abstractmethod
    def update(self, id_user: int, **kwargs) -> User:
        ...


class UserRepositoryMemory(BaseUserRepository):
    def __init__(self):
        self.temp = []

    def all(self) -> list[User]:
        return self.temp

    def get(self, id_user: int) -> User:
        for user in self.temp:
            if user.id == id_user:
                return user
        raise KeyError()

    def add(self, user: User) -> None:
        self.temp.append(user)

    def delete(self, id_user: int) -> None:
        for index, user in enumerate(self.temp):
            if user.id == id_user:
                del self.temp[index]

    def update(self, id_user: int, **kwargs) -> User:
        pass
