"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class AddressGeofencePolygonVerticesTypedDict(TypedDict):
    latitude: float
    r"""The latitude of a geofence vertex in decimal degrees."""
    longitude: float
    r"""The longitude of a geofence vertex in decimal degrees."""


class AddressGeofencePolygonVertices(BaseModel):
    latitude: float
    r"""The latitude of a geofence vertex in decimal degrees."""

    longitude: float
    r"""The longitude of a geofence vertex in decimal degrees."""
