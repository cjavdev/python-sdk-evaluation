# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["V1VehicleSafetyScoreResponse", "HarshEvent"]


class HarshEvent(BaseModel):
    harsh_event_type: Optional[str] = FieldInfo(alias="harshEventType", default=None)
    """Sensor generated harsh event type."""

    timestamp_ms: Optional[int] = FieldInfo(alias="timestampMs", default=None)
    """Timestamp that the harsh event occurred in Unix milliseconds since epoch"""

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """Vehicle associated with the harsh event"""


class V1VehicleSafetyScoreResponse(BaseModel):
    crash_count: Optional[int] = FieldInfo(alias="crashCount", default=None)
    """Crash event count"""

    harsh_accel_count: Optional[int] = FieldInfo(alias="harshAccelCount", default=None)
    """Harsh acceleration event count"""

    harsh_braking_count: Optional[int] = FieldInfo(alias="harshBrakingCount", default=None)
    """Harsh braking event count"""

    harsh_events: Optional[List[HarshEvent]] = FieldInfo(alias="harshEvents", default=None)

    harsh_turning_count: Optional[int] = FieldInfo(alias="harshTurningCount", default=None)
    """Harsh turning event count"""

    safety_score: Optional[int] = FieldInfo(alias="safetyScore", default=None)
    """The vehicle’s Safety Score for the requested period.

    Note that if the vehicle has zero drive time in this period, the Safety Score
    will be returned as 100.
    """

    safety_score_rank: Optional[str] = FieldInfo(alias="safetyScoreRank", default=None)
    """Safety Score Rank"""

    time_over_speed_limit_ms: Optional[int] = FieldInfo(alias="timeOverSpeedLimitMs", default=None)
    """Amount of time driven over the speed limit in milliseconds"""

    total_distance_driven_meters: Optional[int] = FieldInfo(alias="totalDistanceDrivenMeters", default=None)
    """Total distance driven in meters"""

    total_harsh_event_count: Optional[int] = FieldInfo(alias="totalHarshEventCount", default=None)
    """Total harsh event count"""

    total_time_driven_ms: Optional[int] = FieldInfo(alias="totalTimeDrivenMs", default=None)
    """Amount of time driven in milliseconds"""

    vehicle_id: Optional[int] = FieldInfo(alias="vehicleId", default=None)
    """Vehicle ID"""
