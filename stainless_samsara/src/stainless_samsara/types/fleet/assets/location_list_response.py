# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["LocationListResponse", "Asset", "AssetCable", "AssetLocation", "Pagination"]


class AssetCable(BaseModel):
    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Asset type"""


class AssetLocation(BaseModel):
    latitude: Optional[float] = None
    """The latitude of the location in degrees."""

    location: Optional[str] = None
    """The best effort (street,city,state) for the latitude and longitude."""

    longitude: Optional[float] = None
    """The longitude of the location in degrees."""

    speed_miles_per_hour: Optional[float] = FieldInfo(alias="speedMilesPerHour", default=None)
    """
    The speed calculated from GPS that the asset was traveling at in miles per hour.
    """

    time_ms: Optional[float] = FieldInfo(alias="timeMs", default=None)
    """Time in Unix milliseconds since epoch when the asset was at the location."""


class Asset(BaseModel):
    id: int
    """Asset ID"""

    asset_serial_number: Optional[str] = FieldInfo(alias="assetSerialNumber", default=None)
    """Asset serial number"""

    cable: Optional[AssetCable] = None
    """The cable connected to the asset"""

    engine_hours: Optional[int] = FieldInfo(alias="engineHours", default=None)
    """Engine hours"""

    location: Optional[List[AssetLocation]] = None
    """Current location of an asset"""

    name: Optional[str] = None
    """Asset name"""


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


class LocationListResponse(BaseModel):
    assets: Optional[List[Asset]] = None

    pagination: Optional[Pagination] = None
