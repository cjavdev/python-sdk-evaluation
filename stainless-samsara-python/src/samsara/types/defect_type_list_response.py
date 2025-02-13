# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DefectTypeListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """The unique ID of the DVIR defect type."""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """Time when defect type was created in RFC 3339 format."""

    label: str
    """DVIR defect type label."""

    section_type: Literal[
        "exteriorFront",
        "exteriorRear",
        "exteriorSideUnderneath",
        "interiorDriverCab",
        "interiorPassengerArea",
        "other",
        "unknown",
    ] = FieldInfo(alias="sectionType")
    """Section for DVIR defect type.

    Valid values: `exteriorFront`, `exteriorRear`, `exteriorSideUnderneath`,
    `interiorDriverCab`, `interiorPassengerArea`, `other`, `unknown`
    """


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


class DefectTypeListResponse(BaseModel):
    data: List[Data]
    """List of defect types."""

    pagination: Pagination
    """Pagination parameters."""
