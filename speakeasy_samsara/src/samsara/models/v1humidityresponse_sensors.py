"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1HumidityResponseSensorsTypedDict(TypedDict):
    humidity: NotRequired[int]
    r"""Currently reported relative humidity in percent, from 0-100."""
    humidity_time: NotRequired[str]
    r"""The timestamp of reported relative humidity, specified in RFC 3339 time."""
    id: NotRequired[int]
    r"""ID of the sensor."""
    name: NotRequired[str]
    r"""Name of the sensor."""
    trailer_id: NotRequired[int]
    r"""ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported."""
    vehicle_id: NotRequired[int]
    r"""ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported."""


class V1HumidityResponseSensors(BaseModel):
    humidity: Optional[int] = None
    r"""Currently reported relative humidity in percent, from 0-100."""

    humidity_time: Annotated[Optional[str], pydantic.Field(alias="humidityTime")] = None
    r"""The timestamp of reported relative humidity, specified in RFC 3339 time."""

    id: Optional[int] = None
    r"""ID of the sensor."""

    name: Optional[str] = None
    r"""Name of the sensor."""

    trailer_id: Annotated[Optional[int], pydantic.Field(alias="trailerId")] = None
    r"""ID of the trailer associated with the sensor for the data point. If no trailer is connected, this parameter will not be reported."""

    vehicle_id: Annotated[Optional[int], pydantic.Field(alias="vehicleId")] = None
    r"""ID of the vehicle associated with the sensor for the data point. If no vehicle is connected, this parameter will not be reported."""
