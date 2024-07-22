from abc import ABC
from dataclasses import dataclass

from src.models.common.exeption import BaseError


@dataclass(frozen=True, repr=False)
class UserValueObjectError(BaseError, ABC): ...


@dataclass(frozen=True, repr=False)
class UserValueObjectNameError(UserValueObjectError, ABC): ...


@dataclass(frozen=True, repr=False)
class UserNameShortLenError(UserValueObjectNameError):
    value: str

    @property
    def message(self) -> str:
        return f"Слишком короткое имя {len(self.value)}. Нужно больше 2 символов"


@dataclass(frozen=True, repr=False)
class UserNameLengthLenError(UserValueObjectNameError):
    value: str

    @property
    def message(self) -> str:
        return f"Слишком длинное имя {len(self.value)}. Нужно меньше 200 символов"


@dataclass(frozen=True, repr=False)
class UserValueObjectPasswordError(UserValueObjectError, ABC): ...


@dataclass(frozen=True, repr=False)
class UserPasswordShortLenError(UserValueObjectPasswordError):
    value: str

    @property
    def message(self) -> str:
        return f"Слишком короткий пароль {len(self.value)}. Нужно больше 8 символов"


@dataclass(frozen=True, repr=False)
class UserPasswordLengthLenError(UserValueObjectPasswordError):
    value = str

    @property
    def message(self) -> str:
        return f"Слишком длинный пароль {len(self.value)}. Нужно меньше 30 символов"


@dataclass(frozen=True, repr=False)
class UserValueObjectEmailError(UserValueObjectError, ABC): ...


@dataclass(frozen=True, repr=False)
class UserMailNotValidError(UserValueObjectPasswordError):
    value = str

    @property
    def message(self) -> str:
        return f"Неверный адрес электронной почты - {self.value}"
