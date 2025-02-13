# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SafetySettingsGetSafetySettingsResponseBody",
    "Data",
    "DataDistractedDrivingDetectionAlerts",
    "DataDistractedDrivingDetectionAlertsInattentiveDrivingDetectionAlerts",
    "DataDistractedDrivingDetectionAlertsMobileUsageDetectionAlerts",
    "DataFollowingDistanceDetectionAlerts",
    "DataForwardCollisionDetectionAlerts",
    "DataHarshEventSensitivity",
    "DataHarshEventSensitivityHarshAccelSensitivityGForce",
    "DataHarshEventSensitivityHarshBrakeSensitivityGForce",
    "DataHarshEventSensitivityHarshTurnSensitivityGForce",
    "DataHarshEventSensitivityV2",
    "DataHarshEventSensitivityV2HarshAccelSensitivity",
    "DataHarshEventSensitivityV2HarshBrakeSensitivity",
    "DataHarshEventSensitivityV2HarshTurnSensitivity",
    "DataPolicyViolationsDetectionAlerts",
    "DataRollingStopDetectionAlerts",
    "DataSafetyScoreConfiguration",
    "DataSpeedingSettings",
    "DataSpeedingSettingsSeverityLevel",
    "DataVoiceCoaching",
]


class DataDistractedDrivingDetectionAlertsInattentiveDrivingDetectionAlerts(BaseModel):
    has_in_cab_audio_alerts_enabled: Optional[bool] = FieldInfo(alias="hasInCabAudioAlertsEnabled", default=None)
    """Indicates whether in-cab audio alerts for inattentive driving are turned on."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for inattentive driving is turned on."""

    severity: Optional[Literal["low", "medium", "high"]] = None
    """Severity of inattentive driving events.

    Options include low (alerts for all events), medium (alerts for medium and high
    severity events), and high (alerts for high severity events only). Valid values:
    `low`, `medium`, `high`
    """

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class DataDistractedDrivingDetectionAlertsMobileUsageDetectionAlerts(BaseModel):
    has_in_cab_audio_alerts_enabled: Optional[bool] = FieldInfo(alias="hasInCabAudioAlertsEnabled", default=None)
    """Indicates whether in-cab audio alerts for mobile usage are turned on."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for mobile usage is turned on."""

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class DataDistractedDrivingDetectionAlerts(BaseModel):
    inattentive_driving_detection_alerts: Optional[
        DataDistractedDrivingDetectionAlertsInattentiveDrivingDetectionAlerts
    ] = FieldInfo(alias="inattentiveDrivingDetectionAlerts", default=None)
    """Enables AI detection of inattentive driving events."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """
    Indicates whether AI event detection for distracted driving behaviors is turned
    on.
    """

    mobile_usage_detection_alerts: Optional[DataDistractedDrivingDetectionAlertsMobileUsageDetectionAlerts] = FieldInfo(
        alias="mobileUsageDetectionAlerts", default=None
    )
    """Enables AI detection of mobile usage events."""


class DataFollowingDistanceDetectionAlerts(BaseModel):
    duration_ms: Optional[int] = FieldInfo(alias="durationMs", default=None)
    """Duration of following distance at which to alert, measured in milliseconds."""

    has_in_cab_audio_alerts_enabled: Optional[bool] = FieldInfo(alias="hasInCabAudioAlertsEnabled", default=None)
    """Indicates whether in-cab audio alerts for following distance are turned on."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for following distance is turned on."""

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class DataForwardCollisionDetectionAlerts(BaseModel):
    has_in_cab_audio_alerts_enabled: Optional[bool] = FieldInfo(alias="hasInCabAudioAlertsEnabled", default=None)
    """Indicates whether in-cab audio alerts for forward collision are turned on."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for forward collision is turned on."""

    sensitivity: Optional[Literal["near", "medium", "far"]] = None
    """
    Ranges from near forward collision (results in fewer events) to far forward
    collision (results in more events). Valid values: `near`, `medium`, `far`
    """


