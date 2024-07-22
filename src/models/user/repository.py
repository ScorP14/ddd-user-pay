from abc import ABC, abstractmethod
from typing import Sequence

from src.models.user.entity import User
from src.models.user.exeption.repository import UserRepositoryNotFoundError


class BaseUserRepository(ABC):
    @abstractmethod
    def all(self) -> Sequence[User]: ...

    @abstractmethod
    def get(self, id_user: int) -> User: ...

    @abstractmethod
    def get_or_none(self, id_user: int) -> User | None:
        try:
            self.get(id_user)
        except UserRepositoryNotFoundError as e:
            return None

    @abstractmethod
    def add(self, user: User) -> None: ...

    @abstractmethod
    def delete(self, id_user: int) -> None: ...

    @abstractmethod
    def update(self, id_user: int, **kwargs) -> User: ...

    @abstractmethod
    def is_exist_by_id(self, id_user: int) -> bool: ...

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.__class__.__name__


class UserRepositoryMemory(BaseUserRepository):
    def __init__(self):
        self.temp: list[User] = list()

    def all(self) -> list[User]:
        return self.temp

    def get(self, id_user: int) -> User:
        for user in self.temp:
            if user.id.value == id_user:
                return user
        raise UserRepositoryNotFoundError(id_user)

    def get_or_none(self, id_user: int) -> User | None:
        try:
            return self.get(id_user)
        except UserRepositoryNotFoundError:
            return None

    def is_exist_by_id(self, id_user: int) -> bool:
        if self.get_or_none(id_user):
            return True
        return False

    def add(self, user: User) -> None:
        self.temp.append(user)

    def delete(self, id_user: int) -> None:
        for index, user in enumerate(self.temp):
            if user.id == id_user:
                del self.temp[index]

    def update(self, id_user: int, **kwargs) -> User:
        pass
