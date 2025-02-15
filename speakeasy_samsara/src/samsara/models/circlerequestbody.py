"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class CircleRequestBodyTypedDict(TypedDict):
    r"""Information about a circular geofence. This field is only needed if the geofence is a circle."""

    name: str
    r"""The name of the cirlce."""
    radius_meters: int
    r"""The radius of the circular geofence in meters."""
    latitude: NotRequired[float]
    r"""Latitude of the address. Will be geocoded from formattedAddress if not provided."""
    longitude: NotRequired[float]
    r"""Longitude of the address. Will be geocoded from formattedAddress if not provided."""


class CircleRequestBody(BaseModel):
    r"""Information about a circular geofence. This field is only needed if the geofence is a circle."""

    name: str
    r"""The name of the cirlce."""

    radius_meters: Annotated[int, pydantic.Field(alias="radiusMeters")]
    r"""The radius of the circular geofence in meters."""

    latitude: Optional[float] = None
    r"""Latitude of the address. Will be geocoded from formattedAddress if not provided."""

    longitude: Optional[float] = None
    r"""Longitude of the address. Will be geocoded from formattedAddress if not provided."""
