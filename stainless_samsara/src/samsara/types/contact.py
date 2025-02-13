# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Contact", "Data"]


class Data(BaseModel):
    id: str
    """ID of the contact."""

    email: str
    """Email address of the contact."""

    first_name: str = FieldInfo(alias="firstName")
    """First name of the contact."""

    last_name: str = FieldInfo(alias="lastName")
    """Last name of the contact."""

    phone: str
    """Phone number of the contact."""


class Contact(BaseModel):
    data: Optional[Data] = None
    """Information about a notification contact for alerts."""
