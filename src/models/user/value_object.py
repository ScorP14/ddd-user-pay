from dataclasses import dataclass

from email_validator import validate_email, EmailNotValidError

from src.models.common.value_object import ValueObject
from src.models.user.exeption.value_object import (
    UserNameShortLenError,
    UserNameLengthLenError,
)
from src.models.user.exeption.value_object import (
    UserPasswordLengthLenError,
    UserPasswordShortLenError,
)
from src.models.user.exeption.value_object import UserMailNotValidError


@dataclass(frozen=True, repr=False)
class UserName(ValueObject):
    value: str

    def _validator(self):
        if len(self.value) < 2:
            raise UserNameShortLenError(value=self.value)
        elif len(self.value) > 200:
            raise UserNameLengthLenError(value=self.value)


@dataclass(frozen=True, repr=False)
class UserPassword(ValueObject):
    value: str

    def _validator(self):
        if len(self.value) < 8:
            raise UserPasswordShortLenError(self.value)
        elif len(self.value) > 30:
            raise UserPasswordLengthLenError(self.value)


@dataclass(frozen=True, repr=False)
class UserEmail(ValueObject):
    value: str

    def _validator(self):
        try:
            validate_email(
                self.value,
                allow_smtputf8=False,
                allow_empty_local=False,
                allow_quoted_local=True,
                allow_domain_literal=False,
                allow_display_name=False,
                check_deliverability=False,
                test_environment=False,
                globally_deliverable=False,
                timeout=False,
                dns_resolver=False,
            )
        except EmailNotValidError as e:
            raise UserMailNotValidError(self.value)
