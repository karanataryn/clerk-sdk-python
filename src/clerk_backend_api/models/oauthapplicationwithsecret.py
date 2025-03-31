"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
import pydantic
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class OAuthApplicationWithSecretObject(str, Enum):
    OAUTH_APPLICATION = "oauth_application"


class OAuthApplicationWithSecretTypedDict(TypedDict):
    object: OAuthApplicationWithSecretObject
    id: str
    instance_id: str
    name: str
    client_id: str
    public: bool
    scopes: str
    redirect_uris: List[str]
    callback_url: str
    r"""Deprecated: Use redirect_uris instead.

    """
    authorize_url: str
    token_fetch_url: str
    user_info_url: str
    discovery_url: str
    token_introspection_url: str
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    client_secret: NotRequired[str]
    r"""Empty if public client.

    """


class OAuthApplicationWithSecret(BaseModel):
    object: OAuthApplicationWithSecretObject

    id: str

    instance_id: str

    name: str

    client_id: str

    public: bool

    scopes: str

    redirect_uris: List[str]

    callback_url: Annotated[
        str,
        pydantic.Field(
            deprecated="warning: ** DEPRECATED ** - This will be removed in a future release, please migrate away from it as soon as possible."
        ),
    ]
    r"""Deprecated: Use redirect_uris instead.

    """

    authorize_url: str

    token_fetch_url: str

    user_info_url: str

    discovery_url: str

    token_introspection_url: str

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    client_secret: Optional[str] = None
    r"""Empty if public client.

    """