class DataHarshEventSensitivityHarshAccelSensitivityGForce(BaseModel):
    heavy_duty: Optional[str] = FieldInfo(alias="heavyDuty", default=None)
    """Harsh acceleration sensitivity settings for heavy duty vehicle."""

    light_duty: Optional[str] = FieldInfo(alias="lightDuty", default=None)
    """Harsh acceleration sensitivity settings for light duty vehicle."""

    passenger: Optional[str] = None
    """Harsh acceleration sensitivity settings for passenger car."""


class DataHarshEventSensitivityHarshBrakeSensitivityGForce(BaseModel):
    heavy_duty: Optional[str] = FieldInfo(alias="heavyDuty", default=None)
    """Harsh brake sensitivity settings for heavy duty vehicle."""

    light_duty: Optional[str] = FieldInfo(alias="lightDuty", default=None)
    """Harsh brake sensitivity settings for light duty vehicle."""

    passenger: Optional[str] = None
    """Harsh brake sensitivity settings for passenger car."""


class DataHarshEventSensitivityHarshTurnSensitivityGForce(BaseModel):
    heavy_duty: Optional[str] = FieldInfo(alias="heavyDuty", default=None)
    """Harsh turn sensitivity settings for heavy duty vehicle."""

    light_duty: Optional[str] = FieldInfo(alias="lightDuty", default=None)
    """Harsh turn sensitivity settings for light duty vehicle."""

    passenger: Optional[str] = None
    """Harsh turn sensitivity settings for passenger car."""


class DataHarshEventSensitivity(BaseModel):
    harsh_accel_sensitivity_g_force: Optional[DataHarshEventSensitivityHarshAccelSensitivityGForce] = FieldInfo(
        alias="harshAccelSensitivityGForce", default=None
    )
    """The harsh acceleration sensitivity settings."""

    harsh_brake_sensitivity_g_force: Optional[DataHarshEventSensitivityHarshBrakeSensitivityGForce] = FieldInfo(
        alias="harshBrakeSensitivityGForce", default=None
    )
    """The harsh brake sensitivity settings."""

    harsh_turn_sensitivity_g_force: Optional[DataHarshEventSensitivityHarshTurnSensitivityGForce] = FieldInfo(
        alias="harshTurnSensitivityGForce", default=None
    )
    """The harsh turn sensitivity settings."""


class DataHarshEventSensitivityV2HarshAccelSensitivity(BaseModel):
    heavy_duty: Optional[Literal["unknown", "invalid", "off", "low", "normal", "high"]] = FieldInfo(
        alias="heavyDuty", default=None
    )
    """Harsh acceleration sensitivity settings for heavy duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `low`, `normal`, `high`
    """

    light_duty: Optional[Literal["unknown", "invalid", "off", "low", "normal", "high"]] = FieldInfo(
        alias="lightDuty", default=None
    )
    """Harsh acceleration sensitivity settings for light duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `low`, `normal`, `high`
    """

    passenger: Optional[Literal["unknown", "invalid", "off", "low", "normal", "high"]] = None
    """Harsh acceleration sensitivity settings for passenger car.

    Valid values: `unknown`, `invalid`, `off`, `low`, `normal`, `high`
    """


class DataHarshEventSensitivityV2HarshBrakeSensitivity(BaseModel):
    heavy_duty: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = FieldInfo(
        alias="heavyDuty", default=None
    )
    """Harsh brake sensitivity settings for heavy duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """

    light_duty: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = FieldInfo(
        alias="lightDuty", default=None
    )
    """Harsh brake sensitivity settings for light duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """

    passenger: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = None
    """Harsh brake sensitivity settings for passenger car.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """


class DataHarshEventSensitivityV2HarshTurnSensitivity(BaseModel):
    heavy_duty: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = FieldInfo(
        alias="heavyDuty", default=None
    )
    """Harsh turn sensitivity settings for heavy duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """

    light_duty: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = FieldInfo(
        alias="lightDuty", default=None
    )
    """Harsh turn sensitivity settings for light duty vehicle.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """

    passenger: Optional[Literal["unknown", "invalid", "off", "veryLow", "low", "normal", "high"]] = None
    """Harsh turn sensitivity settings for passenger car.

    Valid values: `unknown`, `invalid`, `off`, `veryLow`, `low`, `normal`, `high`
    """


