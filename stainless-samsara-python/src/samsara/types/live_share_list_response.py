# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "LiveShareListResponse",
    "Data",
    "DataAssetsLocationLinkConfig",
    "DataAssetsLocationLinkConfigLocation",
    "DataAssetsNearLocationLinkConfig",
    "DataAssetsOnRouteLinkConfig",
    "Pagination",
]


class DataAssetsLocationLinkConfigLocation(BaseModel):
    formatted_address: str = FieldInfo(alias="formattedAddress")
    """Formatted address of a location"""

    latitude: float
    """Latitude of a location"""

    longitude: float
    """Longitude of a location"""

    name: str
    """Name of a location"""


class DataAssetsLocationLinkConfig(BaseModel):
    asset_id: str = FieldInfo(alias="assetId")
    """Unique assets ID that Live Sharing Link will show."""

    location: Optional[DataAssetsLocationLinkConfigLocation] = None
    """
    Location object that indicates what address information (destination point
    and/or ETA) will be shown by Live Sharing Link.
    """


class DataAssetsNearLocationLinkConfig(BaseModel):
    address_id: str = FieldInfo(alias="addressId")
    """ID of the address.

    Can be either a unique Samsara ID or an external ID for the address.
    """


class DataAssetsOnRouteLinkConfig(BaseModel):
    recurring_route_id: str = FieldInfo(alias="recurringRouteId")
    """Samsara ID of the recurring route."""


class Data(BaseModel):
    id: str
    """Unique identifier for the Live Sharing Link."""

    live_sharing_url: str = FieldInfo(alias="liveSharingUrl")
    """The shareable URL of the vehicle's location."""

    name: str
    """Name of the Live Sharing Link."""

    type: Literal["assetsLocation", "assetsNearLocation", "assetsOnRoute"]
    """Type of the Live Sharing Link.

    Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`
    """

    assets_location_link_config: Optional[DataAssetsLocationLinkConfig] = FieldInfo(
        alias="assetsLocationLinkConfig", default=None
    )
    """Configuration details specific to the 'By Asset' Live Sharing Link."""

    assets_near_location_link_config: Optional[DataAssetsNearLocationLinkConfig] = FieldInfo(
        alias="assetsNearLocationLinkConfig", default=None
    )
    """Configuration details specific to the 'By Location' Live Sharing Link."""

    assets_on_route_link_config: Optional[DataAssetsOnRouteLinkConfig] = FieldInfo(
        alias="assetsOnRouteLinkConfig", default=None
    )
    """Configuration details specific to the 'By Recurring Route' Live Sharing Link."""

    description: Optional[str] = None
    """
    Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    """

    expires_at_time: Optional[str] = FieldInfo(alias="expiresAtTime", default=None)
    """Date that this link expires, in RFC 3339 format."""


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


class LiveShareListResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
    """Pagination parameters."""
