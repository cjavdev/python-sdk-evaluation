# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DriverTrailerAssignmentCreateResponse", "Data"]


class Data(BaseModel):
    id: str
    """Samsara ID for the assignment."""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """Time when the driver trailer assignment was created, in RFC 3339 format"""

    driver_id: str = FieldInfo(alias="driverId")
    """Samsara ID for the driver that this assignment is for."""

    start_time: str = FieldInfo(alias="startTime")
    """Time when the driver trailer assignment starts, in RFC 3339 format"""

    trailer_id: str = FieldInfo(alias="trailerId")
    """Samsara ID of the trailer"""

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """Time when the driver trailer assignment was last updated, in RFC 3339 format"""


class DriverTrailerAssignmentCreateResponse(BaseModel):
    data: Data
    """Response after successfully submitting a Driver Trailer Assignment"""
