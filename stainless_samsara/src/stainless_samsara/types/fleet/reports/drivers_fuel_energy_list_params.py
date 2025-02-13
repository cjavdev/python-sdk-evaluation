# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DriversFuelEnergyListParams"]


class DriversFuelEnergyListParams(TypedDict, total=False):
    end_date: Required[Annotated[str, PropertyInfo(alias="endDate")]]
    """An end date in RFC 3339 format.

    This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds,
    etc.) besides the date and timezone. If no time zone is passed in, then the UTC
    time zone will be used. This parameter is inclusive, so data on the date
    specified will be considered. Note that the most recent 72 hours of data may
    still be processing and is subject to change and latency, so it is not
    recommended to request data for the most recent 72 hours. For example,
    2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    """

    start_date: Required[Annotated[str, PropertyInfo(alias="startDate")]]
    """A start date in RFC 3339 format.

    This parameter ignores everything (i.e. hour, minutes, seconds, nanoseconds,
    etc.) besides the date and timezone. If no time zone is passed in, then the UTC
    time zone will be used. This parameter is inclusive, so data on the date
    specified will be considered. Note that the most recent 72 hours of data may
    still be processing and is subject to change and latency, so it is not
    recommended to request data for the most recent 72 hours. For example,
    2022-07-13T14:20:50.52-07:00 is a time in Pacific Daylight Time.
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """
    A filter on the data based on this comma-separated list of driver IDs and
    externalIds. Example: `driverIds=1234,5678,payroll:4841`
    """

    parent_tag_ids: Annotated[str, PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    tag_ids: Annotated[str, PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """
