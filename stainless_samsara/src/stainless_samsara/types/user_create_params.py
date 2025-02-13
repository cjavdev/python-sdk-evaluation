# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserCreateParams", "Role"]


class UserCreateParams(TypedDict, total=False):
    auth_type: Required[Annotated[Literal["default", "saml"], PropertyInfo(alias="authType")]]
    """The authentication type the user uses to authenticate.

    To use SAML this organization must have a configured SAML integration. Valid
    values: `default`, `saml`.
    """

    email: Required[str]
    """The email address of this user."""

    name: Required[str]
    """The first and last name of the user."""

    roles: Required[Iterable[Role]]
    """The list of roles that applies to this user.

    A user may have "organizational" roles, which apply to the user at the
    organizational level, and "tag-specific" roles, which apply to the user for a
    given tag.
    """

    expire_at: Annotated[str, PropertyInfo(alias="expireAt")]
    """
    For users with temporary access, this is the expiration datetime in RFC3339
    format
    """


class Role(TypedDict, total=False):
    role_id: Required[Annotated[str, PropertyInfo(alias="roleId")]]
    """The unique ID for the role."""

    tag_id: Annotated[str, PropertyInfo(alias="tagId")]
    """ID of the tag this role applies to."""
