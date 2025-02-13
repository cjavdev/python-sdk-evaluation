"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBodyTypedDict(
    TypedDict
):
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""
    value: int
    r"""The supply or discharge air temperature reading in millidegree Celsius."""


class TrailerStatReeferSupplyAirTemperatureMilliCZone1TypeResponseBody(BaseModel):
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    value: int
    r"""The supply or discharge air temperature reading in millidegree Celsius."""
