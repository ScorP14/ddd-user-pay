from dataclasses import dataclass

from src.models.common.value_object import ItemID
from src.models.user.entity import User


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
