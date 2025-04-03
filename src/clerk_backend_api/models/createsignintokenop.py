"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class CreateSignInTokenRequestBodyTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user that can use the newly created sign in token"""
    expires_in_seconds: NotRequired[Nullable[int]]
    r"""Optional parameter to specify the life duration of the sign in token in seconds.
    By default, the duration is 30 days.
    """


class CreateSignInTokenRequestBody(BaseModel):
    user_id: str
    r"""The ID of the user that can use the newly created sign in token"""

    expires_in_seconds: OptionalNullable[int] = 2592000
    r"""Optional parameter to specify the life duration of the sign in token in seconds.
    By default, the duration is 30 days.
    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["expires_in_seconds"]
        nullable_fields = ["expires_in_seconds"]
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
