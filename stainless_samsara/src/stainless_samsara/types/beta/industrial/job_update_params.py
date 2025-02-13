# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JobUpdateParams", "Job", "JobAddress"]


class JobUpdateParams(TypedDict, total=False):
    id: Required[str]
    """A jobId or uuid in STRING format.

    JobId must be prefixed with `jobId:`(Examples:
    `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    """

    job: Required[Job]
    """Job object with fields to update.

    If a field is not provided, it will not be updated
    """

    keep_history: Annotated[bool, PropertyInfo(alias="keepHistory")]
    """
    Defaults to true if user does not want to overwrite entire history for an active
    job (irrelevant for scheduled/completed jobs)
    """


class JobAddress(TypedDict, total=False):
    address: Required[str]
    """Address of a location"""

    latitude: Required[float]
    """Latitude of a location"""

    longitude: Required[float]
    """Longitude of a location"""

    name: Required[str]
    """Name of the location"""


class Job(TypedDict, total=False):
    id: str
    """Job Id"""

    address: JobAddress
    """A location object for the job"""

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """Customer name for job"""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End date of job in RFC 3339 format.

    Must be greater than or equal to the start date
    """

    fleet_device_ids: Annotated[Iterable[int], PropertyInfo(alias="fleetDeviceIds")]
    """
    Fleet devices to be added to this job (cannot have both industrial assets and
    fleet devices in the same job)
    """

    industrial_asset_ids: Annotated[List[str], PropertyInfo(alias="industrialAssetIds")]
    """
    IndustrialAssets to be added to this job (cannot have both industrial assets and
    fleet devices in the same job)
    """

    name: str
    """Job name"""

    notes: str
    """Notes for the upcoming job"""

    ontime_window_after_arrival_ms: Annotated[int, PropertyInfo(alias="ontimeWindowAfterArrivalMs")]
    """
    Specifies the time window (in milliseconds) after a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    ontime_window_before_arrival_ms: Annotated[int, PropertyInfo(alias="ontimeWindowBeforeArrivalMs")]
    """
    Specifies the time window (in milliseconds) before a stop's scheduled arrival
    time during which the stop is considered 'on-time'.
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start date of job in RFC 3339 format."""
