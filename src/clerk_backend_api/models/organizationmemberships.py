"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationmembership import (
    OrganizationMembership,
    OrganizationMembershipTypedDict,
)
from clerk_backend_api.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OrganizationMembershipsTypedDict(TypedDict):
    r"""A list of organization memberships"""

    data: List[OrganizationMembershipTypedDict]
    total_count: int
    r"""Total number of organization memberships

    """


class OrganizationMemberships(BaseModel):
    r"""A list of organization memberships"""

    data: List[OrganizationMembership]

    total_count: int
    r"""Total number of organization memberships

    """
