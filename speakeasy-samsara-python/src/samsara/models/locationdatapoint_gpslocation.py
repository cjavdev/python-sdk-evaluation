"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .locationdatapoint_gpslocation_place import (
    LocationDataPointGpsLocationPlace,
    LocationDataPointGpsLocationPlaceTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LocationDataPointGpsLocationTypedDict(TypedDict):
    r"""GPS location information of the data input's datapoint."""

    formatted_address: NotRequired[str]
    r"""Formatted address of the location"""
    gps_meters_per_second: NotRequired[float]
    r"""Speed of GPS (meters per second)"""
    heading_degrees: NotRequired[float]
    r"""Heading degrees"""
    latitude: NotRequired[float]
    r"""Latitude of the location"""
    longitude: NotRequired[float]
    r"""Longitude of the location"""
    place: NotRequired[LocationDataPointGpsLocationPlaceTypedDict]
    r"""Address of the location"""


class LocationDataPointGpsLocation(BaseModel):
    r"""GPS location information of the data input's datapoint."""

    formatted_address: Annotated[
        Optional[str], pydantic.Field(alias="formattedAddress")
    ] = None
    r"""Formatted address of the location"""

    gps_meters_per_second: Annotated[
        Optional[float], pydantic.Field(alias="gpsMetersPerSecond")
    ] = None
    r"""Speed of GPS (meters per second)"""

    heading_degrees: Annotated[
        Optional[float], pydantic.Field(alias="headingDegrees")
    ] = None
    r"""Heading degrees"""

    latitude: Optional[float] = None
    r"""Latitude of the location"""

    longitude: Optional[float] = None
    r"""Longitude of the location"""

    place: Optional[LocationDataPointGpsLocationPlace] = None
    r"""Address of the location"""
