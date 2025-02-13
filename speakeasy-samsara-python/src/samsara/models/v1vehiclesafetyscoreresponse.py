"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1safetyreportharshevent import (
    V1SafetyReportHarshEvent,
    V1SafetyReportHarshEventTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class V1VehicleSafetyScoreResponseTypedDict(TypedDict):
    r"""Safety score details for a vehicle"""

    crash_count: NotRequired[int]
    r"""Crash event count"""
    harsh_accel_count: NotRequired[int]
    r"""Harsh acceleration event count"""
    harsh_braking_count: NotRequired[int]
    r"""Harsh braking event count"""
    harsh_events: NotRequired[List[V1SafetyReportHarshEventTypedDict]]
    harsh_turning_count: NotRequired[int]
    r"""Harsh turning event count"""
    safety_score: NotRequired[int]
    r"""The vehicle’s Safety Score for the requested period. Note that if the vehicle has zero drive time in this period, the Safety Score will be returned as 100."""
    safety_score_rank: NotRequired[str]
    r"""Safety Score Rank"""
    time_over_speed_limit_ms: NotRequired[int]
    r"""Amount of time driven over the speed limit in milliseconds"""
    total_distance_driven_meters: NotRequired[int]
    r"""Total distance driven in meters"""
    total_harsh_event_count: NotRequired[int]
    r"""Total harsh event count"""
    total_time_driven_ms: NotRequired[int]
    r"""Amount of time driven in milliseconds"""
    vehicle_id: NotRequired[int]
    r"""Vehicle ID"""


class V1VehicleSafetyScoreResponse(BaseModel):
    r"""Safety score details for a vehicle"""

    crash_count: Annotated[Optional[int], pydantic.Field(alias="crashCount")] = None
    r"""Crash event count"""

    harsh_accel_count: Annotated[
        Optional[int], pydantic.Field(alias="harshAccelCount")
    ] = None
    r"""Harsh acceleration event count"""

    harsh_braking_count: Annotated[
        Optional[int], pydantic.Field(alias="harshBrakingCount")
    ] = None
    r"""Harsh braking event count"""

    harsh_events: Annotated[
        Optional[List[V1SafetyReportHarshEvent]], pydantic.Field(alias="harshEvents")
    ] = None

    harsh_turning_count: Annotated[
        Optional[int], pydantic.Field(alias="harshTurningCount")
    ] = None
    r"""Harsh turning event count"""

    safety_score: Annotated[Optional[int], pydantic.Field(alias="safetyScore")] = None
    r"""The vehicle’s Safety Score for the requested period. Note that if the vehicle has zero drive time in this period, the Safety Score will be returned as 100."""

    safety_score_rank: Annotated[
        Optional[str], pydantic.Field(alias="safetyScoreRank")
    ] = None
    r"""Safety Score Rank"""

    time_over_speed_limit_ms: Annotated[
        Optional[int], pydantic.Field(alias="timeOverSpeedLimitMs")
    ] = None
    r"""Amount of time driven over the speed limit in milliseconds"""

    total_distance_driven_meters: Annotated[
        Optional[int], pydantic.Field(alias="totalDistanceDrivenMeters")
    ] = None
    r"""Total distance driven in meters"""

    total_harsh_event_count: Annotated[
        Optional[int], pydantic.Field(alias="totalHarshEventCount")
    ] = None
    r"""Total harsh event count"""

    total_time_driven_ms: Annotated[
        Optional[int], pydantic.Field(alias="totalTimeDrivenMs")
    ] = None
    r"""Amount of time driven in milliseconds"""

    vehicle_id: Annotated[Optional[int], pydantic.Field(alias="vehicleId")] = None
    r"""Vehicle ID"""
