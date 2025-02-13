# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VehicleListParams"]


class VehicleListParams(TypedDict, total=False):
    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """An end time in RFC 3339 format.

    Must be in multiple of hours and no later than 3 hours before the current time.
    Timezones are supported. Note that the most recent 72 hours of data may still be
    processing and is subject to change and latency, so it is not recommended to
    request data for the most recent 72 hours. (Examples: 2019-06-13T19:00:00Z,
    2015-09-15T14:00:00-04:00).
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Must be in multiple of hours and at least 1 day before endTime. Timezones are
    supported. Note that the most recent 72 hours of data may still be processing
    and is subject to change and latency, so it is not recommended to request data
    for the most recent 72 hours. (Examples: 2019-06-11T19:00:00Z,
    2015-09-12T14:00:00-04:00).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    data_formats: Annotated[List[str], PropertyInfo(alias="dataFormats")]
    """A comma-separated list of data formats you want to fetch.

    Valid values: `score`, `raw` and `percentage`. The default data format is
    `score`. Example: `dataFormats=raw,score`
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

    vehicle_ids: Annotated[str, PropertyInfo(alias="vehicleIds")]
    """
    A filter on the data based on this comma-separated list of vehicle IDs and
    externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    """
