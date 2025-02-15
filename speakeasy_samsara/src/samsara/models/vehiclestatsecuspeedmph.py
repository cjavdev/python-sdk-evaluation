"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsEcuSpeedMphTypedDict(TypedDict):
    r"""The speed of the vehicle in miles per hour, as reported by the ECU."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: float
    r"""The speed of the vehicle in miles per hour."""


class VehicleStatsEcuSpeedMph(BaseModel):
    r"""The speed of the vehicle in miles per hour, as reported by the ECU."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: float
    r"""The speed of the vehicle in miles per hour."""
