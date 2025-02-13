# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ClockListResponse",
    "Data",
    "DataClocks",
    "DataClocksBreak",
    "DataClocksCycle",
    "DataClocksDrive",
    "DataClocksShift",
    "DataCurrentDutyStatus",
    "DataCurrentVehicle",
    "DataDriver",
    "DataViolations",
    "Pagination",
]


class DataClocksBreak(BaseModel):
    time_until_break_duration_ms: Optional[float] = FieldInfo(alias="timeUntilBreakDurationMs", default=None)
    """Time until the driver has a required break in milliseconds."""


class DataClocksCycle(BaseModel):
    cycle_remaining_duration_ms: Optional[float] = FieldInfo(alias="cycleRemainingDurationMs", default=None)
    """
    Remaining on duty or driving time the driver has in the current cycle in
    milliseconds. For property-carrying drivers, this is the amount of time the
    driver can be on duty or driving before hitting the 60/70-hour limit in 7/8
    days.
    """

    cycle_started_at_time: Optional[str] = FieldInfo(alias="cycleStartedAtTime", default=None)
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    cycle_tomorrow_duration_ms: Optional[float] = FieldInfo(alias="cycleTomorrowDurationMs", default=None)
    """
    Remaining on duty or driving time the driver has available tomorrow in
    milliseconds. For property-carrying drivers this is calculated based on the
    60/70-hour limit in 7/8 days rule.
    """


class DataClocksDrive(BaseModel):
    drive_remaining_duration_ms: Optional[float] = FieldInfo(alias="driveRemainingDurationMs", default=None)
    """Remaining driving time the driver has in the current shift in milliseconds.

    For property-carrying drivers, this is the amount of time the driver can drive
    before hitting the 11-hour limit.
    """


class DataClocksShift(BaseModel):
    shift_remaining_duration_ms: Optional[float] = FieldInfo(alias="shiftRemainingDurationMs", default=None)
    """
    Remaining on duty or driving time the driver in the current shift in
    milliseconds. For property-carrying drivers, this is the amount of time the
    driver can be on duty or driving before hitting the 14-hour limit.
    """


class DataClocks(BaseModel):
    break_: Optional[DataClocksBreak] = FieldInfo(alias="break", default=None)
    """Remaining durations for the HOS rest break requirement."""

    cycle: Optional[DataClocksCycle] = None
    """Remaining durations and start time for the HOS driving cycle."""

    drive: Optional[DataClocksDrive] = None
    """Remaining durations for the HOS driving shift limits."""

    shift: Optional[DataClocksShift] = None
    """Remaining durations and start time for the HOS on duty shift limits."""


class DataCurrentDutyStatus(BaseModel):
    hos_status_type: Optional[
        Literal["offDuty", "sleeperBed", "driving", "onDuty", "yardMove", "personalConveyance"]
    ] = FieldInfo(alias="hosStatusType", default=None)
    """The Hours of Service status type.

    If the driver app is disconnected, an empty string will be returned. To
    reconnect the app and return updated values, drivers should have the app open
    with good cell service. Valid values: `offDuty`, `sleeperBed`, `driving`,
    `onDuty`, `yardMove`, `personalConveyance`.
    """


class DataCurrentVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataViolations(BaseModel):
    cycle_violation_duration_ms: Optional[float] = FieldInfo(alias="cycleViolationDurationMs", default=None)
    """
    Time since the driver has surpassed the driving cycle duration limit in
    milliseconds. For property-carrying drivers, this is the amount of time the
    driver has been on duty or driving past the 60/70-hour limit in 7/8 days.
    """

    shift_driving_violation_duration_ms: Optional[float] = FieldInfo(
        alias="shiftDrivingViolationDurationMs", default=None
    )
    """
    Time since the driver has surpassed the driving shift duration limit in
    milliseconds. For property-carrying drivers, this is the amount of time the
    driver has been driving past the 11-hour limit.
    """


class Data(BaseModel):
    clocks: Optional[DataClocks] = None
    """Remaining durations and start times (where applicable) for various HOS rules.

    See [this page](https://www.samsara.com/fleet/eld-compliance/hours-of-service)
    for more information on HOS rules.
    """

    current_duty_status: Optional[DataCurrentDutyStatus] = FieldInfo(alias="currentDutyStatus", default=None)
    """The current HOS status type and time the driver started being in this status."""

    current_vehicle: Optional[DataCurrentVehicle] = FieldInfo(alias="currentVehicle", default=None)
    """A minified vehicle object."""

    driver: Optional[DataDriver] = None
    """A minified driver object."""

    violations: Optional[DataViolations] = None
    """Durations the driver has been in violation of HOS rules.

    See [this page](https://www.samsara.com/fleet/eld-compliance/hours-of-service)
    for more information on HOS rules.
    """


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


class ClockListResponse(BaseModel):
    data: List[Data]
    """List of HOS clocks for the specified drivers."""

    pagination: Pagination
    """Pagination parameters."""
