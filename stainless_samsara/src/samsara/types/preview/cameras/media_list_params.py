# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["MediaListParams"]


class MediaListParams(TypedDict, total=False):
    available_after_time: Required[Annotated[str, PropertyInfo(alias="availableAfterTime")]]
    """
    A timestamp in RFC 3339 format that can act as a cursor to track which media has
    previously been retrieved; only media whose availableAtTime comes after this
    parameter will be returned. Examples: 2019-06-13T19:08:25Z,
    2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00
    """

    end_time: Required[Annotated[str, PropertyInfo(alias="endTime")]]
    """An end time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    inputs: Required[List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]]]
    """A list of desired camera inputs for which to return captured media.

    If empty, media for all available inputs will be returned.
    """

    media_types: Required[Annotated[List[Literal["image"]], PropertyInfo(alias="mediaTypes")]]
    """A list of desired media types for which to return captured media.

    If empty, media for all available media types will be returned.
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    trigger_reasons: Required[
        Annotated[
            List[Literal["api", "panicButton", "periodicStill", "tripEndStill", "tripStartStill", "videoRetrieval"]],
            PropertyInfo(alias="triggerReasons"),
        ]
    ]
    """A list of desired trigger reasons for which to return captured media.

    If empty, media for all available trigger reasons will be returned.
    """

    vehicle_ids: Required[Annotated[str, PropertyInfo(alias="vehicleIds")]]
    """
    A filter on the data based on this comma-separated list of vehicle IDs and
    externalIds. Example: `vehicleIds=1234,5678,samsara.vin:1HGBH41JXMN109186`
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """
