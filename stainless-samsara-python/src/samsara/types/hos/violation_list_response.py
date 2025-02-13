# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ViolationListResponse", "Data", "DataViolation", "DataViolationDay", "DataViolationDriver", "Pagination"]


class DataViolationDay(BaseModel):
    end_time: str = FieldInfo(alias="endTime")
    """The end time of the day on which the violation occurred in RFC 3339 format.

    This is determined by the driver's ELD start hour (00:00 or 12:00)
    """

    start_time: str = FieldInfo(alias="startTime")
    """The start time of the day on which the violation occurred in RFC 3339 format.

    This is determined by the driver's ELD start hour (00:00 or 12:00)
    """


class DataViolationDriver(BaseModel):
    id: str
    """ID of the driver"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    name: Optional[str] = None
    """Name of the driver"""


class DataViolation(BaseModel):
    day: DataViolationDay

    description: str
    """Description containing violation type, region, and other metadata.

    This field can assume the following formats for the following types:
    californiaMealbreakMissed, restbreakMissed: "[description] ([max on duty hours]
    hours)" cycleHoursOn, dailyDrivingHours, dailyOffDutyNonResetHours,
    dailyOffDutyTotalHours, dailyOnDutyHours, shiftDrivingHours, shiftHours,
    shiftOnDutyHours: "[description] ([region]-[max hours in duty status] hours)"
    cycleOffHoursAfterOnDutyHours: "[description] ([region]): [minimum hours
    consecutive rest] hours off duty required after [max hours before consecutive
    rest] hours on-duty time" dailyOffDutyDeferralAddToDay2Consecutive,
    dailyOffDutyDeferralNotPartMandatory, dailyOffDutyDeferralTwoDayDrivingLimit,
    dailyOffDutyDeferralTwoDayOffDuty, mandatory24HoursOffDuty: "[description]
    ([region])" unsubmittedLogs: "Missing Driver Certification"
    """

    driver: DataViolationDriver
    """A minified driver object.

    This object is only returned if the route is assigned to the driver.
    """

    duration_ms: int = FieldInfo(alias="durationMs")
    """Duration the driver was in violation in milliseconds.

    This is the time between the time the driver starts being in violation until the
    end of the time window for violations that have one (e.g. `shiftDrivingHours`)
    or until the end of the day. The duration of some violations may cover the whole
    day (e.g. `unsubmittedLogs`).
    """

    type: Literal[
        "NONE",
        "californiaMealbreakMissed",
        "cycleHoursOn",
        "cycleOffHoursAfterOnDutyHours",
        "dailyDrivingHours",
        "dailyOffDutyDeferralAddToDay2Consecutive",
        "dailyOffDutyDeferralNotPartMandatory",
        "dailyOffDutyDeferralTwoDayDrivingLimit",
        "dailyOffDutyDeferralTwoDayOffDuty",
        "dailyOffDutyNonResetHours",
        "dailyOffDutyTotalHours",
        "dailyOnDutyHours",
        "mandatory24HoursOffDuty",
        "restbreakMissed",
        "shiftDrivingHours",
        "shiftHours",
        "shiftOnDutyHours",
        "unsubmittedLogs",
    ]
    """The string value of the violation type.

    Valid values: `NONE`, `californiaMealbreakMissed`, `cycleHoursOn`,
    `cycleOffHoursAfterOnDutyHours`, `dailyDrivingHours`,
    `dailyOffDutyDeferralAddToDay2Consecutive`,
    `dailyOffDutyDeferralNotPartMandatory`,
    `dailyOffDutyDeferralTwoDayDrivingLimit`, `dailyOffDutyDeferralTwoDayOffDuty`,
    `dailyOffDutyNonResetHours`, `dailyOffDutyTotalHours`, `dailyOnDutyHours`,
    `mandatory24HoursOffDuty`, `restbreakMissed`, `shiftDrivingHours`, `shiftHours`,
    `shiftOnDutyHours`, `unsubmittedLogs`
    """

    violation_start_time: str = FieldInfo(alias="violationStartTime")
    """The start time of the violation in RFC 3339 format."""


class Data(BaseModel):
    violations: List[DataViolation]
    """List of violations and their associated drivers"""


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class ViolationListResponse(BaseModel):
    data: List[Data]
    """List of violations data"""

    pagination: Pagination
    """Pagination parameters."""
