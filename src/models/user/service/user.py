from dataclasses import dataclass, field
from typing import Type, Sequence

from src.models.common.value_object import ItemID
from src.models.user.entity import User
from src.models.user.repository import BaseUserRepository
from src.models.user.rule import UserRuleCreate
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


repo = UserRepositoryMemory()

for i in range(5):
    user1 = User(
        id=ItemID(i),
        first_name=UserName("Fsd"),
        last_name=UserName("Last"),
        email=UserEmail("Mail@wqe"),
        password=UserPassword("SECRET12"),
    )
    insta = CreateUser(instance_user=user1, repository=repo, rule=[])
    insta.execute()

print(repo.is_exist_by_id(3))

user12 = User(
    id=ItemID(3),
    first_name=UserName("Fsd"),
    last_name=UserName("Last"),
    email=UserEmail("Mail@wqe"),
    password=UserPassword("SECRET12"),
)
insta = CreateUser(instance_user=user12, repository=repo, rule=[])
insta.execute()

for i in repo.all():
    print(i)
