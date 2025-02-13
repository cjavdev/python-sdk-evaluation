# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionStreamParams"]


class SessionStreamParams(TypedDict, total=False):
    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """Required RFC 3339 timestamp that indicates when to begin receiving data.

    Value is compared against `updatedAtTime`
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    coach_ids: Annotated[List[str], PropertyInfo(alias="coachIds")]
    """Optional string of comma separated user IDs.

    If coach ID is present, sessions for the specified coach(s) will be returned for
    either assignedCoach or completedCoach. If both driverId(s) and coachId(s) are
    present, sessions with specified driver(s) and coach(es) will be returned.
    """

    driver_ids: Annotated[List[str], PropertyInfo(alias="driverIds")]
    """Optional string of comma separated driver IDs.

    If driver ID is present, sessions for the specified driver(s) will be returned.
    """

    end_time: Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]
    """Optional RFC 3339 timestamp.

    If not provided then the endpoint behaves as an unending feed of changes. If
    endTime is set the same as startTime, the most recent data point before that
    time will be returned per asset. Value is compared against `updatedAtTime`
    """

    include_coachable_events: Annotated[bool, PropertyInfo(alias="includeCoachableEvents")]
    """
    Optional boolean to control whether behaviors will include coachableEvents in
    the response. Defaults to false.
    """

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """

    session_statuses: Annotated[List[str], PropertyInfo(alias="sessionStatuses")]
    """Optional string of comma separated statuses.

    Valid values: “upcoming”, “completed”, “deleted”.
    """
