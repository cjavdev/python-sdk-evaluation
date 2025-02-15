"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetslocationlinkconfigobjectresponsebody import (
    AssetsLocationLinkConfigObjectResponseBody,
    AssetsLocationLinkConfigObjectResponseBodyTypedDict,
)
from .assetsnearlocationlinkconfigobjectresponsebody import (
    AssetsNearLocationLinkConfigObjectResponseBody,
    AssetsNearLocationLinkConfigObjectResponseBodyTypedDict,
)
from .assetsonroutelinkconfigobjectresponsebody import (
    AssetsOnRouteLinkConfigObjectResponseBody,
    AssetsOnRouteLinkConfigObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LiveSharingLinkFullResponseObjectResponseBodyType(str, Enum):
    r"""Type of the Live Sharing Link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`"""

    ASSETS_LOCATION = "assetsLocation"
    ASSETS_NEAR_LOCATION = "assetsNearLocation"
    ASSETS_ON_ROUTE = "assetsOnRoute"


class LiveSharingLinkFullResponseObjectResponseBodyTypedDict(TypedDict):
    r"""Live Sharing Link object"""

    id: str
    r"""Unique identifier for the Live Sharing Link."""
    live_sharing_url: str
    r"""The shareable URL of the vehicle's location."""
    name: str
    r"""Name of the Live Sharing Link."""
    type: LiveSharingLinkFullResponseObjectResponseBodyType
    r"""Type of the Live Sharing Link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`"""
    assets_location_link_config: NotRequired[
        AssetsLocationLinkConfigObjectResponseBodyTypedDict
    ]
    r"""Configuration details specific to the 'By Asset' Live Sharing Link."""
    assets_near_location_link_config: NotRequired[
        AssetsNearLocationLinkConfigObjectResponseBodyTypedDict
    ]
    r"""Configuration details specific to the 'By Location' Live Sharing Link."""
    assets_on_route_link_config: NotRequired[
        AssetsOnRouteLinkConfigObjectResponseBodyTypedDict
    ]
    r"""Configuration details specific to the 'By Recurring Route' Live Sharing Link."""
    description: NotRequired[str]
    r"""Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type)."""
    expires_at_time: NotRequired[str]
    r"""Date that this link expires, in RFC 3339 format."""


class LiveSharingLinkFullResponseObjectResponseBody(BaseModel):
    r"""Live Sharing Link object"""

    id: str
    r"""Unique identifier for the Live Sharing Link."""

    live_sharing_url: Annotated[str, pydantic.Field(alias="liveSharingUrl")]
    r"""The shareable URL of the vehicle's location."""

    name: str
    r"""Name of the Live Sharing Link."""

    type: LiveSharingLinkFullResponseObjectResponseBodyType
    r"""Type of the Live Sharing Link.  Valid values: `assetsLocation`, `assetsNearLocation`, `assetsOnRoute`"""

    assets_location_link_config: Annotated[
        Optional[AssetsLocationLinkConfigObjectResponseBody],
        pydantic.Field(alias="assetsLocationLinkConfig"),
    ] = None
    r"""Configuration details specific to the 'By Asset' Live Sharing Link."""

    assets_near_location_link_config: Annotated[
        Optional[AssetsNearLocationLinkConfigObjectResponseBody],
        pydantic.Field(alias="assetsNearLocationLinkConfig"),
    ] = None
    r"""Configuration details specific to the 'By Location' Live Sharing Link."""

    assets_on_route_link_config: Annotated[
        Optional[AssetsOnRouteLinkConfigObjectResponseBody],
        pydantic.Field(alias="assetsOnRouteLinkConfig"),
    ] = None
    r"""Configuration details specific to the 'By Recurring Route' Live Sharing Link."""

    description: Optional[str] = None
    r"""Description for the Live Sharing Link (not applicable for 'assetsOnRoute' type)."""

    expires_at_time: Annotated[Optional[str], pydantic.Field(alias="expiresAtTime")] = (
        None
    )
    r"""Date that this link expires, in RFC 3339 format."""
