# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DriverCoachAssignmentListResponse", "Data", "DataDriver", "Pagination"]


class DataDriver(BaseModel):
    driver_id: str = FieldInfo(alias="driverId")
    """Samsara ID of the driver."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class Data(BaseModel):
    coach_id: str = FieldInfo(alias="coachId")
    """Coach ID associated with coach assignment. Always returned."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time coach assignment was created in UTC. Always returned."""

    driver: DataDriver
    """A driver object with an id and map of external ids."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time coaching assignment was updated in UTC. Always returned."""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class DriverCoachAssignmentListResponse(BaseModel):
    data: List[Data]
    """List of driver coach assignment objects"""

    pagination: Pagination
    """Pagination parameters."""
