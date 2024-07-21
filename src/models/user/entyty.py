from dataclasses import dataclass

from src.models.common.exeption import BaseError
from src.models.common.value_object import ItemID
from src.models.user.value_object import UserName, UserPassword, UserEmail


@dataclass
class User:
    id: ItemID
    first_name: UserName
    last_name: UserName
    email: UserEmail
    password: UserPassword


@dataclass
class Payment:
    id: ItemID
    user: User
    amount: float


@dataclass
class Account:
    id: ItemID
    user: User
    balance: float





user1 = User(
    id=ItemID(),
    first_name=UserName('Fsd'), last_name=UserName('Last'),
    email=UserEmail('Mail@wqe'), password=UserPassword('SECRET12')
)


print(user1)
print(user1.password == 'SECRET123')


@dataclass
class Administrator(User):
    ...
