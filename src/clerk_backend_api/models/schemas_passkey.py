"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class SchemasPasskeyObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    PASSKEY = "passkey"


class PasskeyVerificationStatus(str, Enum):
    VERIFIED = "verified"


class PasskeyVerificationStrategy(str, Enum):
    PASSKEY = "passkey"


class Nonce(str, Enum):
    NONCE = "nonce"


class PasskeyTypedDict(TypedDict):
    status: PasskeyVerificationStatus
    strategy: PasskeyVerificationStrategy
    attempts: Nullable[int]
    expire_at: Nullable[int]
    nonce: NotRequired[Nonce]
    message: NotRequired[Nullable[str]]
    verified_at_client: NotRequired[Nullable[str]]


class Passkey(BaseModel):
    status: PasskeyVerificationStatus

    strategy: PasskeyVerificationStrategy

    attempts: Nullable[int]

    expire_at: Nullable[int]

    nonce: Optional[Nonce] = None

    message: OptionalNullable[str] = UNSET

    verified_at_client: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["nonce", "message", "verified_at_client"]
        nullable_fields = ["attempts", "expire_at", "message", "verified_at_client"]
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


SchemasPasskeyVerificationTypedDict = PasskeyTypedDict


SchemasPasskeyVerification = Passkey


class SchemasPasskeyTypedDict(TypedDict):
    object: SchemasPasskeyObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    name: str
    last_used_at: int
    r"""Unix timestamp of when the passkey was last used.

    """
    verification: Nullable[SchemasPasskeyVerificationTypedDict]
    id: NotRequired[str]


class SchemasPasskey(BaseModel):
    object: SchemasPasskeyObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    name: str

    last_used_at: int
    r"""Unix timestamp of when the passkey was last used.

    """

    verification: Nullable[SchemasPasskeyVerification]

    id: Optional[str] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id"]
        nullable_fields = ["verification"]
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
