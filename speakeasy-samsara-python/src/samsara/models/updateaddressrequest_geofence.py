"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .addressgeofence_circle import (
    AddressGeofenceCircle,
    AddressGeofenceCircleTypedDict,
)
from .addressgeofence_polygon import (
    AddressGeofencePolygon,
    AddressGeofencePolygonTypedDict,
)
from .addressgeofence_settings import (
    AddressGeofenceSettings,
    AddressGeofenceSettingsTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class UpdateAddressRequestGeofenceTypedDict(TypedDict):
    r"""The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both."""

    circle: NotRequired[AddressGeofenceCircleTypedDict]
    r"""Information about a circular geofence. This field is only needed if the geofence is a circle."""
    polygon: NotRequired[AddressGeofencePolygonTypedDict]
    r"""Information about a polygon geofence. This field is only needed if the geofence is a polygon."""
    settings: NotRequired[AddressGeofenceSettingsTypedDict]
    r"""Information about a geofence's settings."""


class UpdateAddressRequestGeofence(BaseModel):
    r"""The geofence that defines this address and its bounds. This can either be a circle or a polygon, but not both."""

    circle: Optional[AddressGeofenceCircle] = None
    r"""Information about a circular geofence. This field is only needed if the geofence is a circle."""

    polygon: Optional[AddressGeofencePolygon] = None
    r"""Information about a polygon geofence. This field is only needed if the geofence is a polygon."""

    settings: Optional[AddressGeofenceSettings] = None
    r"""Information about a geofence's settings."""
