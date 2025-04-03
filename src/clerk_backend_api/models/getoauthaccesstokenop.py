"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class GetOAuthAccessTokenRequestTypedDict(TypedDict):
    user_id: str
    r"""The ID of the user for which to retrieve the OAuth access token"""
    provider: str
    r"""The ID of the OAuth provider (e.g. `oauth_google`)"""
    paginated: NotRequired[bool]
    r"""Whether to paginate the results.
    If true, the results will be paginated.
    If false, the results will not be paginated.
    """
    limit: NotRequired[int]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[int]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """


class GetOAuthAccessTokenRequest(BaseModel):
    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user for which to retrieve the OAuth access token"""

    provider: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the OAuth provider (e.g. `oauth_google`)"""

    paginated: Annotated[
        Optional[bool],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None
    r"""Whether to paginate the results.
    If true, the results will be paginated.
    If false, the results will not be paginated.
    """

    limit: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """

    offset: Annotated[
        Optional[int],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
