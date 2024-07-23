from src.models.common.value_object import ItemID
from src.models.user.entity import User
from src.models.user.repository import BaseUserRepository, UserRepositoryMemory
from src.models.user.service.user import CreateUser
from src.models.user.value_object import UserName, UserEmail, UserPassword
from src.models.user.rule.create import UserRuleIsExistInRepository


def create_users(repository: BaseUserRepository, count: int = 5):
    list_user = [
        User(
            id=ItemID(i),
            first_name=UserName(f"Petyi{i}"),
            last_name=UserName("Last"),
            email=UserEmail("Mail@wqe"),
            password=UserPassword("SECRET12"),
        )
        for i in range(count)
    ]
    for user in list_user:
        instance = CreateUser(instance_user=user, repository=repository, rule=[])
        instance.execute()


def check_rule(repo: BaseUserRepository, id_item: int):
    repo.is_exist_by_id(id_item)
    user = User(
        id=ItemID(id_item),
        first_name=UserName("Fsd"),
        last_name=UserName("Last"),
        email=UserEmail("Mail@wqe"),
        password=UserPassword("SECRET12"),
    )
    instance = CreateUser(
        instance_user=user, repository=repo, rule=[UserRuleIsExistInRepository]
    )
    instance.execute()


repo = UserRepositoryMemory()
create_users(repo, count=10)
for i in repo.all():
    print(i)

check_rule(repo, 9)
