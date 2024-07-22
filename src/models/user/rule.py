from dataclasses import dataclass
from abc import ABC, abstractmethod

from src.models.user.entity import User
from src.models.user.repository import BaseUserRepository


@dataclass(frozen=True)
class BaseBusinessRule(ABC):

    @abstractmethod
    def checking(self): ...


@dataclass(frozen=True)
class UserRuleCreate(BaseBusinessRule, ABC):
    user: User
    repository: BaseUserRepository


@dataclass(frozen=True)
class UserRuleIsExistInRepository(UserRuleCreate):

    def checking(self):
        if self.repository.is_exist_by_id(self.user.id.value):
            raise Exception("ЕСТЬ ТАКОЙ ПОЛЬЗОВАТЕЛЬ!!!!")
