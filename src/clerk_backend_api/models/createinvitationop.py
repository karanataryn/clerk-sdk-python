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
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class CreateInvitationRequestBodyTypedDict(TypedDict):
    r"""Required parameters"""

    email_address: str
    r"""The email address the invitation will be sent to"""
    public_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata that will be attached to the newly created invitation.
    The value of this property should be a well-formed JSON object.
    Once the user accepts the invitation and signs up, these metadata will end up in the user's public metadata.
    """
    redirect_url: NotRequired[str]
    r"""Optional URL which specifies where to redirect the user once they click the invitation link.
    This is only required if you have implemented a [custom flow](https://clerk.com/docs/authentication/invitations#custom-flow) and you're not using Clerk Hosted Pages or Clerk Components.
    """
    notify: NotRequired[Nullable[bool]]
    r"""Optional flag which denotes whether an email invitation should be sent to the given email address.
    Defaults to true.
    """
    ignore_existing: NotRequired[Nullable[bool]]
    r"""Whether an invitation should be created if there is already an existing invitation for this email address, or it's claimed by another user."""
    expires_in_days: NotRequired[Nullable[int]]
    r"""The number of days the invitation will be valid for. By default, the invitation does not expire."""


class CreateInvitationRequestBody(BaseModel):
    r"""Required parameters"""

    email_address: str
    r"""The email address the invitation will be sent to"""

    public_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata that will be attached to the newly created invitation.
    The value of this property should be a well-formed JSON object.
    Once the user accepts the invitation and signs up, these metadata will end up in the user's public metadata.
    """

    redirect_url: Optional[str] = None
    r"""Optional URL which specifies where to redirect the user once they click the invitation link.
    This is only required if you have implemented a [custom flow](https://clerk.com/docs/authentication/invitations#custom-flow) and you're not using Clerk Hosted Pages or Clerk Components.
    """

    notify: OptionalNullable[bool] = True
    r"""Optional flag which denotes whether an email invitation should be sent to the given email address.
    Defaults to true.
    """

    ignore_existing: OptionalNullable[bool] = False
    r"""Whether an invitation should be created if there is already an existing invitation for this email address, or it's claimed by another user."""

    expires_in_days: OptionalNullable[int] = UNSET
    r"""The number of days the invitation will be valid for. By default, the invitation does not expire."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "public_metadata",
            "redirect_url",
            "notify",
            "ignore_existing",
            "expires_in_days",
        ]
        nullable_fields = ["notify", "ignore_existing", "expires_in_days"]
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
