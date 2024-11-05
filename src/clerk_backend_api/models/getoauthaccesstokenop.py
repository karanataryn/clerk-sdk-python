"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from pydantic import model_serializer
from typing import Any, Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetOAuthAccessTokenRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user for which to retrieve the OAuth access token"""
    provider: str
    r"""The ID of the OAuth provider (e.g. `oauth_google`)"""


class GetOAuthAccessTokenRequest(BaseModel):
    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user for which to retrieve the OAuth access token"""

    provider: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the OAuth provider (e.g. `oauth_google`)"""


class ResponseBodyTypedDict(TypedDict):
    object: NotRequired[str]
    external_account_id: NotRequired[str]
    r"""External account ID"""
    provider_user_id: NotRequired[str]
    r"""The unique ID of the user in the external provider's system"""
    token: NotRequired[str]
    r"""The access token"""
    provider: NotRequired[str]
    r"""The ID of the provider"""
    public_metadata: NotRequired[Dict[str, Any]]
    label: NotRequired[Nullable[str]]
    scopes: NotRequired[List[str]]
    r"""The list of scopes that the token is valid for.
    Only present for OAuth 2.0 tokens.
    """
    token_secret: NotRequired[str]
    r"""The token secret. Only present for OAuth 1.0 tokens."""


class ResponseBody(BaseModel):
    object: Optional[str] = None

    external_account_id: Optional[str] = None
    r"""External account ID"""

    provider_user_id: Optional[str] = None
    r"""The unique ID of the user in the external provider's system"""

    token: Optional[str] = None
    r"""The access token"""

    provider: Optional[str] = None
    r"""The ID of the provider"""

    public_metadata: Optional[Dict[str, Any]] = None

    label: OptionalNullable[str] = UNSET

    scopes: Optional[List[str]] = None
    r"""The list of scopes that the token is valid for.
    Only present for OAuth 2.0 tokens.
    """

    token_secret: Optional[str] = None
    r"""The token secret. Only present for OAuth 1.0 tokens."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "object",
            "external_account_id",
            "provider_user_id",
            "token",
            "provider",
            "public_metadata",
            "label",
            "scopes",
            "token_secret",
        ]
        nullable_fields = ["label"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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
