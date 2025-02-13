# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListUserRolesResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: Optional[str] = None
    """The unique ID for the role."""

    name: Optional[str] = None
    """The name of the role."""


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


class ListUserRolesResponse(BaseModel):
    data: Optional[List[Data]] = None
    """A list of user roles"""

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
