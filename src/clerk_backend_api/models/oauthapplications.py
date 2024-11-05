"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .oauthapplication import OAuthApplication, OAuthApplicationTypedDict
from clerk_backend_api.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class OAuthApplicationsTypedDict(TypedDict):
    r"""A list of OAuth applications"""

    data: List[OAuthApplicationTypedDict]
    total_count: int
    r"""Total number of OAuth applications

    """


class OAuthApplications(BaseModel):
    r"""A list of OAuth applications"""

    data: List[OAuthApplication]

    total_count: int
    r"""Total number of OAuth applications

    """
