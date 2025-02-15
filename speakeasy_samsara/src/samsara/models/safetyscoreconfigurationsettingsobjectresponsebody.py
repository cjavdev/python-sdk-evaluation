"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SafetyScoreConfigurationSettingsObjectResponseBodyTypedDict(TypedDict):
    r"""The configurable safety infraction weights."""

    ai_inattentive_driving_detection_weight: NotRequired[int]
    r"""Score weight for AI-detected inattentive driving behavior."""
    crash_weight: NotRequired[int]
    r"""Score weight for crash behavior."""
    defensive_driving_weight: NotRequired[int]
    r"""Score weight for defensive driving behavior. This behavior has a positive impact on the safety score."""
    did_not_yield_weight: NotRequired[int]
    r"""Score weight for driver not yielding."""
    drowsy_weight: NotRequired[int]
    r"""Score weight for drowsy behavior."""
    eating_drinking_weight: NotRequired[int]
    r"""Score weight for eating/drinking behavior."""
    following_distance_moderate_weight: NotRequired[int]
    r"""Score weight for moderate (2-4s) following distance behavior."""
    following_distance_severe_weight: NotRequired[int]
    r"""Score weight for severe (0-2s) following distance behavior."""
    following_distance_weight: NotRequired[int]
    r"""Score weight for following distance behavior."""
    forward_collision_warning_weight: NotRequired[int]
    r"""Score weight for forward collision warning behavior."""
    harsh_accel_weight: NotRequired[int]
    r"""Score weight for harsh acceleration behavior."""
    harsh_brake_weight: NotRequired[int]
    r"""Score weight for harsh braking behavior."""
    harsh_turn_weight: NotRequired[int]
    r"""Score weight for harsh turn behavior."""
    heavy_speeding_weight: NotRequired[int]
    r"""Score weight for heavy speeding (20-30% over limit)."""
    inattentive_driving_weight: NotRequired[int]
    r"""Score weight for inattentive driving behavior."""
    lane_departure_weight: NotRequired[int]
    r"""Score weight for lane departure behavior."""
    late_response_weight: NotRequired[int]
    r"""Score weight for late response behavior."""
    light_speeding_weight: NotRequired[int]
    r"""Score weight for light speeding (0-10% over limit)."""
    max_speed_weight: NotRequired[int]
    r"""Score weight for max speed events."""
    mobile_usage_weight: NotRequired[int]
    r"""Score weight for mobile usage behavior."""
    moderate_speeding_weight: NotRequired[int]
    r"""Score weight for moderate speeding (10-20% over limit)."""
    near_collision_weight: NotRequired[int]
    r"""Score weight for near collision behavior."""
    no_seatbelt_weight: NotRequired[int]
    r"""Score weight for no seatbelt behavior."""
    obstructed_camera_weight: NotRequired[int]
    r"""Score weight for obstructed camera behavior."""
    ran_red_light_weight: NotRequired[int]
    r"""Score weight for driver running red light."""
    rolling_stop_weight: NotRequired[int]
    r"""Score weight for rolling stop behavior."""
    severe_speeding_weight: NotRequired[int]
    r"""Score weight for severe speeding (over 30% over limit)."""
    smoking_weight: NotRequired[int]
    r"""Score weight for smoking behavior."""
    speeding_weight: NotRequired[int]
    r"""Score weight for manual speeding event."""


