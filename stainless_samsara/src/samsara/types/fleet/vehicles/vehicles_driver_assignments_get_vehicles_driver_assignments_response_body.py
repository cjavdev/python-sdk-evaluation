# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody",
    "Data",
    "DataDriverAssignment",
    "DataDriverAssignmentDriver",
    "Pagination",
]


class DataDriverAssignmentDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataDriverAssignment(BaseModel):
    assignment_type: Optional[Literal["driverApp"]] = FieldInfo(alias="assignmentType", default=None)
    """
    Assignment type of the driver-vehicle assignment, indicating the provenance of
    the assignment. The only type of assignment supported right now is `driverApp`
    assignments. This list could change, so it is recommended that clients
    gracefully handle any types not enumerated in this list. Valid values:
    `driverApp`
    """

    driver: Optional[DataDriverAssignmentDriver] = None
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    end_time: Optional[str] = FieldInfo(alias="endTime", default=None)
    """An end time in RFC 3339 format.

    Omitted if not applicable. Millisecond precision and timezones are supported.
    (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    is_passenger: Optional[bool] = FieldInfo(alias="isPassenger", default=None)
    """Boolean indicating whether the driver is a passenger."""

    start_time: Optional[str] = FieldInfo(alias="startTime", default=None)
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """


class Data(BaseModel):
    id: str
    """ID of the vehicle."""

    driver_assignments: List[DataDriverAssignment] = FieldInfo(alias="driverAssignments")
    """List of driver assignment objects."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle."""


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


class VehiclesDriverAssignmentsGetVehiclesDriverAssignmentsResponseBody(BaseModel):
    data: List[Data]
    """List of vehicles and their driver assignments."""

    pagination: Pagination
    """Pagination parameters."""
