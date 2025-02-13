"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .createuserrequest_roles import (
    CreateUserRequestRoles,
    CreateUserRequestRolesTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateUserRequestAuthType(str, Enum):
    r"""The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`."""

    DEFAULT = "default"
    SAML = "saml"


class UpdateUserRequestTypedDict(TypedDict):
    r"""The user update arguments"""

    auth_type: NotRequired[UpdateUserRequestAuthType]
    r"""The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`."""
    expire_at: NotRequired[str]
    r"""For users with temporary access, this is the expiration datetime in RFC3339 format"""
    name: NotRequired[str]
    r"""The first and last name of the user."""
    roles: NotRequired[List[CreateUserRequestRolesTypedDict]]
    r"""The list of roles that applies to this user. A user may have \"organizational\" roles, which apply to the user at the organizational level, and \"tag-specific\" roles, which apply to the user for a given tag."""


class UpdateUserRequest(BaseModel):
    r"""The user update arguments"""

    auth_type: Annotated[
        Optional[UpdateUserRequestAuthType], pydantic.Field(alias="authType")
    ] = None
    r"""The authentication type the user uses to authenticate. To use SAML this organization must have a configured SAML integration. Valid values: `default`, `saml`."""

    expire_at: Annotated[Optional[str], pydantic.Field(alias="expireAt")] = None
    r"""For users with temporary access, this is the expiration datetime in RFC3339 format"""

    name: Optional[str] = None
    r"""The first and last name of the user."""

    roles: Optional[List[CreateUserRequestRoles]] = None
    r"""The list of roles that applies to this user. A user may have \"organizational\" roles, which apply to the user at the organizational level, and \"tag-specific\" roles, which apply to the user for a given tag."""
