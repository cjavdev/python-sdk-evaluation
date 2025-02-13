# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1TrailerAssignmentsResponse", "TrailerAssignment"]


class TrailerAssignment(BaseModel):
    driver_id: Optional[int] = FieldInfo(alias="driverId", default=None)
    """The ID of the driver associated with this trailer."""

    end_ms: Optional[int] = FieldInfo(alias="endMs", default=None)
    """The time at which the driver ended the assignment.

    If the assignment is current, this value will be omitted.
    """

    start_ms: Optional[int] = FieldInfo(alias="startMs", default=None)
    """The time at which the driver started the assignment"""


class V1TrailerAssignmentsResponse(BaseModel):
    id: int
    """ID of the trailer"""

    name: str
    """Assignment trailer name (given when creating trailer via the trailer portal)"""

    trailer_assignments: Optional[List[TrailerAssignment]] = FieldInfo(alias="trailerAssignments", default=None)
