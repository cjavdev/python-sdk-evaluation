# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .v1_trailer_assignments_response import V1TrailerAssignmentsResponse

__all__ = ["InlineResponse200_7", "Pagination"]


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's
    'startingAfter' query parameter.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """True if there are more pages of results after this response."""

    has_prev_page: bool = FieldInfo(alias="hasPrevPage")
    """True if there are more pages of results before this response."""

    start_cursor: str = FieldInfo(alias="startCursor")
    """Cursor identifier representing the first element in the response.

    This value should be used in conjunction with a subsequent request's
    'ending_before' query parameter.
    """


class InlineResponse200_7(BaseModel):
    pagination: Optional[Pagination] = None

    trailers: Optional[List[V1TrailerAssignmentsResponse]] = None
