"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Any, Dict, Optional
from typing_extensions import NotRequired, TypedDict


class OrganizationInvitationWithPublicOrganizationDataObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    ORGANIZATION_INVITATION = "organization_invitation"


class PublicOrganizationDataTypedDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    slug: NotRequired[str]
    image_url: NotRequired[str]
    has_image: NotRequired[bool]


class PublicOrganizationData(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    image_url: Optional[str] = None

    has_image: Optional[bool] = None


class OrganizationInvitationWithPublicOrganizationDataTypedDict(TypedDict):
    r"""An organization invitation with public organization data populated"""

    id: NotRequired[str]
    object: NotRequired[OrganizationInvitationWithPublicOrganizationDataObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    email_address: NotRequired[str]
    role: NotRequired[str]
    role_name: NotRequired[str]
    organization_id: NotRequired[str]
    status: NotRequired[str]
    public_metadata: NotRequired[Dict[str, Any]]
    private_metadata: NotRequired[Dict[str, Any]]
    public_organization_data: NotRequired[PublicOrganizationDataTypedDict]
    created_at: NotRequired[int]
    r"""Unix timestamp of creation."""
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update."""


class OrganizationInvitationWithPublicOrganizationData(BaseModel):
    r"""An organization invitation with public organization data populated"""

    id: Optional[str] = None

    object: Optional[OrganizationInvitationWithPublicOrganizationDataObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    email_address: Optional[str] = None

    role: Optional[str] = None

    role_name: Optional[str] = None

    organization_id: Optional[str] = None

    status: Optional[str] = None

    public_metadata: Optional[Dict[str, Any]] = None

    private_metadata: Optional[Dict[str, Any]] = None

    public_organization_data: Optional[PublicOrganizationData] = None

    created_at: Optional[int] = None
    r"""Unix timestamp of creation."""

    updated_at: Optional[int] = None
    r"""Unix timestamp of last update."""
