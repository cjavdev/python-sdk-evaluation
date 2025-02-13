# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserResponse", "Data", "DataRole", "DataRoleRole", "DataRoleTag"]


class DataRoleRole(BaseModel):
    id: Optional[str] = None
    """The unique ID for the role."""

    name: Optional[str] = None
    """The name of the role."""


class DataRoleTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataRole(BaseModel):
    expire_at: Optional[str] = FieldInfo(alias="expireAt", default=None)
    """For user account expiration, the access expiration datetime in RFC3339 format"""

    role: Optional[DataRoleRole] = None
    """A user role object."""

    tag: Optional[DataRoleTag] = None
    """A minified tag object"""


class Data(BaseModel):
    id: str
    """ID of the user."""

    auth_type: Literal["default", "saml"] = FieldInfo(alias="authType")
    """The authentication type the user uses to authenticate.

    To use SAML this organization must have a configured SAML integration. Valid
    values: `default`, `saml`.
    """

    email: str
    """The email address of this user."""

    name: str
    """The first and last name of the user."""

    roles: List[DataRole]
    """The list of roles that applies to this user.

    A user may have "organizational" roles, which apply to the user at the
    organizational level, and "tag-specific" roles, which apply to the user for a
    given tag.
    """


class UserResponse(BaseModel):
    data: Optional[Data] = None
    """A user object."""
