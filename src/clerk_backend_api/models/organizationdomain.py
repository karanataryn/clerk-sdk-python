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


class OrganizationDomainObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value. Always `organization_domain`"""

    ORGANIZATION_DOMAIN = "organization_domain"


class EnrollmentMode(str, Enum):
    r"""Mode of enrollment for the domain"""

    MANUAL_INVITATION = "manual_invitation"
    AUTOMATIC_INVITATION = "automatic_invitation"
    AUTOMATIC_SUGGESTION = "automatic_suggestion"


class OrganizationDomainStatus(str, Enum):
    r"""Status of the verification. It can be `unverified` or `verified`"""

    UNVERIFIED = "unverified"
    VERIFIED = "verified"


class OrganizationDomainVerificationTypedDict(TypedDict):
    r"""Verification details for the domain"""

    status: NotRequired[OrganizationDomainStatus]
    r"""Status of the verification. It can be `unverified` or `verified`"""
    strategy: NotRequired[str]
    r"""Name of the strategy used to verify the domain"""
    attempts: NotRequired[int]
    r"""How many attempts have been made to verify the domain"""
    expire_at: NotRequired[Nullable[int]]
    r"""Unix timestamp of when the verification will expire"""


class OrganizationDomainVerification(BaseModel):
    r"""Verification details for the domain"""

    status: Optional[OrganizationDomainStatus] = None
    r"""Status of the verification. It can be `unverified` or `verified`"""

    strategy: Optional[str] = None
    r"""Name of the strategy used to verify the domain"""

    attempts: Optional[int] = None
    r"""How many attempts have been made to verify the domain"""

    expire_at: OptionalNullable[int] = UNSET
    r"""Unix timestamp of when the verification will expire"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["status", "strategy", "attempts", "expire_at"]
        nullable_fields = ["expire_at"]
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


class OrganizationDomainTypedDict(TypedDict):
    r"""An organization domain"""

    id: NotRequired[str]
    r"""Unique identifier for the organization domain"""
    object: NotRequired[OrganizationDomainObject]
    r"""String representing the object's type. Objects of the same type share the same value. Always `organization_domain`

    """
    organization_id: NotRequired[str]
    r"""Unique identifier for the organization"""
    name: NotRequired[str]
    r"""Name of the organization domain"""
    enrollment_mode: NotRequired[EnrollmentMode]
    r"""Mode of enrollment for the domain"""
    affiliation_email_address: NotRequired[Nullable[str]]
    r"""Affiliation email address for the domain, if available."""
    verification: NotRequired[Nullable[OrganizationDomainVerificationTypedDict]]
    r"""Verification details for the domain"""
    total_pending_invitations: NotRequired[int]
    r"""Total number of pending invitations associated with this domain"""
    total_pending_suggestions: NotRequired[int]
    r"""Total number of pending suggestions associated with this domain"""
    created_at: NotRequired[int]
    r"""Unix timestamp when the domain was created"""
    updated_at: NotRequired[int]
    r"""Unix timestamp of the last update to the domain"""


class OrganizationDomain(BaseModel):
    r"""An organization domain"""

    id: Optional[str] = None
    r"""Unique identifier for the organization domain"""

    object: Optional[OrganizationDomainObject] = None
    r"""String representing the object's type. Objects of the same type share the same value. Always `organization_domain`

    """

    organization_id: Optional[str] = None
    r"""Unique identifier for the organization"""

    name: Optional[str] = None
    r"""Name of the organization domain"""

    enrollment_mode: Optional[EnrollmentMode] = None
    r"""Mode of enrollment for the domain"""

    affiliation_email_address: OptionalNullable[str] = UNSET
    r"""Affiliation email address for the domain, if available."""

    verification: OptionalNullable[OrganizationDomainVerification] = UNSET
    r"""Verification details for the domain"""

    total_pending_invitations: Optional[int] = None
    r"""Total number of pending invitations associated with this domain"""

    total_pending_suggestions: Optional[int] = None
    r"""Total number of pending suggestions associated with this domain"""

    created_at: Optional[int] = None
    r"""Unix timestamp when the domain was created"""

    updated_at: Optional[int] = None
    r"""Unix timestamp of the last update to the domain"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "object",
            "organization_id",
            "name",
            "enrollment_mode",
            "affiliation_email_address",
            "verification",
            "total_pending_invitations",
            "total_pending_suggestions",
            "created_at",
            "updated_at",
        ]
        nullable_fields = ["affiliation_email_address", "verification"]
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
