# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    id: str
    """A jobId or uuid in STRING format.

    JobId must be prefixed with `jobId:`(Examples:
    `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`, `"jobId:98765"`).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    customer_name: Annotated[str, PropertyInfo(alias="customerName")]
    """Customer name to filter by"""

    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """An end time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    fleet_device_ids: Annotated[Iterable[int], PropertyInfo(alias="fleetDeviceIds")]
    """FleetDeviceId in INTEGER format. (Example: `123456`)."""

    industrial_asset_ids: Annotated[List[str], PropertyInfo(alias="industrialAssetIds")]
    """IndustrialAssetId in STRING format.

    (Example: `"8d218e6c-7a16-4f9f-90f7-cc1d93b9e596"`).
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    status: Literal["active", "scheduled", "completed"]
    """A job status in STRING format.

    Job statuses can be one of three (ignores case):
    `"active", "scheduled", "completed"` Valid values: `active`, `scheduled`,
    `completed`
    """
