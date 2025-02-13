# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DriverEfficiencyResponse",
    "Data",
    "DataDriverSummary",
    "DataDriverSummaryDriver",
    "DataDriverSummaryVehicleSummary",
    "DataDriverSummaryVehicleSummaryVehicle",
    "Pagination",
]


class DataDriverSummaryDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the driver."""

    username: Optional[str] = None
    """Username of the driver."""


class DataDriverSummaryVehicleSummaryVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class DataDriverSummaryVehicleSummary(BaseModel):
    anticipation_brake_event_count: Optional[float] = FieldInfo(alias="anticipationBrakeEventCount", default=None)
    """Quick braking events (less than one second after accelerating)."""

    coasting_duration_ms: Optional[float] = FieldInfo(alias="coastingDurationMs", default=None)
    """Time spent without engaging the accelerator or brake in milliseconds."""

    cruise_control_duration_ms: Optional[float] = FieldInfo(alias="cruiseControlDurationMs", default=None)
    """Time spent in cruise control in milliseconds."""

    distance_driven_meters: Optional[float] = FieldInfo(alias="distanceDrivenMeters", default=None)
    """Distance driven in meters."""

    drive_time_duration_ms: Optional[float] = FieldInfo(alias="driveTimeDurationMs", default=None)
    """Time driven in milliseconds."""

    fuel_consumed_ml: Optional[float] = FieldInfo(alias="fuelConsumedMl", default=None)
    """Fuel consumption in milliliters."""

    green_band_driving_duration_ms: Optional[float] = FieldInfo(alias="greenBandDrivingDurationMs", default=None)
    """Time in efficient RPM (800 to 17000) in milliseconds."""

    high_torque_ms: Optional[float] = FieldInfo(alias="highTorqueMs", default=None)
    """Time the vehicle engine torque is greater than 90% in milliseconds."""

    idle_time_duration_ms: Optional[float] = FieldInfo(alias="idleTimeDurationMs", default=None)
    """Time spent idling in milliseconds."""

    over_speed_ms: Optional[float] = FieldInfo(alias="overSpeedMs", default=None)
    """Driving time spent over the efficient speed threshold in milliseconds."""

    power_take_off_duration_ms: Optional[float] = FieldInfo(alias="powerTakeOffDurationMs", default=None)
    """Time spent with power take off enabled while idling in milliseconds."""

    total_brake_event_count: Optional[float] = FieldInfo(alias="totalBrakeEventCount", default=None)
    """Total number of brake events."""

    vehicle: Optional[DataDriverSummaryVehicleSummaryVehicle] = None
    """A minified vehicle object."""


class DataDriverSummary(BaseModel):
    anticipation_brake_event_count: Optional[float] = FieldInfo(alias="anticipationBrakeEventCount", default=None)
    """Quick braking events (less than one second after accelerating)."""

    coasting_duration_ms: Optional[float] = FieldInfo(alias="coastingDurationMs", default=None)
    """Time spent without engaging the accelerator or brake in milliseconds."""

    cruise_control_duration_ms: Optional[float] = FieldInfo(alias="cruiseControlDurationMs", default=None)
    """Time spent in cruise control in milliseconds."""

    driver: Optional[DataDriverSummaryDriver] = None
    """A minified driver object."""

    green_band_driving_duration_ms: Optional[float] = FieldInfo(alias="greenBandDrivingDurationMs", default=None)
    """Time in efficient RPM (800 to 17000) in milliseconds."""

    high_torque_ms: Optional[float] = FieldInfo(alias="highTorqueMs", default=None)
    """Time the vehicle engine torque is greater than 90% in milliseconds."""

    over_speed_ms: Optional[float] = FieldInfo(alias="overSpeedMs", default=None)
    """Driving time spent over the efficient speed threshold in milliseconds."""

    total_brake_event_count: Optional[float] = FieldInfo(alias="totalBrakeEventCount", default=None)
    """Total number of brake events."""

    total_distance_driven_meters: Optional[float] = FieldInfo(alias="totalDistanceDrivenMeters", default=None)
    """Distance driven in meters."""

    total_drive_time_duration_ms: Optional[float] = FieldInfo(alias="totalDriveTimeDurationMs", default=None)
    """Time driven in milliseconds."""

    total_fuel_consumed_ml: Optional[float] = FieldInfo(alias="totalFuelConsumedMl", default=None)
    """Fuel consumption in milliliters."""

    total_idle_time_duration_ms: Optional[float] = FieldInfo(alias="totalIdleTimeDurationMs", default=None)
    """Time spent idling in milliseconds."""

    total_power_take_off_duration_ms: Optional[float] = FieldInfo(alias="totalPowerTakeOffDurationMs", default=None)
    """Time spent with power take off enabled while idling in milliseconds."""

    vehicle_summaries: Optional[List[DataDriverSummaryVehicleSummary]] = FieldInfo(
        alias="vehicleSummaries", default=None
    )
    """
    Summaries of vehicle efficiency for each vehicle the driver was driving during
    the given time period.
    """


class Data(BaseModel):
    driver_summaries: Optional[List[DataDriverSummary]] = FieldInfo(alias="driverSummaries", default=None)
    """A list of driver and associated vehicle efficiency data."""

    summary_end_time: Optional[datetime] = FieldInfo(alias="summaryEndTime", default=None)
    """End time of the window for which this efficiency report was computed.

    Will be a UTC timestamp in RFC 3339 format. For example: `2020-03-16T16:00:00Z`
    """

    summary_start_time: Optional[datetime] = FieldInfo(alias="summaryStartTime", default=None)
    """Start time of the window for which this efficiency report was computed.

    Will be a UTC timestamp in RFC 3339 format. For example: `2020-03-15T16:00:00Z`
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


class DriverEfficiencyResponse(BaseModel):
    data: Optional[Data] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
