from dataclasses import dataclass

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
class Administrator(User):
    ...
