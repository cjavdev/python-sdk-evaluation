# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Cargo", "Sensor"]


class Sensor(BaseModel):
    id: Optional[int] = None
    """ID of the sensor."""

    cargo_empty: Optional[bool] = FieldInfo(alias="cargoEmpty", default=None)
    """Flag indicating whether the current cargo is empty or loaded."""

    cargo_status_time: Optional[str] = FieldInfo(alias="cargoStatusTime", default=None)
    """The timestamp of reported cargo status, specified in RFC 3339 time."""

    name: Optional[str] = None
    """Name of the sensor."""

    red_eye_distance: Optional[int] = FieldInfo(alias="redEyeDistance", default=None)
    """The distance between red eye detector and the closest object in cm."""

    trailer_id: Optional[int] = FieldInfo(alias="trailerId", default=None)
    """ID of the trailer associated with the sensor for the data point.

    If no trailer is connected, this parameter will not be reported.
    """

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """ID of the vehicle associated with the sensor for the data point.

    If no vehicle is connected, this parameter will not be reported.
    """


class Cargo(BaseModel):
    group_id: Optional[int] = FieldInfo(alias="groupId", default=None)
    """Deprecated."""

    sensors: Optional[List[Sensor]] = None
