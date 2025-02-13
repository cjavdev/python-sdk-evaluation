"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverEfficiencyPercentageDataObjectResponseBodyTypedDict(TypedDict):
    r"""Driver Efficiency percentage data. This object is returned when the “percentage” format is specified in “dataFormats”."""

    idling_percentage: float
    r"""Percentage of time a driver is idling."""
    anticipation_percentage: NotRequired[float]
    r"""Percentage of time a driver is in quickly breaking events vs total breaking events."""
    coasting_percentage: NotRequired[float]
    r"""Percentage of time a driver is in coasting."""
    cruise_control_percentage: NotRequired[float]
    r"""Percentage of time a vehicle is in cruise control."""
    green_band_percentage: NotRequired[float]
    r"""Percentage of time a driver is driving within the green band."""
    high_grade_road_driving_percentage: NotRequired[float]
    r"""Percentage of time a driver is driving on high-grade road."""
    high_torque_percentage: NotRequired[float]
    r"""Percentage of time a driver is driving in high torque."""
    over_speed_percentage: NotRequired[float]
    r"""Percentage of time a driver is in over-speeding."""
    wear_free_brake_percentage: NotRequired[float]
    r"""Percentage of time a driver is in wear-free breaking."""


class DriverEfficiencyPercentageDataObjectResponseBody(BaseModel):
    r"""Driver Efficiency percentage data. This object is returned when the “percentage” format is specified in “dataFormats”."""

    idling_percentage: Annotated[float, pydantic.Field(alias="idlingPercentage")]
    r"""Percentage of time a driver is idling."""

    anticipation_percentage: Annotated[
        Optional[float], pydantic.Field(alias="anticipationPercentage")
    ] = None
    r"""Percentage of time a driver is in quickly breaking events vs total breaking events."""

    coasting_percentage: Annotated[
        Optional[float], pydantic.Field(alias="coastingPercentage")
    ] = None
    r"""Percentage of time a driver is in coasting."""

    cruise_control_percentage: Annotated[
        Optional[float], pydantic.Field(alias="cruiseControlPercentage")
    ] = None
    r"""Percentage of time a vehicle is in cruise control."""

    green_band_percentage: Annotated[
        Optional[float], pydantic.Field(alias="greenBandPercentage")
    ] = None
    r"""Percentage of time a driver is driving within the green band."""

    high_grade_road_driving_percentage: Annotated[
        Optional[float], pydantic.Field(alias="highGradeRoadDrivingPercentage")
    ] = None
    r"""Percentage of time a driver is driving on high-grade road."""

    high_torque_percentage: Annotated[
        Optional[float], pydantic.Field(alias="highTorquePercentage")
    ] = None
    r"""Percentage of time a driver is driving in high torque."""

    over_speed_percentage: Annotated[
        Optional[float], pydantic.Field(alias="overSpeedPercentage")
    ] = None
    r"""Percentage of time a driver is in over-speeding."""

    wear_free_brake_percentage: Annotated[
        Optional[float], pydantic.Field(alias="wearFreeBrakePercentage")
    ] = None
    r"""Percentage of time a driver is in wear-free breaking."""
