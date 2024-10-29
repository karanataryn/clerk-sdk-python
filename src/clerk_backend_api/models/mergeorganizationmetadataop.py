"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class MergeOrganizationMetadataRequestBodyTypedDict(TypedDict):
    public_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata saved on the organization, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """
    private_metadata: NotRequired[Dict[str, Any]]
    r"""Metadata saved on the organization that is only visible to your backend.
    The new object will be merged with the existing value.
    """
    

class MergeOrganizationMetadataRequestBody(BaseModel):
    public_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata saved on the organization, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """
    private_metadata: Optional[Dict[str, Any]] = None
    r"""Metadata saved on the organization that is only visible to your backend.
    The new object will be merged with the existing value.
    """
    

class MergeOrganizationMetadataRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization for which metadata will be merged or updated"""
    request_body: MergeOrganizationMetadataRequestBodyTypedDict
    

class MergeOrganizationMetadataRequest(BaseModel):
    organization_id: Annotated[str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""The ID of the organization for which metadata will be merged or updated"""
    request_body: Annotated[MergeOrganizationMetadataRequestBody, FieldMetadata(request=RequestMetadata(media_type="application/json"))]
    
