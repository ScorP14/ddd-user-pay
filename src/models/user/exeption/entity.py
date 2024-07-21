from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.models.common.exeption import BaseError


@dataclass(frozen=True, repr=False, kw_only=True)
class BaseUserEntityError(BaseError, ABC):
    ...



