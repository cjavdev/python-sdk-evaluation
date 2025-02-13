# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["VehicleLocationsResponse", "Data", "DataLocation", "DataLocationReverseGeo", "Pagination"]


class DataLocationReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataLocation(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    heading: Optional[float] = None
    """Heading of the vehicle in degrees."""

    reverse_geo: Optional[DataLocationReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information."""

    speed: Optional[float] = None
    """GPS speed of the vehicle in miles per hour.

    See `isEcuSpeed` to determine speed data source.
    """


class Data(BaseModel):
    id: str
    """The unique Samsara ID of the Vehicle.

    This is automatically generated when the Vehicle object is created. It cannot be
    changed.
    """

    location: DataLocation
    """Vehicle location event."""

    name: str
    """The human-readable name of the Vehicle.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. **By default**, this name is
    the serial number of the Samsara Vehicle Gateway. It can be set or updated
    through the Samsara Dashboard or through the API at any time.
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


class VehicleLocationsResponse(BaseModel):
    data: List[Data]
    """List of the most recent locations for the specified vehicles."""

    pagination: Pagination
    """Pagination parameters."""
