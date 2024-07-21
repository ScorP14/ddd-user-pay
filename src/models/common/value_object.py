import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, repr=False)
class ValueObject(ABC):
    value: Any

    def __post_init__(self):
        self._validator()

    @abstractmethod
    def _validator(self):
        """Валидация value"""

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.value


@dataclass(frozen=True, repr=False)
class ItemID(ValueObject):
    value: int = field(default_factory=lambda: uuid.uuid4().int)

    def _validator(self):
        pass

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.value)
