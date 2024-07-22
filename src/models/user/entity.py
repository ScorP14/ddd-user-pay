from dataclasses import dataclass, field

from src.models.common.value_object import ItemID
from src.models.user.value_object import UserName, UserPassword, UserEmail


@dataclass
class User:
    id: ItemID
    first_name: UserName = field(repr=False)
    last_name: UserName = field(repr=False)
    email: UserEmail = field(repr=False)
    password: UserPassword = field(repr=False)


@dataclass
class Administrator(User): ...
