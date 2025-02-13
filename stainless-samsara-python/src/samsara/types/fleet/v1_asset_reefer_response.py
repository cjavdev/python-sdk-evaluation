# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "V1AssetReeferResponse",
    "ReeferStats",
    "ReeferStatsAlarm",
    "ReeferStatsAlarmAlarm",
    "ReeferStatsEngineHour",
    "ReeferStatsFuelPercentage",
    "ReeferStatsPowerStatus",
    "ReeferStatsReturnAirTemp",
    "ReeferStatsSetPoint",
]


class ReeferStatsAlarmAlarm(BaseModel):
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


class ReeferStatsAlarm(BaseModel):
    alarms: Optional[List[ReeferStatsAlarmAlarm]] = None

    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp when the alarms were reported, in Unix milliseconds since epoch"""


class ReeferStatsEngineHour(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    engine_hours: Optional[int] = FieldInfo(alias="engineHours", default=None)
    """Engine hours of the reefer."""


class ReeferStatsFuelPercentage(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    fuel_percentage: Optional[int] = FieldInfo(alias="fuelPercentage", default=None)
    """Fuel percentage of the reefer."""


class ReeferStatsPowerStatus(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    status: Optional[str] = None
    """Power status of the reefer.

    Valid values: `Off`, `Active`, `Active (Start/Stop)`, `Active (Continuous)`.
    """


class ReeferStatsReturnAirTemp(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Return air temperature in millidegree Celsius."""


class ReeferStatsSetPoint(BaseModel):
    changed_at_ms: Optional[int] = FieldInfo(alias="changedAtMs", default=None)
    """Timestamp in Unix milliseconds since epoch."""

    temp_in_milli_c: Optional[int] = FieldInfo(alias="tempInMilliC", default=None)
    """Set point temperature in millidegree Celsius."""


class ReeferStats(BaseModel):
    alarms: Optional[List[ReeferStatsAlarm]] = None
    """Reefer alarms"""

    engine_hours: Optional[List[ReeferStatsEngineHour]] = FieldInfo(alias="engineHours", default=None)
    """Engine hours of the reefer"""

    fuel_percentage: Optional[List[ReeferStatsFuelPercentage]] = FieldInfo(alias="fuelPercentage", default=None)
    """Fuel percentage of the reefer"""

    power_status: Optional[List[ReeferStatsPowerStatus]] = FieldInfo(alias="powerStatus", default=None)
    """Power status of the reefer"""

    return_air_temp: Optional[List[ReeferStatsReturnAirTemp]] = FieldInfo(alias="returnAirTemp", default=None)
    """Return air temperature of the reefer"""

    set_point: Optional[List[ReeferStatsSetPoint]] = FieldInfo(alias="setPoint", default=None)
    """Set point temperature of the reefer"""


class V1AssetReeferResponse(BaseModel):
    id: Optional[int] = None
    """Asset ID"""

    asset_type: Optional[str] = FieldInfo(alias="assetType", default=None)
    """Asset type"""

    name: Optional[str] = None
    """Asset name"""

    reefer_stats: Optional[ReeferStats] = FieldInfo(alias="reeferStats", default=None)
