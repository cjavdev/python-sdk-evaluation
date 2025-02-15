"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsGpsOdometerMetersTypedDict(TypedDict):
    r"""Vehicle GPS odometer event."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""Number of meters the vehicle has traveled according to the GPS calculations and the manually-specified odometer reading."""


class VehicleStatsGpsOdometerMeters(BaseModel):
    r"""Vehicle GPS odometer event."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""Number of meters the vehicle has traveled according to the GPS calculations and the manually-specified odometer reading."""
