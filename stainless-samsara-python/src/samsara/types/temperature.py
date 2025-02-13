# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Temperature", "Sensor"]


class Sensor(BaseModel):
    id: Optional[int] = None
    """ID of the sensor."""

    ambient_temperature: Optional[int] = FieldInfo(alias="ambientTemperature", default=None)
    """Currently reported ambient temperature in millidegrees celsius."""

    ambient_temperature_time: Optional[str] = FieldInfo(alias="ambientTemperatureTime", default=None)
    """The timestamp of reported ambient temperature, specified in RFC 3339 time."""

    name: Optional[str] = None
    """Name of the sensor."""

    probe_temperature: Optional[int] = FieldInfo(alias="probeTemperature", default=None)
    """Currently reported probe temperature in millidegrees celsius.

    If no probe is connected, this parameter will not be reported.
    """

    probe_temperature_time: Optional[str] = FieldInfo(alias="probeTemperatureTime", default=None)
    """The timestamp of reported probe temperature, specified in RFC 3339 time."""

    trailer_id: Optional[int] = FieldInfo(alias="trailerId", default=None)
    """ID of the trailer associated with the sensor for the data point.

    If no trailer is connected, this parameter will not be reported.
    """

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """ID of the vehicle associated with the sensor for the data point.

    If no vehicle is connected, this parameter will not be reported.
    """


class Temperature(BaseModel):
    group_id: Optional[int] = FieldInfo(alias="groupId", default=None)
    """Deprecated."""

    sensors: Optional[List[Sensor]] = None
