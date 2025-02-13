# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DriverEfficiencyParams"]


class DriverEfficiencyParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    driver_activation_status: Annotated[Literal["active", "deactivated"], PropertyInfo(alias="driverActivationStatus")]
    """
    If value is `deactivated`, only drivers that are deactivated will appear in the
    response. This parameter will default to `active` if not provided (fetching only
    active drivers).
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """A filter on the data based on this comma-separated list of driver IDs.

    Cannot be used with tag filtering or driver status. Example:
    `driverIds=1234,5678`
    """

    driver_parent_tag_ids: Annotated[List[str], PropertyInfo(alias="driverParentTagIds")]
    """
    Filters like `driverTagIds` but includes descendants of all the given parent
    tags. Should not be provided in addition to `driverIds`. Example:
    `driverParentTagIds=1234,5678`
    """

    driver_tag_ids: Annotated[List[str], PropertyInfo(alias="driverTagIds")]
    """Filters summary to drivers based on this comma-separated list of tag IDs.

    Data from all the drivers' respective vehicles will be included in the summary,
    regardless of which tag the vehicle is associated with. Should not be provided
    in addition to `driverIds`. Example: driverTagIds=1234,5678
    """

    end_time: Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]
    """An end time in RFC 3339 format.

    The results will be truncated to the hour mark for the provided time. For
    example, if `endTime` is 2020-03-17T12:06:19Z then the results will include data
    up until 2020-03-17T12:00:00Z. The provided end time cannot be in the future.
    End time can be at most 31 days after the start time. Default: The current time
    truncated to the hour mark.

    Note that the most recent 72 hours of data may still be processing and is
    subject to change and latency, so it is not recommended to request data for the
    most recent 72 hours
    """

    start_time: Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]
    """A start time in RFC 3339 format.

    The results will be truncated to the hour mark for the provided time. For
    example, if `startTime` is 2020-03-17T12:06:19Z then the results will include
    data starting from 2020-03-17T12:00:00Z. The provided start time cannot be in
    the future. Start time can be at most 31 days before the end time. If the start
    time is within the last hour, the results will be empty. Default: 24 hours prior
    to endTime.

    Note that the most recent 72 hours of data may still be processing and is
    subject to change and latency, so it is not recommended to request data for the
    most recent 72 hours.
    """
