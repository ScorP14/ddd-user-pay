from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseBusinessRule(ABC):

    @abstractmethod
    def checking(self): ...
