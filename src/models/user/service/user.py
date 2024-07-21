from dataclasses import dataclass

from src.models.common.value_object import ItemID
from src.models.user.entyty import User
from src.models.user.repository import BaseUserRepository
from src.models.user.value_object import UserName, UserEmail, UserPassword


@dataclass
class CreateUser:
    repository: BaseUserRepository
    instance_user: User

    def execute(self):
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
    fields: dict[str, str] # ?

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



from src.models.user.entyty import User
from src.models.user.repository import UserRepositoryMemory

repo = UserRepositoryMemory()

user1 = User(
    id=ItemID(),
    first_name=UserName('Fsd'), last_name=UserName('Last'),
    email=UserEmail('Mail@wqe'), password=UserPassword('SECRET12')
)
insta = CreateUser(instance_user=user1, repository=repo)
print(insta)
insta.execute()
print(repo.all())

# print(user1)
# print(user1.password == 'SECRET123')
