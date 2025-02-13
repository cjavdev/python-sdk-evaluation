# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LocationHistoryResponse", "Data", "DataLocation", "Pagination"]


class DataLocation(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    heading: Optional[float] = None
    """Heading of the unit of equipment in degrees."""

    speed: Optional[float] = None
    """GPS speed of the unit of equipment in miles per hour."""


class Data(BaseModel):
    id: str
    """Unique Samsara ID for the equipment."""

    locations: List[DataLocation]
    """A time-series of location events for the given unit of equipment."""

    name: str
    """Name of the equipment."""


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


class LocationHistoryResponse(BaseModel):
    data: List[Data]
    """Time-series of locations for the specified units of equipment."""

    pagination: Pagination
    """Pagination parameters."""
