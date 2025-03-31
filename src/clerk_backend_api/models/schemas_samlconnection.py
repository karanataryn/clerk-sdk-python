"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .samlconnectionattributemapping import (
    SAMLConnectionAttributeMapping,
    SAMLConnectionAttributeMappingTypedDict,
)
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


class SchemasSAMLConnectionObject(str, Enum):
    SAML_CONNECTION = "saml_connection"


class SchemasSAMLConnectionTypedDict(TypedDict):
    object: SchemasSAMLConnectionObject
    id: str
    name: str
    domain: str
    idp_entity_id: Nullable[str]
    idp_sso_url: Nullable[str]
    idp_certificate: Nullable[str]
    acs_url: str
    sp_entity_id: str
    sp_metadata_url: str
    active: bool
    provider: str
    user_count: int
    sync_user_attributes: bool
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    idp_metadata_url: NotRequired[Nullable[str]]
    idp_metadata: NotRequired[Nullable[str]]
    organization_id: NotRequired[Nullable[str]]
    attribute_mapping: NotRequired[SAMLConnectionAttributeMappingTypedDict]
    allow_subdomains: NotRequired[bool]
    allow_idp_initiated: NotRequired[bool]
    disable_additional_identifications: NotRequired[bool]


class SchemasSAMLConnection(BaseModel):
    object: SchemasSAMLConnectionObject

    id: str

    name: str

    domain: str

    idp_entity_id: Nullable[str]

    idp_sso_url: Nullable[str]

    idp_certificate: Nullable[str]

    acs_url: str

    sp_entity_id: str

    sp_metadata_url: str

    active: bool

    provider: str

    user_count: int

    sync_user_attributes: bool

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    idp_metadata_url: OptionalNullable[str] = UNSET

    idp_metadata: OptionalNullable[str] = UNSET

    organization_id: OptionalNullable[str] = UNSET

    attribute_mapping: Optional[SAMLConnectionAttributeMapping] = None

    allow_subdomains: Optional[bool] = None

    allow_idp_initiated: Optional[bool] = None

    disable_additional_identifications: Optional[bool] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "idp_metadata_url",
            "idp_metadata",
            "organization_id",
            "attribute_mapping",
            "allow_subdomains",
            "allow_idp_initiated",
            "disable_additional_identifications",
        ]
        nullable_fields = [
            "idp_entity_id",
            "idp_sso_url",
            "idp_certificate",
            "idp_metadata_url",
            "idp_metadata",
            "organization_id",
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
