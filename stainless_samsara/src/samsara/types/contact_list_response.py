# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ContactListResponse", "Data", "Pagination"]


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


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class ContactListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
