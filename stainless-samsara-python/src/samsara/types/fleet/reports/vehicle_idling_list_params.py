# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VehicleIdlingListParams"]


class VehicleIdlingListParams(TypedDict, total=False):
    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. Note that the most recent 72 hours of data may still be processing
    and is subject to change and latency, so it is not recommended to request data
    for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. Note that the most recent 72 hours of data may still be processing
    and is subject to change and latency, so it is not recommended to request data
    for the most recent 72 hours. (Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    is_pto_active: Annotated[bool, PropertyInfo(alias="isPtoActive")]
    """A filter on the data based on power take-off being active or inactive."""

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """

    min_idling_duration_minutes: Annotated[int, PropertyInfo(alias="minIdlingDurationMinutes")]
    """A filter on the data based on a minimum idling duration."""

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
