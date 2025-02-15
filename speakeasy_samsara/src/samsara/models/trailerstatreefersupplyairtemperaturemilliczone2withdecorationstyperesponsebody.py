"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailerstatdecorationresponsebody import (
    TrailerStatDecorationResponseBody,
    TrailerStatDecorationResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TrailerStatReeferSupplyAirTemperatureMilliCZone2WithDecorationsTypeResponseBodyTypedDict(
    TypedDict
):
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""
    value: int
    r"""The supply or discharge air temperature reading in millidegree Celsius."""
    decorations: NotRequired[TrailerStatDecorationResponseBodyTypedDict]
    r"""Decorated values for the primary trailer stat datapoints."""


class TrailerStatReeferSupplyAirTemperatureMilliCZone2WithDecorationsTypeResponseBody(
    BaseModel
):
    r"""Supply or discharge air temperature of zone 2 of the reefer. This is the temperature of the air as it leaves the cooling unit."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    value: int
    r"""The supply or discharge air temperature reading in millidegree Celsius."""

    decorations: Optional[TrailerStatDecorationResponseBody] = None
    r"""Decorated values for the primary trailer stat datapoints."""