class DataHarshEventSensitivityV2(BaseModel):
    harsh_accel_sensitivity: Optional[DataHarshEventSensitivityV2HarshAccelSensitivity] = FieldInfo(
        alias="harshAccelSensitivity", default=None
    )
    """The harsh acceleration sensitivity settings."""

    harsh_brake_sensitivity: Optional[DataHarshEventSensitivityV2HarshBrakeSensitivity] = FieldInfo(
        alias="harshBrakeSensitivity", default=None
    )
    """The harsh brake sensitivity settings."""

    harsh_turn_sensitivity: Optional[DataHarshEventSensitivityV2HarshTurnSensitivity] = FieldInfo(
        alias="harshTurnSensitivity", default=None
    )
    """The harsh turn sensitivity settings."""


class DataPolicyViolationsDetectionAlerts(BaseModel):
    events_available_for_testing: Optional[
        List[Literal["mobileUsage", "smoking", "eatingDrinking", "inwardCameraObstruction", "outwardCameraObstruction"]]
    ] = FieldInfo(alias="eventsAvailableForTesting", default=None)
    """List of selectable beta policy violation events to be tested."""

    events_to_coach: Optional[
        List[
            Literal[
                "noSeatbelt",
                "noMask",
                "mobileUsage",
                "smoking",
                "eatingDrinking",
                "inwardCameraObstruction",
                "outwardCameraObstruction",
            ]
        ]
    ] = FieldInfo(alias="eventsToCoach", default=None)
    """List of selectable policy violation events to enable coaching for."""

    has_in_cab_audio_alerts_enabled: Optional[bool] = FieldInfo(alias="hasInCabAudioAlertsEnabled", default=None)
    """Indicates whether in-cab audio alerts for rolling stops are turned on."""

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for rolling stops is turned on."""

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class DataRollingStopDetectionAlerts(BaseModel):
    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether AI event detection for rolling stops is turned on."""

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class DataSafetyScoreConfiguration(BaseModel):
    ai_inattentive_driving_detection_weight: Optional[int] = FieldInfo(
        alias="aiInattentiveDrivingDetectionWeight", default=None
    )
    """Score weight for AI-detected inattentive driving behavior."""

    crash_weight: Optional[int] = FieldInfo(alias="crashWeight", default=None)
    """Score weight for crash behavior."""

    defensive_driving_weight: Optional[int] = FieldInfo(alias="defensiveDrivingWeight", default=None)
    """Score weight for defensive driving behavior.

    This behavior has a positive impact on the safety score.
    """

    did_not_yield_weight: Optional[int] = FieldInfo(alias="didNotYieldWeight", default=None)
    """Score weight for driver not yielding."""

    drowsy_weight: Optional[int] = FieldInfo(alias="drowsyWeight", default=None)
    """Score weight for drowsy behavior."""

    eating_drinking_weight: Optional[int] = FieldInfo(alias="eatingDrinkingWeight", default=None)
    """Score weight for eating/drinking behavior."""

    following_distance_moderate_weight: Optional[int] = FieldInfo(alias="followingDistanceModerateWeight", default=None)
    """Score weight for moderate (2-4s) following distance behavior."""

    following_distance_severe_weight: Optional[int] = FieldInfo(alias="followingDistanceSevereWeight", default=None)
    """Score weight for severe (0-2s) following distance behavior."""

    following_distance_weight: Optional[int] = FieldInfo(alias="followingDistanceWeight", default=None)
    """Score weight for following distance behavior."""

    forward_collision_warning_weight: Optional[int] = FieldInfo(alias="forwardCollisionWarningWeight", default=None)
    """Score weight for forward collision warning behavior."""

    harsh_accel_weight: Optional[int] = FieldInfo(alias="harshAccelWeight", default=None)
    """Score weight for harsh acceleration behavior."""

    harsh_brake_weight: Optional[int] = FieldInfo(alias="harshBrakeWeight", default=None)
    """Score weight for harsh braking behavior."""

    harsh_turn_weight: Optional[int] = FieldInfo(alias="harshTurnWeight", default=None)
    """Score weight for harsh turn behavior."""

    heavy_speeding_weight: Optional[int] = FieldInfo(alias="heavySpeedingWeight", default=None)
    """Score weight for heavy speeding (20-30% over limit)."""

    inattentive_driving_weight: Optional[int] = FieldInfo(alias="inattentiveDrivingWeight", default=None)
    """Score weight for inattentive driving behavior."""

    lane_departure_weight: Optional[int] = FieldInfo(alias="laneDepartureWeight", default=None)
    """Score weight for lane departure behavior."""

    late_response_weight: Optional[int] = FieldInfo(alias="lateResponseWeight", default=None)
    """Score weight for late response behavior."""

    light_speeding_weight: Optional[int] = FieldInfo(alias="lightSpeedingWeight", default=None)
    """Score weight for light speeding (0-10% over limit)."""

    max_speed_weight: Optional[int] = FieldInfo(alias="maxSpeedWeight", default=None)
    """Score weight for max speed events."""

    mobile_usage_weight: Optional[int] = FieldInfo(alias="mobileUsageWeight", default=None)
    """Score weight for mobile usage behavior."""

    moderate_speeding_weight: Optional[int] = FieldInfo(alias="moderateSpeedingWeight", default=None)
    """Score weight for moderate speeding (10-20% over limit)."""

    near_collision_weight: Optional[int] = FieldInfo(alias="nearCollisionWeight", default=None)
    """Score weight for near collision behavior."""

    no_seatbelt_weight: Optional[int] = FieldInfo(alias="noSeatbeltWeight", default=None)
    """Score weight for no seatbelt behavior."""

    obstructed_camera_weight: Optional[int] = FieldInfo(alias="obstructedCameraWeight", default=None)
    """Score weight for obstructed camera behavior."""

    ran_red_light_weight: Optional[int] = FieldInfo(alias="ranRedLightWeight", default=None)
    """Score weight for driver running red light."""

    rolling_stop_weight: Optional[int] = FieldInfo(alias="rollingStopWeight", default=None)
    """Score weight for rolling stop behavior."""

    severe_speeding_weight: Optional[int] = FieldInfo(alias="severeSpeedingWeight", default=None)
    """Score weight for severe speeding (over 30% over limit)."""

    smoking_weight: Optional[int] = FieldInfo(alias="smokingWeight", default=None)
    """Score weight for smoking behavior."""

    speeding_weight: Optional[int] = FieldInfo(alias="speedingWeight", default=None)
    """Score weight for manual speeding event."""


