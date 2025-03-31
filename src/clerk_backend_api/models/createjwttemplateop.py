"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateJWTTemplateClaimsTypedDict(TypedDict):
    r"""JWT template claims in JSON format"""


class CreateJWTTemplateClaims(BaseModel):
    r"""JWT template claims in JSON format"""


class CreateJWTTemplateRequestBodyTypedDict(TypedDict):
    name: str
    r"""JWT template name"""
    claims: CreateJWTTemplateClaimsTypedDict
    r"""JWT template claims in JSON format"""
    lifetime: NotRequired[Nullable[float]]
    r"""JWT token lifetime"""
    allowed_clock_skew: NotRequired[Nullable[float]]
    r"""JWT token allowed clock skew"""
    custom_signing_key: NotRequired[bool]
    r"""Whether a custom signing key/algorithm is also provided for this template"""
    signing_algorithm: NotRequired[Nullable[str]]
    r"""The custom signing algorithm to use when minting JWTs. Required if `custom_signing_key` is `true`."""
    signing_key: NotRequired[Nullable[str]]
    r"""The custom signing private key to use when minting JWTs. Required if `custom_signing_key` is `true`."""


class CreateJWTTemplateRequestBody(BaseModel):
    name: str
    r"""JWT template name"""

    claims: CreateJWTTemplateClaims
    r"""JWT template claims in JSON format"""

    lifetime: OptionalNullable[float] = UNSET
    r"""JWT token lifetime"""

    allowed_clock_skew: OptionalNullable[float] = UNSET
    r"""JWT token allowed clock skew"""

    custom_signing_key: Optional[bool] = None
    r"""Whether a custom signing key/algorithm is also provided for this template"""

    signing_algorithm: OptionalNullable[str] = UNSET
    r"""The custom signing algorithm to use when minting JWTs. Required if `custom_signing_key` is `true`."""

    signing_key: OptionalNullable[str] = UNSET
    r"""The custom signing private key to use when minting JWTs. Required if `custom_signing_key` is `true`."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "lifetime",
            "allowed_clock_skew",
            "custom_signing_key",
            "signing_algorithm",
            "signing_key",
        ]
        nullable_fields = [
            "lifetime",
            "allowed_clock_skew",
            "signing_algorithm",
            "signing_key",
        ]
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
