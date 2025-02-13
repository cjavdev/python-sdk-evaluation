# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Door", "Sensor"]


class Sensor(BaseModel):
    id: Optional[int] = None
    """ID of the sensor."""

    door_closed: Optional[bool] = FieldInfo(alias="doorClosed", default=None)
    """Flag indicating whether the current door is closed or open."""

    door_status_time: Optional[str] = FieldInfo(alias="doorStatusTime", default=None)
    """The timestamp of reported door status, specified in RFC 3339 time."""

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


class Door(BaseModel):
    group_id: Optional[int] = FieldInfo(alias="groupId", default=None)
    """Deprecated."""

    sensors: Optional[List[Sensor]] = None
