# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["Job", "Data", "DataAddress", "DataFleetDevice", "DataIndustrialAsset", "Pagination"]


class DataAddress(BaseModel):
    address: str
    """Address of a location"""

    latitude: float
    """Latitude of a location"""

    longitude: float
    """Longitude of a location"""

    name: str
    """Name of a location"""


class DataFleetDevice(BaseModel):
    id: int
    """Id of the device"""

    name: str
    """Name of the device"""


class DataIndustrialAsset(BaseModel):
    id: str
    """Id of the device"""

    name: str
    """Name of the industrial asset"""


class Data(BaseModel):
    id: str
    """Job id"""

    address: DataAddress
    """jobLocation object"""

    created_at: str = FieldInfo(alias="createdAt")
    """When the job was created"""

    customer_name: str = FieldInfo(alias="customerName")
    """Customer name for job"""

    end_date: str = FieldInfo(alias="endDate")
    """End date of job in RFC 3339 format"""

    modified_at: str = FieldInfo(alias="modifiedAt")
    """When the job was last modified"""

    name: str
    """Job name"""

    notes: str
    """Notes for the upcoming job"""

    start_date: str = FieldInfo(alias="startDate")
    """Start date of job in RFC 3339 format"""

    status: Literal["active", "scheduled", "completed"]
    """The current job status Valid values: `active`, `scheduled`, `completed`"""

    uuid: str
    """Samsara uuid"""

    fleet_devices: Optional[List[DataFleetDevice]] = FieldInfo(alias="fleetDevices", default=None)
    """
    fleet devices in this job (cannot have both industrial assets and fleet devices
    in the same job)
    """

    industrial_assets: Optional[List[DataIndustrialAsset]] = FieldInfo(alias="industrialAssets", default=None)
    """
    Industrial Assets in this job (cannot have both industrial assets and fleet
    devices in the same job)
    """

    ontime_window_after_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowAfterArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Optional[int] = FieldInfo(alias="ontimeWindowBeforeArrivalMs", default=None)
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """


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


class Job(BaseModel):
    data: List[Data]
    """List of Job Objects"""

    pagination: Pagination
    """Pagination parameters."""

    id: Optional[str] = None
    """The job id of the failed request"""

    uuid: Optional[str] = None
    """The uuid of the failed request"""
