# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Humidity", "Sensor"]


class Sensor(BaseModel):
    id: Optional[int] = None
    """ID of the sensor."""

    humidity: Optional[int] = None
    """Currently reported relative humidity in percent, from 0-100."""

    humidity_time: Optional[str] = FieldInfo(alias="humidityTime", default=None)
    """The timestamp of reported relative humidity, specified in RFC 3339 time."""

    name: Optional[str] = None
    """Name of the sensor."""

    trailer_id: Optional[int] = FieldInfo(alias="trailerId", default=None)
    """ID of the trailer associated with the sensor for the data point.

    If no trailer is connected, this parameter will not be reported.
    """

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """ID of the vehicle associated with the sensor for the data point.

    If no vehicle is connected, this parameter will not be reported.
    """


class Humidity(BaseModel):
    group_id: Optional[int] = FieldInfo(alias="groupId", default=None)
    """Deprecated."""

    sensors: Optional[List[Sensor]] = None
