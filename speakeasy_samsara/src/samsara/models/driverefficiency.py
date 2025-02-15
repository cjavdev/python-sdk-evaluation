"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .extendeddrivertinyresponse import (
    ExtendedDriverTinyResponse,
    ExtendedDriverTinyResponseTypedDict,
)
from .vehiclesummary import VehicleSummary, VehicleSummaryTypedDict
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverEfficiencyTypedDict(TypedDict):
    r"""Summary of a driver's efficiency."""

    anticipation_brake_event_count: NotRequired[float]
    r"""Quick braking events (less than one second after accelerating)."""
    coasting_duration_ms: NotRequired[float]
    r"""Time spent without engaging the accelerator or brake in milliseconds."""
    cruise_control_duration_ms: NotRequired[float]
    r"""Time spent in cruise control in milliseconds."""
    driver: NotRequired[ExtendedDriverTinyResponseTypedDict]
    r"""A minified driver object."""
    green_band_driving_duration_ms: NotRequired[float]
    r"""Time in efficient RPM (800 to 17000) in milliseconds."""
    high_torque_ms: NotRequired[float]
    r"""Time the vehicle engine torque is greater than 90% in milliseconds."""
    over_speed_ms: NotRequired[float]
    r"""Driving time spent over the efficient speed threshold in milliseconds."""
    total_brake_event_count: NotRequired[float]
    r"""Total number of brake events."""
    total_distance_driven_meters: NotRequired[float]
    r"""Distance driven in meters."""
    total_drive_time_duration_ms: NotRequired[float]
    r"""Time driven in milliseconds."""
    total_fuel_consumed_ml: NotRequired[float]
    r"""Fuel consumption in milliliters."""
    total_idle_time_duration_ms: NotRequired[float]
    r"""Time spent idling in milliseconds."""
    total_power_take_off_duration_ms: NotRequired[float]
    r"""Time spent with power take off enabled while idling in milliseconds."""
    vehicle_summaries: NotRequired[List[VehicleSummaryTypedDict]]
    r"""Summaries of vehicle efficiency for each vehicle the driver was driving during the given time period."""


class DriverEfficiency(BaseModel):
    r"""Summary of a driver's efficiency."""

    anticipation_brake_event_count: Annotated[
        Optional[float], pydantic.Field(alias="anticipationBrakeEventCount")
    ] = None
    r"""Quick braking events (less than one second after accelerating)."""

    coasting_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="coastingDurationMs")
    ] = None
    r"""Time spent without engaging the accelerator or brake in milliseconds."""

    cruise_control_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="cruiseControlDurationMs")
    ] = None
    r"""Time spent in cruise control in milliseconds."""

    driver: Optional[ExtendedDriverTinyResponse] = None
    r"""A minified driver object."""

    green_band_driving_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="greenBandDrivingDurationMs")
    ] = None
    r"""Time in efficient RPM (800 to 17000) in milliseconds."""

    high_torque_ms: Annotated[Optional[float], pydantic.Field(alias="highTorqueMs")] = (
        None
    )
    r"""Time the vehicle engine torque is greater than 90% in milliseconds."""

    over_speed_ms: Annotated[Optional[float], pydantic.Field(alias="overSpeedMs")] = (
        None
    )
    r"""Driving time spent over the efficient speed threshold in milliseconds."""

    total_brake_event_count: Annotated[
        Optional[float], pydantic.Field(alias="totalBrakeEventCount")
    ] = None
    r"""Total number of brake events."""

    total_distance_driven_meters: Annotated[
        Optional[float], pydantic.Field(alias="totalDistanceDrivenMeters")
    ] = None
    r"""Distance driven in meters."""

    total_drive_time_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="totalDriveTimeDurationMs")
    ] = None
    r"""Time driven in milliseconds."""

    total_fuel_consumed_ml: Annotated[
        Optional[float], pydantic.Field(alias="totalFuelConsumedMl")
    ] = None
    r"""Fuel consumption in milliliters."""

    total_idle_time_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="totalIdleTimeDurationMs")
    ] = None
    r"""Time spent idling in milliseconds."""

    total_power_take_off_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="totalPowerTakeOffDurationMs")
    ] = None
    r"""Time spent with power take off enabled while idling in milliseconds."""

    vehicle_summaries: Annotated[
        Optional[List[VehicleSummary]], pydantic.Field(alias="vehicleSummaries")
    ] = None
    r"""Summaries of vehicle efficiency for each vehicle the driver was driving during the given time period."""
