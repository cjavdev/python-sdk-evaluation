"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsResponseEvBatteryVoltageMilliVoltTypedDict(TypedDict):
    r"""Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: int
    r"""Battery voltage for electric and hybrid vehicles in milli volts."""


class VehicleStatsResponseEvBatteryVoltageMilliVolt(BaseModel):
    r"""Battery voltage for electric and hybrid vehicles in milli volts. Not all EV and HEVs may report this field."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: int
    r"""Battery voltage for electric and hybrid vehicles in milli volts."""