class DataSpeedingSettingsSeverityLevel(BaseModel):
    duration_ms: int = FieldInfo(alias="durationMs")
    """
    The amount of time the vehicle is speeding in this category before being
    attributed to this level
    """

    is_enabled: bool = FieldInfo(alias="isEnabled")
    """Indicates the severity level is enabled"""

    severity_level: Literal["light", "moderate", "heavy", "severe"] = FieldInfo(alias="severityLevel")
    """The severity level name. Valid values: `light`, `moderate`, `heavy`, `severe`"""

    speed_over_limit_threshold: float = FieldInfo(alias="speedOverLimitThreshold")
    """
    The minimum speed above the speed limit that will get attributed to this
    severity level.
    """


class DataSpeedingSettings(BaseModel):
    severity_levels: Optional[List[DataSpeedingSettingsSeverityLevel]] = FieldInfo(alias="severityLevels", default=None)
    """The speeding severity levels for an organization."""

    unit: Optional[Literal["milesPerHour", "kilometersPerHour", "percentage"]] = None
    """
    The unit of measurement for speeding Valid values: `milesPerHour`,
    `kilometersPerHour`, `percentage`
    """


class DataVoiceCoaching(BaseModel):
    events_to_coach: Optional[
        List[Literal["crash", "inCabSpeeding", "maximumSpeed", "seatbeltUnbuckled", "harshDriving"]]
    ] = FieldInfo(alias="eventsToCoach", default=None)
    """Selected driving events will be enabled for voice coaching.

    Harsh driving events include harsh acceleration and harsh brake.
    """

    is_enabled: Optional[bool] = FieldInfo(alias="isEnabled", default=None)
    """Indicates whether voice coaching is turned on."""

    language: Optional[Literal["english", "spanish", "dutch", "englishUk", "italian", "french", "german"]] = None
    """The coaching language.

    The default language is English. Valid values: `english`, `spanish`, `dutch`,
    `englishUk`, `italian`, `french`, `german`
    """

    speeding_threshold_mph: Optional[float] = FieldInfo(alias="speedingThresholdMph", default=None)
    """Alert when speed is over this many miles per hour."""


