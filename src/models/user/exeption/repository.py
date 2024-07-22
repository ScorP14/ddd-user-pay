from dataclasses import dataclass
from abc import ABC

from src.models.user.exeption.base import BaseUserError


@dataclass(frozen=True, repr=False)
class UserRepositoryError(BaseUserError, ABC): ...


@dataclass(frozen=True, repr=False)
class UserRepositoryNotFoundError(UserRepositoryError):
    value: int

    @property
    def message(self) -> str:
        return f"Пользователь с id({self.value}) не найден"
