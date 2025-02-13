# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DriverCoachAssignmentUpdateResponse", "Data"]


class Data(BaseModel):
    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time coach assignment was created in UTC. Always returned."""

    driver_id: str = FieldInfo(alias="driverId")
    """Unique user ID for the driver of the driver coach assignment"""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time coaching assignment was updated in UTC. Always returned."""

    coach_id: Optional[str] = FieldInfo(alias="coachId", default=None)
    """Coach ID associated with coach assignment.

    Optional. Will be empty if no driver coach is assigned
    """


class DriverCoachAssignmentUpdateResponse(BaseModel):
    data: Data
    """Driver coach assignment object."""
