"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsEngineRpmTypedDict(TypedDict):
    r"""Vehicle engine RPM reading."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""The revolutions per minute of the engine."""


class VehicleStatsEngineRpm(BaseModel):
    r"""Vehicle engine RPM reading."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""The revolutions per minute of the engine."""
