from dataclasses import dataclass
from abc import ABC

from src.models.user.entity import User
from src.models.user.repository import BaseUserRepository
from src.models.user.rule.base import BaseBusinessRule


@dataclass(frozen=True)
class UserRuleCreate(BaseBusinessRule, ABC):
    """Базовый класс для всех бизнес правил по созданию пользователя"""
    user: User
    repository: BaseUserRepository


@dataclass(frozen=True)
class UserRuleIsExistInRepository(UserRuleCreate):

    def checking(self):
        if self.repository.is_exist_by_id(self.user.id.value):
            raise Exception("ЕСТЬ ТАКОЙ ПОЛЬЗОВАТЕЛЬ!!!!")
