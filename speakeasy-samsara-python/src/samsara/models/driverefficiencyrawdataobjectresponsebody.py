"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverEfficiencyRawDataObjectResponseBodyTypedDict(TypedDict):
    r"""Driver Efficiency raw data. This object is returned when the “raw” format is specified in “dataFormats”."""

    drive_time_duration_ms: int
    r"""Total driving time in milliseconds."""
    engine_on_duration_ms: int
    r"""Total engine-on time in milliseconds."""
    idling_duration_ms: int
    r"""Time spent idling in milliseconds."""
    total_brake_duration_ms: int
    r"""Total breaking time in milliseconds."""
    anticipation_brake_event_count: NotRequired[int]
    r"""Total number of quick braking events (less than one second after accelerating)."""
    average_vehicle_weight_kg: NotRequired[int]
    r"""Average vehicle weight in kilograms."""
    coasting_duration_ms: NotRequired[int]
    r"""Time spent without engaging the accelerator or brake in milliseconds."""
    cruise_control_duration_ms: NotRequired[int]
    r"""Time spent in cruise control in milliseconds."""
    green_band_duration_ms: NotRequired[int]
    r"""Time spent driving within the configurable green band in milliseconds."""
    high_grade_road_driving_duration_ms: NotRequired[int]
    r"""Time spent driving on high-grade roads in milliseconds."""
    high_torque_duration_ms: NotRequired[int]
    r"""Time the vehicle engine torque is greater than 90% in milliseconds."""
    over_speed_duration_ms: NotRequired[int]
    r"""Time spent over-speeding in milliseconds."""
    total_brake_event_count: NotRequired[int]
    r"""Total number of brake events."""
    wear_free_brake_duration_ms: NotRequired[int]
    r"""Time spent ware-free breaking in milliseconds."""


class DriverEfficiencyRawDataObjectResponseBody(BaseModel):
    r"""Driver Efficiency raw data. This object is returned when the “raw” format is specified in “dataFormats”."""

    drive_time_duration_ms: Annotated[int, pydantic.Field(alias="driveTimeDurationMs")]
    r"""Total driving time in milliseconds."""

    engine_on_duration_ms: Annotated[int, pydantic.Field(alias="engineOnDurationMs")]
    r"""Total engine-on time in milliseconds."""

    idling_duration_ms: Annotated[int, pydantic.Field(alias="idlingDurationMs")]
    r"""Time spent idling in milliseconds."""

    total_brake_duration_ms: Annotated[
        int, pydantic.Field(alias="totalBrakeDurationMs")
    ]
    r"""Total breaking time in milliseconds."""

    anticipation_brake_event_count: Annotated[
        Optional[int], pydantic.Field(alias="anticipationBrakeEventCount")
    ] = None
    r"""Total number of quick braking events (less than one second after accelerating)."""

    average_vehicle_weight_kg: Annotated[
        Optional[int], pydantic.Field(alias="averageVehicleWeightKg")
    ] = None
    r"""Average vehicle weight in kilograms."""

    coasting_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="coastingDurationMs")
    ] = None
    r"""Time spent without engaging the accelerator or brake in milliseconds."""

    cruise_control_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="cruiseControlDurationMs")
    ] = None
    r"""Time spent in cruise control in milliseconds."""

    green_band_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="greenBandDurationMs")
    ] = None
    r"""Time spent driving within the configurable green band in milliseconds."""

    high_grade_road_driving_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="highGradeRoadDrivingDurationMs")
    ] = None
    r"""Time spent driving on high-grade roads in milliseconds."""

    high_torque_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="highTorqueDurationMs")
    ] = None
    r"""Time the vehicle engine torque is greater than 90% in milliseconds."""

    over_speed_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="overSpeedDurationMs")
    ] = None
    r"""Time spent over-speeding in milliseconds."""

    total_brake_event_count: Annotated[
        Optional[int], pydantic.Field(alias="totalBrakeEventCount")
    ] = None
    r"""Total number of brake events."""

    wear_free_brake_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="wearFreeBrakeDurationMs")
    ] = None
    r"""Time spent ware-free breaking in milliseconds."""
