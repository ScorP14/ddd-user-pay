from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class BaseBusinessRule:

    @abstractmethod
    def rule_checking(self):
        ...