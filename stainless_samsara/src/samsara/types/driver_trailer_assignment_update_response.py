# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DriverTrailerAssignmentUpdateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Samsara ID for the assignment."""

    driver_id: str = FieldInfo(alias="driverId")
    """Samsara ID for the driver that this assignment is for."""

    end_time: str = FieldInfo(alias="endTime")
    """Time when the driver trailer assignment ends, in RFC 3339 format"""

    start_time: str = FieldInfo(alias="startTime")
    """Time when the driver trailer assignment starts, in RFC 3339 format"""

    trailer_id: str = FieldInfo(alias="trailerId")
    """Samsara ID of the trailer"""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Time when the driver trailer assignment was created, in RFC 3339 format"""

    updated_at_time: Optional[str] = FieldInfo(alias="updatedAtTime", default=None)
    """Time when the driver trailer assignment was last updated, in RFC 3339 format"""


class DriverTrailerAssignmentUpdateResponse(BaseModel):
    data: Data
    """Response after successfully updating a Driver Trailer Assignment"""
