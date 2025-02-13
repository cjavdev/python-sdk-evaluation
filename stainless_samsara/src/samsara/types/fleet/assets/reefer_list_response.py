# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ReeferListResponse",
    "Data",
    "DataReeferStats",
    "DataReeferStatsAmbientAirTemperature",
    "DataReeferStatsDischargeAirTemperature",
    "DataReeferStatsEngineHour",
    "DataReeferStatsFuelPercentage",
    "DataReeferStatsPowerStatus",
    "DataReeferStatsReeferAlarm",
    "DataReeferStatsReeferAlarmAlarm",
    "DataReeferStatsReturnAirTemperature",
    "DataReeferStatsSetPoint",
    "Pagination",
]


class DataReeferStatsAmbientAirTemperature(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Ambient temperature in millidegree Celsius."""


class DataReeferStatsDischargeAirTemperature(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Discharge temperature in millidegree Celsius."""


class DataReeferStatsEngineHour(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    engine_hours: Optional[int] = FieldInfo(alias="engineHours", default=None)
    """Engine hours of the reefer."""


class DataReeferStatsFuelPercentage(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    fuel_percentage: Optional[int] = FieldInfo(alias="fuelPercentage", default=None)
    """Fuel percentage of the reefer."""


class DataReeferStatsPowerStatus(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    status: Optional[Literal["Off", "Active", "Active (Start/Stop)", "Active (Continuous)"]] = None
    """Power status of the reefer.

    Valid values: `Off`, `Active`, `Active (Start/Stop)`, `Active (Continuous)`.
    """


class DataReeferStatsReeferAlarmAlarm(BaseModel):
    alarm_code: Optional[int] = FieldInfo(alias="alarmCode", default=None)
    """ID of the alarm"""

    description: Optional[str] = None
    """Description of the alarm"""

    operator_action: Optional[str] = FieldInfo(alias="operatorAction", default=None)
    """Recommended operator action"""

    severity: Optional[int] = None
    """
    Severity of the alarm: 1: OK to run, 2: Check as specified, 3: Take immediate
    action
    """


class DataReeferStatsReeferAlarm(BaseModel):
    alarms: Optional[List[DataReeferStatsReeferAlarmAlarm]] = None

    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp when the alarms were reported, in Unix milliseconds since epoch"""


class DataReeferStatsReturnAirTemperature(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Return air temperature in millidegree Celsius."""


class DataReeferStatsSetPoint(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Set point temperature in millidegree Celsius."""


class DataReeferStats(BaseModel):
    ambient_air_temperature: Optional[List[DataReeferStatsAmbientAirTemperature]] = FieldInfo(
        alias="ambientAirTemperature", default=None
    )
    """Ambient temperature of the reefer.

    This is the temperature of the air around the Samsara Asset Gateway.
    """

    discharge_air_temperature: Optional[List[DataReeferStatsDischargeAirTemperature]] = FieldInfo(
        alias="dischargeAirTemperature", default=None
    )
    """Discharge air temperature of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    engine_hours: Optional[List[DataReeferStatsEngineHour]] = FieldInfo(alias="engineHours", default=None)
    """Engine hours of the reefer"""

    fuel_percentage: Optional[List[DataReeferStatsFuelPercentage]] = FieldInfo(alias="fuelPercentage", default=None)
    """Fuel percentage of the reefer"""

    power_status: Optional[List[DataReeferStatsPowerStatus]] = FieldInfo(alias="powerStatus", default=None)
    """Power status of the reefer"""

    reefer_alarms: Optional[List[DataReeferStatsReeferAlarm]] = FieldInfo(alias="reeferAlarms", default=None)
    """Reefer alarms"""

    return_air_temperature: Optional[List[DataReeferStatsReturnAirTemperature]] = FieldInfo(
        alias="returnAirTemperature", default=None
    )
    """Return air temperature of the reefer.

    This is the temperature read by the reefer module (Carrier, Thermo King) that
    shows the temperature of the air as it enters the system.
    """

    set_point: Optional[List[DataReeferStatsSetPoint]] = FieldInfo(alias="setPoint", default=None)
    """Set point temperature of the reefer"""


class Data(BaseModel):
    id: Optional[int] = None
    """Asset ID"""

    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Asset type"""

    name: Optional[str] = None
    """Asset name"""

    reefer_stats: Optional[DataReeferStats] = FieldInfo(alias="reeferStats", default=None)
    """Contains all the state changes of the reefer for the included stat types.

    Each state change is recorded independently, so the number of records in each
    array may differ depending on when that stat changed state. Stat types with a
    continuous value (such as temperature) will be recorded at different rates
    depending on the reefer, but generally readings have a frequency on the order of
    seconds.
    """


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's
    'startingAfter' query parameter.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """True if there are more pages of results after this response."""

    has_prev_page: bool = FieldInfo(alias="hasPrevPage")
    """True if there are more pages of results before this response."""

    start_cursor: str = FieldInfo(alias="startCursor")
    """Cursor identifier representing the first element in the response.

    This value should be used in conjunction with a subsequent request's
    'ending_before' query parameter.
    """


class ReeferListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
