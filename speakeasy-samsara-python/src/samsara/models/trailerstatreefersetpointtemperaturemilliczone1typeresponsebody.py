"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBodyTypedDict(
    TypedDict
):
    r"""Set point temperature of zone 1 of the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""
    value: int
    r"""The set point temperature reading in millidegree Celsius."""


class TrailerStatReeferSetPointTemperatureMilliCZone1TypeResponseBody(BaseModel):
    r"""Set point temperature of zone 1 of the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    value: int
    r"""The set point temperature reading in millidegree Celsius."""
