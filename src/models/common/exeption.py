from dataclasses import dataclass
from typing import Any
from abc import ABC, abstractmethod


@dataclass(frozen=True, repr=False)
class BaseError(Exception, ABC):
    value: Any

    @property
    @abstractmethod
    def message(self) -> str: ...
