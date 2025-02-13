"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsResponseSpreaderAirTempTypedDict(TypedDict):
    r"""Air (ambient) temperature in milli celsius reading from material spreader."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""Air (ambient) temperature in milli celsius reading from material spreader."""


class VehicleStatsResponseSpreaderAirTemp(BaseModel):
    r"""Air (ambient) temperature in milli celsius reading from material spreader."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""Air (ambient) temperature in milli celsius reading from material spreader."""
