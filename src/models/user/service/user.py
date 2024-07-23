from dataclasses import dataclass, field
from typing import Type, Sequence

from src.models.common.value_object import ItemID
from src.models.user.entity import User
from src.models.user.repository import BaseUserRepository
from src.models.user.rule.create import UserRuleCreate
from src.models.user.value_object import UserName, UserEmail, UserPassword
from src.models.user.repository import UserRepositoryMemory


@dataclass
class CreateUser:
    repository: BaseUserRepository
    instance_user: User
    rule: Sequence[Type[UserRuleCreate]] = field(default_factory=list)

    def execute(self):
        for rule in self.rule:
            rule(user=self.instance_user, repository=self.repository).checking()
        self.repository.add(self.instance_user)


@dataclass
class DeleteUser:
    repository: BaseUserRepository
    id_item: int

    def execute(self):
        self.repository.delete(self.id_item)


@dataclass
class UpdateUser:
    repository: BaseUserRepository
    instance_user: User
    fields: dict[str, str]  # ?

    def execute(self):
        self.repository.update(self.instance_user.id.value, **self.fields)


@dataclass
class GetUser:
    repository: BaseUserRepository
    id_item: int

    def execute(self):
        self.repository.get(self.id_item)


@dataclass
class GetOrNoneUser:
    repository: BaseUserRepository
    id_item: int

    def execute(self):
        self.repository.get_or_none(self.id_item)