class SafetyScoreConfigurationSettingsObjectResponseBody(BaseModel):
    r"""The configurable safety infraction weights."""

    ai_inattentive_driving_detection_weight: Annotated[
        Optional[int], pydantic.Field(alias="aiInattentiveDrivingDetectionWeight")
    ] = None
    r"""Score weight for AI-detected inattentive driving behavior."""

    crash_weight: Annotated[Optional[int], pydantic.Field(alias="crashWeight")] = None
    r"""Score weight for crash behavior."""

    defensive_driving_weight: Annotated[
        Optional[int], pydantic.Field(alias="defensiveDrivingWeight")
    ] = None
    r"""Score weight for defensive driving behavior. This behavior has a positive impact on the safety score."""

    did_not_yield_weight: Annotated[
        Optional[int], pydantic.Field(alias="didNotYieldWeight")
    ] = None
    r"""Score weight for driver not yielding."""

    drowsy_weight: Annotated[Optional[int], pydantic.Field(alias="drowsyWeight")] = None
    r"""Score weight for drowsy behavior."""

    eating_drinking_weight: Annotated[
        Optional[int], pydantic.Field(alias="eatingDrinkingWeight")
    ] = None
    r"""Score weight for eating/drinking behavior."""

    following_distance_moderate_weight: Annotated[
        Optional[int], pydantic.Field(alias="followingDistanceModerateWeight")
    ] = None
    r"""Score weight for moderate (2-4s) following distance behavior."""

    following_distance_severe_weight: Annotated[
        Optional[int], pydantic.Field(alias="followingDistanceSevereWeight")
    ] = None
    r"""Score weight for severe (0-2s) following distance behavior."""

    following_distance_weight: Annotated[
        Optional[int], pydantic.Field(alias="followingDistanceWeight")
    ] = None
    r"""Score weight for following distance behavior."""

    forward_collision_warning_weight: Annotated[
        Optional[int], pydantic.Field(alias="forwardCollisionWarningWeight")
    ] = None
    r"""Score weight for forward collision warning behavior."""

    harsh_accel_weight: Annotated[
        Optional[int], pydantic.Field(alias="harshAccelWeight")
    ] = None
    r"""Score weight for harsh acceleration behavior."""

    harsh_brake_weight: Annotated[
        Optional[int], pydantic.Field(alias="harshBrakeWeight")
    ] = None
    r"""Score weight for harsh braking behavior."""

    harsh_turn_weight: Annotated[
        Optional[int], pydantic.Field(alias="harshTurnWeight")
    ] = None
    r"""Score weight for harsh turn behavior."""

    heavy_speeding_weight: Annotated[
        Optional[int], pydantic.Field(alias="heavySpeedingWeight")
    ] = None
    r"""Score weight for heavy speeding (20-30% over limit)."""

    inattentive_driving_weight: Annotated[
        Optional[int], pydantic.Field(alias="inattentiveDrivingWeight")
    ] = None
    r"""Score weight for inattentive driving behavior."""

    lane_departure_weight: Annotated[
        Optional[int], pydantic.Field(alias="laneDepartureWeight")
    ] = None
    r"""Score weight for lane departure behavior."""

    late_response_weight: Annotated[
        Optional[int], pydantic.Field(alias="lateResponseWeight")
    ] = None
    r"""Score weight for late response behavior."""

    light_speeding_weight: Annotated[
        Optional[int], pydantic.Field(alias="lightSpeedingWeight")
    ] = None
    r"""Score weight for light speeding (0-10% over limit)."""

    max_speed_weight: Annotated[
        Optional[int], pydantic.Field(alias="maxSpeedWeight")
    ] = None
    r"""Score weight for max speed events."""

    mobile_usage_weight: Annotated[
        Optional[int], pydantic.Field(alias="mobileUsageWeight")
    ] = None
    r"""Score weight for mobile usage behavior."""

    moderate_speeding_weight: Annotated[
        Optional[int], pydantic.Field(alias="moderateSpeedingWeight")
    ] = None
    r"""Score weight for moderate speeding (10-20% over limit)."""

    near_collision_weight: Annotated[
        Optional[int], pydantic.Field(alias="nearCollisionWeight")
    ] = None
    r"""Score weight for near collision behavior."""

    no_seatbelt_weight: Annotated[
        Optional[int], pydantic.Field(alias="noSeatbeltWeight")
    ] = None
    r"""Score weight for no seatbelt behavior."""

    obstructed_camera_weight: Annotated[
        Optional[int], pydantic.Field(alias="obstructedCameraWeight")
    ] = None
    r"""Score weight for obstructed camera behavior."""

    ran_red_light_weight: Annotated[
        Optional[int], pydantic.Field(alias="ranRedLightWeight")
    ] = None
    r"""Score weight for driver running red light."""

    rolling_stop_weight: Annotated[
        Optional[int], pydantic.Field(alias="rollingStopWeight")
    ] = None
    r"""Score weight for rolling stop behavior."""

    severe_speeding_weight: Annotated[
        Optional[int], pydantic.Field(alias="severeSpeedingWeight")
    ] = None
    r"""Score weight for severe speeding (over 30% over limit)."""

    smoking_weight: Annotated[Optional[int], pydantic.Field(alias="smokingWeight")] = (
        None
    )
    r"""Score weight for smoking behavior."""

    speeding_weight: Annotated[
        Optional[int], pydantic.Field(alias="speedingWeight")
    ] = None
    r"""Score weight for manual speeding event."""
