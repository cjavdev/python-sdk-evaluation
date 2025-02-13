# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "LogListResponse",
    "Data",
    "DataDriver",
    "DataHosLog",
    "DataHosLogCodriver",
    "DataHosLogLogRecordedLocation",
    "DataHosLogVehicle",
    "Pagination",
]


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataHosLogCodriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataHosLogLogRecordedLocation(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""


class DataHosLogVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataHosLog(BaseModel):
    log_start_time: str = FieldInfo(alias="logStartTime")
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    codrivers: Optional[List[DataHosLogCodriver]] = None
    """The codriver information."""

    hos_status_type: Optional[
        Literal["offDuty", "sleeperBed", "driving", "onDuty", "yardMove", "personalConveyance"]
    ] = FieldInfo(alias="hosStatusType", default=None)
    """The Hours of Service status type.

    Valid values: `offDuty`, `sleeperBed`, `driving`, `onDuty`, `yardMove`,
    `personalConveyance`.
    """

    log_end_time: Optional[str] = FieldInfo(alias="logEndTime", default=None)
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    log_recorded_location: Optional[DataHosLogLogRecordedLocation] = FieldInfo(
        alias="logRecordedLocation", default=None
    )
    """Location associated with the duty status change"""

    remark: Optional[str] = None
    """Remark associated with the log entry."""

    vehicle: Optional[DataHosLogVehicle] = None
    """A minified vehicle object."""


class Data(BaseModel):
    driver: Optional[DataDriver] = None
    """A minified driver object."""

    hos_logs: Optional[List[DataHosLog]] = FieldInfo(alias="hosLogs", default=None)
    """List of HOS log entries."""


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


class LogListResponse(BaseModel):
    data: List[Data]
    """List of HOS logs for the specified drivers."""

    pagination: Pagination
    """Pagination parameters."""