class Data(BaseModel):
    default_vehicle_type: Literal["off", "automatic", "passengerCar", "lightTruck", "heavyDuty"] = FieldInfo(
        alias="defaultVehicleType"
    )
    """Default vehicle type (for newly added or activated vehicles).

    Valid values: `off`, `automatic`, `passengerCar`, `lightTruck`, `heavyDuty`
    """

    distracted_driving_detection_alerts: DataDistractedDrivingDetectionAlerts = FieldInfo(
        alias="distractedDrivingDetectionAlerts"
    )
    """
    Enables AI detection of distracted driving, surfaces events in Safety Inbox, and
    enables configurable alerts. By default, Distracted Driving will impact the
    drivers' safety score.
    """

    following_distance_detection_alerts: DataFollowingDistanceDetectionAlerts = FieldInfo(
        alias="followingDistanceDetectionAlerts"
    )
    """
    Enables AI detection of tailgating or unsafe following distances, surfaces
    events in Safety Inbox, and enables configurable alerts. By default, Following
    Distance will impact the drivers' safety score.
    """

    forward_collision_detection_alerts: DataForwardCollisionDetectionAlerts = FieldInfo(
        alias="forwardCollisionDetectionAlerts"
    )
    """
    Enables AI detection of near forward collisions, surfaces events in Safety
    Inbox, and enables configurable alerts. While the feature is in beta, it is only
    enabled during daytime driving hours. In-cab alerts are recommended for testing
    use only.
    """

    harsh_event_sensitivity: DataHarshEventSensitivity = FieldInfo(alias="harshEventSensitivity")
    """The configurable sensitivity for Harsh Event Detection on CM11/CM12/CM22
    devices.

    Sensitivity can be measured as a numeric g-force value or the following values:
    `Normal`, `Less Sensitive`, `More Sensitive`.
    """

    harsh_event_sensitivity_v2: DataHarshEventSensitivityV2 = FieldInfo(alias="harshEventSensitivityV2")
    """The configurable sensitivity for Harsh Event Detection.

    Does not apply to CM11/12/22 devices.
    """

    policy_violations_detection_alerts: DataPolicyViolationsDetectionAlerts = FieldInfo(
        alias="policyViolationsDetectionAlerts"
    )
    """
    Enables detection of policy violations, surfaces events in Safety Inbox, and
    enables configurable alerts. While the feature is in beta, in-cab alerts are
    recommended for testing use only.
    """

    rolling_stop_detection_alerts: DataRollingStopDetectionAlerts = FieldInfo(alias="rollingStopDetectionAlerts")
    """AI event detection settings for the rolling stop behavior.

    Detection is available in vehicles with compatible dash cams.
    """

    safety_score_configuration: DataSafetyScoreConfiguration = FieldInfo(alias="safetyScoreConfiguration")
    """The configurable safety infraction weights."""

    safety_score_target: int = FieldInfo(alias="safetyScoreTarget")
    """The fleet-wide target safety score that is shown on safety score graphs.

    A safety score goal of 0 means that score benchmarking is disabled.
    """

    speeding_settings: DataSpeedingSettings = FieldInfo(alias="speedingSettings")
    """Enables custom speeding levels."""

    voice_coaching: DataVoiceCoaching = FieldInfo(alias="voiceCoaching")
    """
    Enabling voice coaching will play messages for harsh events, speeding, and
    unbuckled seat belts.
    """


class SafetySettingsGetSafetySettingsResponseBody(BaseModel):
    data: List[Data]
    """Safety settings for a single organization."""
