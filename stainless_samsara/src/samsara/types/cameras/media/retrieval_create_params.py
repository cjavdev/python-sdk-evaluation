# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RetrievalCreateParams"]


class RetrievalCreateParams(TypedDict, total=False):
    inputs: Required[List[Literal["dashcamRoadFacing", "dashcamDriverFacing", "analog"]]]
    """A list of desired camera inputs for which to capture media.

    Only media with valid inputs (e.g. device has that input stream and device was
    recording at the time) will be uploaded. An empty list is invalid.
    """

    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    vehicle_id: Required[Annotated[str, PropertyInfo(alias="vehicleId")]]
    """Vehicle ID for which to initiate media capture. Examples: 1234"""

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    If same as startTime or not specified, an image will be captured at startTime.
    If specified, must be equal to or after startTime and no more than 60 seconds
    after startTime. (Examples: 2019-06-13T19:08:55Z, 2019-06-13T19:08:55.455Z, OR
    2015-09-15T14:00:42-04:00).
    """
