# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JobCreateParams", "Job", "JobAddress"]


class JobCreateParams(TypedDict, total=False):
    job: Required[Job]
    """Job object to be created"""


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
    id: Required[str]
    """Job Id"""

    end_date: Required[Annotated[str, PropertyInfo(alias="endDate")]]
    """End date of job in RFC 3339 format.

    Must be greater than or equal to the start date
    """

    name: Required[str]
    """Job name"""

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]
    """Start date of job in RFC 3339 format."""

    address: JobAddress
    """A location object for the job"""

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """Customer name for job"""

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
