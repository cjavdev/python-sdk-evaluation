"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .reversegeoobjectresponsebody import (
    ReverseGeoObjectResponseBody,
    ReverseGeoObjectResponseBodyTypedDict,
)
from .trailerstatdecorationresponsebody import (
    TrailerStatDecorationResponseBody,
    TrailerStatDecorationResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TrailerStatGpsWithDecorationsTypeResponseBodyTypedDict(TypedDict):
    r"""GPS location data for the trailer."""

    latitude: float
    r"""GPS latitude represented in degrees."""
    longitude: float
    r"""GPS longitude represented in degrees."""
    time: str
    r"""UTC timestamp in RFC 3339 format."""
    decorations: NotRequired[TrailerStatDecorationResponseBodyTypedDict]
    r"""Decorated values for the primary trailer stat datapoints."""
    heading_degrees: NotRequired[int]
    r"""Heading of the trailer in degrees."""
    reverse_geo: NotRequired[ReverseGeoObjectResponseBodyTypedDict]
    r"""Reverse geocoded information"""
    speed_miles_per_hour: NotRequired[int]
    r"""GPS speed of the trailer in miles per hour."""


class TrailerStatGpsWithDecorationsTypeResponseBody(BaseModel):
    r"""GPS location data for the trailer."""

    latitude: float
    r"""GPS latitude represented in degrees."""

    longitude: float
    r"""GPS longitude represented in degrees."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    decorations: Optional[TrailerStatDecorationResponseBody] = None
    r"""Decorated values for the primary trailer stat datapoints."""

    heading_degrees: Annotated[
        Optional[int], pydantic.Field(alias="headingDegrees")
    ] = None
    r"""Heading of the trailer in degrees."""

    reverse_geo: Annotated[
        Optional[ReverseGeoObjectResponseBody], pydantic.Field(alias="reverseGeo")
    ] = None
    r"""Reverse geocoded information"""

    speed_miles_per_hour: Annotated[
        Optional[int], pydantic.Field(alias="speedMilesPerHour")
    ] = None
    r"""GPS speed of the trailer in miles per hour."""
