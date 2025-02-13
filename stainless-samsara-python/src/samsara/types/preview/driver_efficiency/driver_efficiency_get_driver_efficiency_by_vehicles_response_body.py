# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody",
    "Data",
    "DataDifficultyScore",
    "DataPercentageData",
    "DataRawData",
    "DataScoreData",
    "Pagination",
]


class DataDifficultyScore(BaseModel):
    overall_score: Optional[str] = FieldInfo(alias="overallScore", default=None)
    """Represents the overall difficulty score. It has scores from 1 to 5."""

    topography_score: Optional[str] = FieldInfo(alias="topographyScore", default=None)
    """Represents the topography difficulty score. It has scores from 1 to 5."""

    vehicle_weight_score: Optional[str] = FieldInfo(alias="vehicleWeightScore", default=None)
    """Represents the average vehicle weight score. It has scores from 1 to 5."""


class DataPercentageData(BaseModel):
    idling_percentage: float = FieldInfo(alias="idlingPercentage")
    """Percentage of time a driver is idling."""

    anticipation_percentage: Optional[float] = FieldInfo(alias="anticipationPercentage", default=None)
    """
    Percentage of time a driver is in quickly breaking events vs total breaking
    events.
    """

    coasting_percentage: Optional[float] = FieldInfo(alias="coastingPercentage", default=None)
    """Percentage of time a driver is in coasting."""

    cruise_control_percentage: Optional[float] = FieldInfo(alias="cruiseControlPercentage", default=None)
    """Percentage of time a vehicle is in cruise control."""

    green_band_percentage: Optional[float] = FieldInfo(alias="greenBandPercentage", default=None)
    """Percentage of time a driver is driving within the green band."""

    high_grade_road_driving_percentage: Optional[float] = FieldInfo(
        alias="highGradeRoadDrivingPercentage", default=None
    )
    """Percentage of time a driver is driving on high-grade road."""

    high_torque_percentage: Optional[float] = FieldInfo(alias="highTorquePercentage", default=None)
    """Percentage of time a driver is driving in high torque."""

    over_speed_percentage: Optional[float] = FieldInfo(alias="overSpeedPercentage", default=None)
    """Percentage of time a driver is in over-speeding."""

    wear_free_brake_percentage: Optional[float] = FieldInfo(alias="wearFreeBrakePercentage", default=None)
    """Percentage of time a driver is in wear-free breaking."""


class DataRawData(BaseModel):
    drive_time_duration_ms: int = FieldInfo(alias="driveTimeDurationMs")
    """Total driving time in milliseconds."""

    engine_on_duration_ms: int = FieldInfo(alias="engineOnDurationMs")
    """Total engine-on time in milliseconds."""

    idling_duration_ms: int = FieldInfo(alias="idlingDurationMs")
    """Time spent idling in milliseconds."""

    total_brake_duration_ms: int = FieldInfo(alias="totalBrakeDurationMs")
    """Total breaking time in milliseconds."""

    anticipation_brake_event_count: Optional[int] = FieldInfo(alias="anticipationBrakeEventCount", default=None)
    """Total number of quick braking events (less than one second after accelerating)."""

    average_vehicle_weight_kg: Optional[int] = FieldInfo(alias="averageVehicleWeightKg", default=None)
    """Average vehicle weight in kilograms."""

    coasting_duration_ms: Optional[int] = FieldInfo(alias="coastingDurationMs", default=None)
    """Time spent without engaging the accelerator or brake in milliseconds."""

    cruise_control_duration_ms: Optional[int] = FieldInfo(alias="cruiseControlDurationMs", default=None)
    """Time spent in cruise control in milliseconds."""

    green_band_duration_ms: Optional[int] = FieldInfo(alias="greenBandDurationMs", default=None)
    """Time spent driving within the configurable green band in milliseconds."""

    high_grade_road_driving_duration_ms: Optional[int] = FieldInfo(alias="highGradeRoadDrivingDurationMs", default=None)
    """Time spent driving on high-grade roads in milliseconds."""

    high_torque_duration_ms: Optional[int] = FieldInfo(alias="highTorqueDurationMs", default=None)
    """Time the vehicle engine torque is greater than 90% in milliseconds."""

    over_speed_duration_ms: Optional[int] = FieldInfo(alias="overSpeedDurationMs", default=None)
    """Time spent over-speeding in milliseconds."""

    total_brake_event_count: Optional[int] = FieldInfo(alias="totalBrakeEventCount", default=None)
    """Total number of brake events."""

    wear_free_brake_duration_ms: Optional[int] = FieldInfo(alias="wearFreeBrakeDurationMs", default=None)
    """Time spent ware-free breaking in milliseconds."""


class DataScoreData(BaseModel):
    overall_score: str = FieldInfo(alias="overallScore")
    """Represents the overall score for the driver.

    The score will be in either number (0-100) as a string or letter format (A-G)
    depending on the organisation config.
    """

    anticipation_score: Optional[str] = FieldInfo(alias="anticipationScore", default=None)
    """Represents the anticipation score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    coasting_score: Optional[str] = FieldInfo(alias="coastingScore", default=None)
    """Represents the coasting score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    cruise_control_score: Optional[str] = FieldInfo(alias="cruiseControlScore", default=None)
    """Represents the cruise control score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    green_band_score: Optional[str] = FieldInfo(alias="greenBandScore", default=None)
    """Represents the green band score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    high_torque_score: Optional[str] = FieldInfo(alias="highTorqueScore", default=None)
    """Represents the high torque score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    idling_score: Optional[str] = FieldInfo(alias="idlingScore", default=None)
    """
    Represents the idling score for the driver.The score will be in either number or
    letter format depending on the organisation config.
    """

    over_speed_score: Optional[str] = FieldInfo(alias="overSpeedScore", default=None)
    """Represents the over speed score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """

    wear_free_brake_score: Optional[str] = FieldInfo(alias="wearFreeBrakeScore", default=None)
    """Represents the ware-free breaking score for the driver.

    The score will be in either number or letter format depending on the
    organisation config.
    """


class Data(BaseModel):
    vehicle_id: str = FieldInfo(alias="vehicleId")
    """ID of the vehicle."""

    difficulty_score: Optional[DataDifficultyScore] = FieldInfo(alias="difficultyScore", default=None)
    """Difficulty score won't be available if there is no data to compute it against."""

    percentage_data: Optional[DataPercentageData] = FieldInfo(alias="percentageData", default=None)
    """Driver Efficiency percentage data.

    This object is returned when the “percentage” format is specified in
    “dataFormats”.
    """

    raw_data: Optional[DataRawData] = FieldInfo(alias="rawData", default=None)
    """Driver Efficiency raw data.

    This object is returned when the “raw” format is specified in “dataFormats”.
    """

    score_data: Optional[DataScoreData] = FieldInfo(alias="scoreData", default=None)
    """Driver Efficiency score data.

    This object is returned by default or when the “score” format is specified in
    “dataFormats”.
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


class DriverEfficiencyGetDriverEfficiencyByVehiclesResponseBody(BaseModel):
    data: List[Data]
    """List of driver efficiency data associated with vehicles."""

    pagination: Pagination
    """Pagination parameters."""
