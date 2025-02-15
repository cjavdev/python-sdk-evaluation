"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .locationdatapoint_gpslocation import (
    LocationDataPointGpsLocation,
    LocationDataPointGpsLocationTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LocationDataPointTypedDict(TypedDict):
    r"""A single location data point of a data input."""

    gps_location: NotRequired[LocationDataPointGpsLocationTypedDict]
    r"""GPS location information of the data input's datapoint."""
    time: NotRequired[str]
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class LocationDataPoint(BaseModel):
    r"""A single location data point of a data input."""

    gps_location: Annotated[
        Optional[LocationDataPointGpsLocation], pydantic.Field(alias="gpsLocation")
    ] = None
    r"""GPS location information of the data input's datapoint."""

    time: Optional[str] = None
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
