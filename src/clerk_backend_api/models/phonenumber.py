"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .identificationlink import IdentificationLink, IdentificationLinkTypedDict
from clerk_backend_api import utils
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import validate_open_enum
from enum import Enum
from pydantic import model_serializer
from pydantic.functional_validators import PlainValidator
from typing import List, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class PhoneNumberObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    PHONE_NUMBER = "phone_number"


class AdminVerificationPhoneNumberStatus(str, Enum):
    VERIFIED = "verified"


class AdminVerificationStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    ADMIN = "admin"


class VerificationAdminTypedDict(TypedDict):
    status: AdminVerificationPhoneNumberStatus
    strategy: AdminVerificationStrategy
    attempts: Nullable[int]
    expire_at: Nullable[int]
    verified_at_client: NotRequired[Nullable[str]]


class VerificationAdmin(BaseModel):
    status: AdminVerificationPhoneNumberStatus

    strategy: Annotated[
        AdminVerificationStrategy, PlainValidator(validate_open_enum(False))
    ]

    attempts: Nullable[int]

    expire_at: Nullable[int]

    verified_at_client: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["verified_at_client"]
        nullable_fields = ["attempts", "expire_at", "verified_at_client"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class OTPVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"


class OTPVerificationStrategy(str, Enum, metaclass=utils.OpenEnumMeta):
    PHONE_CODE = "phone_code"
    EMAIL_CODE = "email_code"
    RESET_PASSWORD_EMAIL_CODE = "reset_password_email_code"


class VerificationOTPTypedDict(TypedDict):
    status: OTPVerificationStatus
    strategy: OTPVerificationStrategy
    attempts: Nullable[int]
    expire_at: Nullable[int]
    verified_at_client: NotRequired[Nullable[str]]


class VerificationOTP(BaseModel):
    status: OTPVerificationStatus

    strategy: Annotated[
        OTPVerificationStrategy, PlainValidator(validate_open_enum(False))
    ]

    attempts: Nullable[int]

    expire_at: Nullable[int]

    verified_at_client: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["verified_at_client"]
        nullable_fields = ["attempts", "expire_at", "verified_at_client"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


PhoneNumberVerificationTypedDict = TypeAliasType(
    "PhoneNumberVerificationTypedDict",
    Union[VerificationOTPTypedDict, VerificationAdminTypedDict],
)


PhoneNumberVerification = TypeAliasType(
    "PhoneNumberVerification", Union[VerificationOTP, VerificationAdmin]
)


class PhoneNumberTypedDict(TypedDict):
    r"""Success"""

    object: PhoneNumberObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    phone_number: str
    reserved: bool
    verification: Nullable[PhoneNumberVerificationTypedDict]
    linked_to: List[IdentificationLinkTypedDict]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    id: NotRequired[str]
    reserved_for_second_factor: NotRequired[bool]
    default_second_factor: NotRequired[bool]
    backup_codes: NotRequired[Nullable[List[str]]]


class PhoneNumber(BaseModel):
    r"""Success"""

    object: PhoneNumberObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    phone_number: str

    reserved: bool

    verification: Nullable[PhoneNumberVerification]

    linked_to: List[IdentificationLink]

    created_at: int
    r"""Unix timestamp of creation

    """

    updated_at: int
    r"""Unix timestamp of creation

    """

    id: Optional[str] = None

    reserved_for_second_factor: Optional[bool] = None

    default_second_factor: Optional[bool] = None

    backup_codes: OptionalNullable[List[str]] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "reserved_for_second_factor",
            "default_second_factor",
            "backup_codes",
        ]
        nullable_fields = ["verification", "backup_codes"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
