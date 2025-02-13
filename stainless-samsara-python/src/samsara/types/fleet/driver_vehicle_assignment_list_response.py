# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DriverVehicleAssignmentListResponse", "Data", "DataDriver", "DataVehicle", "DataMetadata", "Pagination"]


class DataDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the vehicle"""


class DataMetadata(BaseModel):
    source_name: Optional[str] = FieldInfo(alias="sourceName", default=None)
    """Assigned source name from an external source."""


class Data(BaseModel):
    driver: DataDriver
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    is_passenger: bool = FieldInfo(alias="isPassenger")
    """Boolean indicating whether the driver is a passenger."""

    start_time: str = FieldInfo(alias="startTime")
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    vehicle: DataVehicle
    """A minified vehicle object.

    This object is only returned if the route is assigned to the vehicle.
    """

    assigned_at_time: Optional[str] = FieldInfo(alias="assignedAtTime", default=None)
    """An assigned at time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    assignment_type: Optional[
        Literal[
            "invalid",
            "unknown",
            "HOS",
            "idCard",
            "static",
            "faceId",
            "tachograph",
            "safetyManual",
            "RFID",
            "trailer",
            "external",
            "qrCode",
        ]
    ] = FieldInfo(alias="assignmentType", default=None)
    """Name of the assigning source for the driver assignment record.

    Valid values: `invalid`, `unknown`, `HOS`, `idCard`, `static`, `faceId`,
    `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`
    """

    end_time: Optional[str] = FieldInfo(alias="endTime", default=None)
    """An end time in RFC 3339 format.

    Omitted if not applicable. Millisecond precision and timezones are supported.
    (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    metadata: Optional[DataMetadata] = None
    """Metadata object for external assignment source data."""


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


class DriverVehicleAssignmentListResponse(BaseModel):
    data: List[Data]
    """List of driver assignment objects and their respective vehcile and driver info."""

    pagination: Pagination
    """Pagination parameters."""
