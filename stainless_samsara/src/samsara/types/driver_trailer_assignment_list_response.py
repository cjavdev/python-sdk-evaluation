# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DriverTrailerAssignmentListResponse", "Data", "DataDriver", "DataTrailer", "Pagination"]


class DataDriver(BaseModel):
    driver_id: str = FieldInfo(alias="driverId")
    """Samsara ID of the driver."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class DataTrailer(BaseModel):
    trailer_id: str = FieldInfo(alias="trailerId")
    """Samsara ID of the trailer."""


class Data(BaseModel):
    id: str
    """Samsara ID of the driver trailer assignment."""

    driver: DataDriver
    """A driver object with an id and map of external ids."""

    start_time: str = FieldInfo(alias="startTime")
    """Time when the driver trailer assignment starts, in RFC 3339 format."""

    trailer: DataTrailer
    """A trailer asset object associate with the assigment."""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Time when the driver trailer assignment was created, in RFC 3339 format."""

    end_time: Optional[str] = FieldInfo(alias="endTime", default=None)
    """Time when the driver trailer assignment will end, in RFC 3339 format."""

    updated_at_time: Optional[str] = FieldInfo(alias="updatedAtTime", default=None)
    """Time when the driver trailer assignment was last updated, in RFC 3339 format."""


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


class DriverTrailerAssignmentListResponse(BaseModel):
    data: List[Data]
    """
    List of driver trailer assignment objects and their respective driver and
    trailer info.
    """

    pagination: Pagination
    """Pagination parameters."""
