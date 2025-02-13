"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehiclelocation import VehicleLocation, VehicleLocationTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class VehicleLocationsListResponseDataTypedDict(TypedDict):
    r"""A vehicle and its list of location events."""

    id: str
    r"""The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed."""
    locations: List[VehicleLocationTypedDict]
    r"""A list of location events for the given vehicle."""
    name: str
    r"""The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""


class VehicleLocationsListResponseData(BaseModel):
    r"""A vehicle and its list of location events."""

    id: str
    r"""The unique Samsara ID of the Vehicle. This is automatically generated when the Vehicle object is created. It cannot be changed."""

    locations: List[VehicleLocation]
    r"""A list of location events for the given vehicle."""

    name: str
    r"""The human-readable name of the Vehicle. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. **By default**, this name is the serial number of the Samsara Vehicle Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""
