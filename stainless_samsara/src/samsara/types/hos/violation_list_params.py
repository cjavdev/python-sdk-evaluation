# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ViolationListParams"]


class ViolationListParams(TypedDict, total=False):
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

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    parent_tag_ids: Annotated[str, PropertyInfo(alias="parentTagIds")]
    """
    A filter on the data based on this comma-separated list of parent tag IDs, for
    use by orgs with tag hierarchies. Specifying a parent tag will implicitly
    include all descendent tags of the parent tag. Example: `parentTagIds=345,678`
    """

    start_time: Annotated[str, PropertyInfo(alias="startTime")]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    tag_ids: Annotated[str, PropertyInfo(alias="tagIds")]
    """A filter on the data based on this comma-separated list of tag IDs.

    Example: `tagIds=1234,5678`
    """

    types: List[str]
    """A filter on violations data based on the violation type enum.

    Supported types:
    `NONE, californiaMealbreakMissed, cycleHoursOn, cycleOffHoursAfterOnDutyHours, dailyDrivingHours, dailyOffDutyDeferralAddToDay2Consecutive, dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit, dailyOffDutyDeferralTwoDayOffDuty, dailyOffDutyNonResetHours, dailyOffDutyTotalHours, dailyOnDutyHours, mandatory24HoursOffDuty, restbreakMissed, shiftDrivingHours, shiftHours, shiftOnDutyHours, unsubmittedLogs`
    """
