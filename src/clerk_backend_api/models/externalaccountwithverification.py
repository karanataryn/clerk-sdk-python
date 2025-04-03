"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
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
import pydantic
from pydantic import ConfigDict, model_serializer
from pydantic.functional_validators import PlainValidator
from typing import Any, Dict, Optional, Union
from typing_extensions import Annotated, NotRequired, TypeAliasType, TypedDict


class ExternalAccountWithVerificationObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    EXTERNAL_ACCOUNT = "external_account"
    FACEBOOK_ACCOUNT = "facebook_account"
    GOOGLE_ACCOUNT = "google_account"


class GoogleOneTapVerificationStatus(str, Enum):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"


class GoogleOneTapVerificationStrategy(str, Enum):
    GOOGLE_ONE_TAP = "google_one_tap"


class ClerkErrorErrorExternalAccountWithVerificationMetaTypedDict(TypedDict):
    pass


class ClerkErrorErrorExternalAccountWithVerificationMeta(BaseModel):
    pass


class GoogleOneTapErrorClerkErrorTypedDict(TypedDict):
    message: str
    long_message: str
    code: str
    meta: NotRequired[ClerkErrorErrorExternalAccountWithVerificationMetaTypedDict]
    clerk_trace_id: NotRequired[str]


class GoogleOneTapErrorClerkError(BaseModel):
    message: str

    long_message: str

    code: str

    meta: Optional[ClerkErrorErrorExternalAccountWithVerificationMeta] = None

    clerk_trace_id: Optional[str] = None


GoogleOneTapVerificationErrorTypedDict = GoogleOneTapErrorClerkErrorTypedDict


GoogleOneTapVerificationError = GoogleOneTapErrorClerkError


class GoogleOneTapTypedDict(TypedDict):
    status: GoogleOneTapVerificationStatus
    strategy: GoogleOneTapVerificationStrategy
    expire_at: Nullable[int]
    attempts: Nullable[int]
    verified_at_client: NotRequired[Nullable[str]]
    error: NotRequired[Nullable[GoogleOneTapVerificationErrorTypedDict]]


class GoogleOneTap(BaseModel):
    status: GoogleOneTapVerificationStatus

    strategy: GoogleOneTapVerificationStrategy

    expire_at: Nullable[int]

    attempts: Nullable[int]

    verified_at_client: OptionalNullable[str] = UNSET

    error: OptionalNullable[GoogleOneTapVerificationError] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["verified_at_client", "error"]
        nullable_fields = ["expire_at", "attempts", "verified_at_client", "error"]
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


class OauthVerificationStatus(str, Enum, metaclass=utils.OpenEnumMeta):
    UNVERIFIED = "unverified"
    VERIFIED = "verified"
    FAILED = "failed"
    EXPIRED = "expired"
    TRANSFERABLE = "transferable"


class ClerkErrorErrorMetaTypedDict(TypedDict):
    pass


class ClerkErrorErrorMeta(BaseModel):
    pass


class OauthErrorClerkErrorTypedDict(TypedDict):
    message: str
    long_message: str
    code: str
    meta: NotRequired[ClerkErrorErrorMetaTypedDict]
    clerk_trace_id: NotRequired[str]


class OauthErrorClerkError(BaseModel):
    message: str

    long_message: str

    code: str

    meta: Optional[ClerkErrorErrorMeta] = None

    clerk_trace_id: Optional[str] = None


VerificationErrorTypedDict = OauthErrorClerkErrorTypedDict


VerificationError = OauthErrorClerkError


class OauthTypedDict(TypedDict):
    status: OauthVerificationStatus
    strategy: str
    expire_at: int
    attempts: Nullable[int]
    external_verification_redirect_url: NotRequired[str]
    error: NotRequired[Nullable[VerificationErrorTypedDict]]
    verified_at_client: NotRequired[Nullable[str]]


class Oauth(BaseModel):
    status: Annotated[
        OauthVerificationStatus, PlainValidator(validate_open_enum(False))
    ]

    strategy: str

    expire_at: int

    attempts: Nullable[int]

    external_verification_redirect_url: Optional[str] = None

    error: OptionalNullable[VerificationError] = UNSET

    verified_at_client: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "external_verification_redirect_url",
            "error",
            "verified_at_client",
        ]
        nullable_fields = ["attempts", "error", "verified_at_client"]
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


ExternalAccountWithVerificationVerificationTypedDict = TypeAliasType(
    "ExternalAccountWithVerificationVerificationTypedDict",
    Union[GoogleOneTapTypedDict, OauthTypedDict],
)


ExternalAccountWithVerificationVerification = TypeAliasType(
    "ExternalAccountWithVerificationVerification", Union[GoogleOneTap, Oauth]
)


class ExternalAccountWithVerificationTypedDict(TypedDict):
    object: ExternalAccountWithVerificationObject
    r"""String representing the object's type. Objects of the same type share the same value."""
    id: str
    provider: str
    identification_id: str
    provider_user_id: str
    r"""The unique ID of the user in the external provider's system"""
    approved_scopes: str
    email_address: str
    first_name: str
    last_name: str
    public_metadata: Dict[str, Any]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    verification: Nullable[ExternalAccountWithVerificationVerificationTypedDict]
    avatar_url: NotRequired[str]
    r"""Please use `image_url` instead"""
    image_url: NotRequired[Nullable[str]]
    username: NotRequired[Nullable[str]]
    label: NotRequired[Nullable[str]]


class ExternalAccountWithVerification(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, extra="allow"
    )
    __pydantic_extra__: Dict[str, Any] = pydantic.Field(init=False)

    object: ExternalAccountWithVerificationObject
    r"""String representing the object's type. Objects of the same type share the same value."""

    id: str

    provider: str

    identification_id: str

    provider_user_id: str
    r"""The unique ID of the user in the external provider's system"""

    approved_scopes: str

    email_address: str

    first_name: str

    last_name: str

    public_metadata: Dict[str, Any]

    created_at: int
    r"""Unix timestamp of creation

    """

    updated_at: int
    r"""Unix timestamp of creation

    """

    verification: Nullable[ExternalAccountWithVerificationVerification]

    avatar_url: Annotated[
        Optional[str],
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ] = None
    r"""Please use `image_url` instead"""

    image_url: OptionalNullable[str] = UNSET

    username: OptionalNullable[str] = UNSET

    label: OptionalNullable[str] = UNSET

    @property
    def additional_properties(self):
        return self.__pydantic_extra__

    @additional_properties.setter
    def additional_properties(self, value):
        self.__pydantic_extra__ = value  # pyright: ignore[reportIncompatibleVariableOverride]

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["avatar_url", "image_url", "username", "label"]
        nullable_fields = ["verification", "image_url", "username", "label"]
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

        for k, v in serialized.items():
            m[k] = v

        return m
