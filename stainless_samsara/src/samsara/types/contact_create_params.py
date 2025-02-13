# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContactCreateParams"]


class ContactCreateParams(TypedDict, total=False):
    email: str
    """Email address of the contact."""

    first_name: Annotated[str, PropertyInfo(alias="firstName")]
    """First name of the contact."""

    last_name: Annotated[str, PropertyInfo(alias="lastName")]
    """Last name of the contact."""

    phone: str
    """Phone number of the contact."""
