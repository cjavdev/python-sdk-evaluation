# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LiveShareCreateParams",
    "AssetsLocationLinkConfig",
    "AssetsLocationLinkConfigLocation",
    "AssetsNearLocationLinkConfig",
    "AssetsOnRouteLinkConfig",
]


class LiveShareCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the Live Sharing Link."""

    type: Required[Literal["assetsLocation", "assetsNearLocation", "assetsOnRoute"]]
    """Type of the Live Sharing Link.

    This field specifies which one of '<type>LinkConfig' objects will be used to
    configure the sharing link. Valid values: `assetsLocation`,
    `assetsNearLocation`, `assetsOnRoute`
    """

    assets_location_link_config: Annotated[AssetsLocationLinkConfig, PropertyInfo(alias="assetsLocationLinkConfig")]
    """Configuration details specific to the 'By Asset' Live Sharing Link."""

    assets_near_location_link_config: Annotated[
        AssetsNearLocationLinkConfig, PropertyInfo(alias="assetsNearLocationLinkConfig")
    ]
    """Configuration details specific to the 'By Location' Live Sharing Link."""

    assets_on_route_link_config: Annotated[AssetsOnRouteLinkConfig, PropertyInfo(alias="assetsOnRouteLinkConfig")]
    """Configuration details specific to the 'By Recurring Route' Live Sharing Link."""

    description: str
    """
    Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type).
    """

    expires_at_time: Annotated[str, PropertyInfo(alias="expiresAtTime")]
    """Date that this link expires in RFC 3339 format.

    Can't be set in the past. If not provided then link will never expire.
    """


class AssetsLocationLinkConfigLocation(TypedDict, total=False):
    formatted_address: Required[Annotated[str, PropertyInfo(alias="formattedAddress")]]
    """Formatted address of a location"""

    latitude: Required[float]
    """Latitude of a location"""

    longitude: Required[float]
    """Longitude of a location"""

    name: Required[str]
    """Name of a location"""


class AssetsLocationLinkConfig(TypedDict, total=False):
    asset_id: Required[Annotated[str, PropertyInfo(alias="assetId")]]
    """Unique assets ID that Live Sharing Link will show."""

    location: AssetsLocationLinkConfigLocation
    """
    Location object that indicates what address information (destination point
    and/or ETA) will be shown by Live Sharing Link.
    """


class AssetsNearLocationLinkConfig(TypedDict, total=False):
    address_id: Required[Annotated[str, PropertyInfo(alias="addressId")]]
    """ID of the address.

    Can be either a unique Samsara ID or an external ID for the address.
    """


class AssetsOnRouteLinkConfig(TypedDict, total=False):
    recurring_route_id: Required[Annotated[str, PropertyInfo(alias="recurringRouteId")]]
    """Samsara ID of the recurring route."""
