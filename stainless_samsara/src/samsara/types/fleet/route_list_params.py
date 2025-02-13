# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 512 objects.
    """
