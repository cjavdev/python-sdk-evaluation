# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "StatListResponse",
    "Data",
    "DataCarrierReeferState",
    "DataGps",
    "DataGpsReverseGeo",
    "DataGpsOdometerMeters",
    "DataReeferAlarms",
    "DataReeferAlarmsAlarm",
    "DataReeferAmbientAirTemperatureMilliC",
    "DataReeferDoorStateZone1",
    "DataReeferDoorStateZone2",
    "DataReeferDoorStateZone3",
    "DataReeferFuelPercent",
    "DataReeferObdEngineSeconds",
    "DataReeferReturnAirTemperatureMilliCZone1",
    "DataReeferReturnAirTemperatureMilliCZone2",
    "DataReeferReturnAirTemperatureMilliCZone3",
    "DataReeferRunMode",
    "DataReeferSetPointTemperatureMilliCZone1",
    "DataReeferSetPointTemperatureMilliCZone2",
    "DataReeferSetPointTemperatureMilliCZone3",
    "DataReeferStateZone1",
    "DataReeferStateZone2",
    "DataReeferStateZone3",
    "DataReeferSupplyAirTemperatureMilliCZone1",
    "DataReeferSupplyAirTemperatureMilliCZone2",
    "DataReeferSupplyAirTemperatureMilliCZone3",
    "Pagination",
]


class DataCarrierReeferState(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The overall state of the multizone carrier reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate of the multizone carrier reefer, if available."""


class DataGpsReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGps(BaseModel):
    latitude: float
    """GPS latitude represented in degrees."""

    longitude: float
    """GPS longitude represented in degrees."""

    time: str
    """UTC timestamp in RFC 3339 format."""

    heading_degrees: Optional[int] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the trailer in degrees."""

    reverse_geo: Optional[DataGpsReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information"""

    speed_miles_per_hour: Optional[int] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the trailer in miles per hour."""


class DataGpsOdometerMeters(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    Number of meters the trailer has traveled according to the GPS calculations and
    the manually specified odometer reading.
    """


class DataReeferAlarmsAlarm(BaseModel):
    alarm_code: str = FieldInfo(alias="alarmCode")
    """The ID of the alarm."""

    description: str
    """The description of the alarm."""

    operator_action: str = FieldInfo(alias="operatorAction")
    """The recommended operator action."""

    severity: int
    """The severity of the alarm.

    `1`: Ok to run, `2`: Check as specified, `3`: Take immediate action.
    """


class DataReeferAlarms(BaseModel):
    alarms: List[DataReeferAlarmsAlarm]
    """The alarms reported by the reefer."""

    time: str
    """UTC timestamp in RFC 3339 format."""


class DataReeferAmbientAirTemperatureMilliC(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The ambient air temperature reading of the reefer in millidegree Celsius."""


class DataReeferDoorStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferDoorStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: Literal["open", "closed"]
    """The door state of zone 2 of the reefer. Valid values: `open`, `closed`"""


class DataReeferFuelPercent(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The fuel level in percentage points (e.g. `99`, `50`, etc)."""


class DataReeferObdEngineSeconds(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """
    The number of seconds the reefer has been on according to the onboard
    diagnostics.
    """


class DataReeferReturnAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferReturnAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The return air temperature reading in millidegree Celsius."""


class DataReeferRunMode(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The operational mode of the reefer."""


class DataReeferSetPointTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferSetPointTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The set point temperature reading in millidegree Celsius."""


class DataReeferStateZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 1 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 1 of the reefer, if available."""


class DataReeferStateZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 2 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 2 of the reefer, if available."""


class DataReeferStateZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: str
    """The state zone 3 of the reefer."""

    substate_value: Optional[str] = FieldInfo(alias="substateValue", default=None)
    """The substate zone 3 of the reefer, if available."""


class DataReeferSupplyAirTemperatureMilliCZone1(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone2(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class DataReeferSupplyAirTemperatureMilliCZone3(BaseModel):
    time: str
    """UTC timestamp in RFC 3339 format."""

    value: int
    """The supply or discharge air temperature reading in millidegree Celsius."""


class Data(BaseModel):
    id: str
    """ID of the trailer."""

    name: str
    """Name of the vehicle."""

    carrier_reefer_state: Optional[DataCarrierReeferState] = FieldInfo(alias="carrierReeferState", default=None)
    """Reefer state event."""

    gps: Optional[DataGps] = None
    """GPS location data for the trailer."""

    gps_odometer_meters: Optional[DataGpsOdometerMeters] = FieldInfo(alias="gpsOdometerMeters", default=None)
    """Trailer GPS odometer event."""

    reefer_alarms: Optional[DataReeferAlarms] = FieldInfo(alias="reeferAlarms", default=None)
    """Alarms that have been emitted by the reefer."""

    reefer_ambient_air_temperature_milli_c: Optional[DataReeferAmbientAirTemperatureMilliC] = FieldInfo(
        alias="reeferAmbientAirTemperatureMilliC", default=None
    )
    """Reefer ambient air temperature reading."""

    reefer_door_state_zone1: Optional[DataReeferDoorStateZone1] = FieldInfo(alias="reeferDoorStateZone1", default=None)
    """The door state of the reefer."""

    reefer_door_state_zone2: Optional[DataReeferDoorStateZone2] = FieldInfo(alias="reeferDoorStateZone2", default=None)
    """The door state of the reefer."""

    reefer_door_state_zone3: Optional[DataReeferDoorStateZone3] = FieldInfo(alias="reeferDoorStateZone3", default=None)
    """The door state of the reefer."""

    reefer_fuel_percent: Optional[DataReeferFuelPercent] = FieldInfo(alias="reeferFuelPercent", default=None)
    """The fuel percentage of the reefer."""

    reefer_obd_engine_seconds: Optional[DataReeferObdEngineSeconds] = FieldInfo(
        alias="reeferObdEngineSeconds", default=None
    )
    """Reefer onboard engine seconds reading."""

    reefer_return_air_temperature_milli_c_zone1: Optional[DataReeferReturnAirTemperatureMilliCZone1] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone1", default=None
    )
    """Return air temperature of zone 1 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone2: Optional[DataReeferReturnAirTemperatureMilliCZone2] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone2", default=None
    )
    """Return air temperature of zone 2 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_return_air_temperature_milli_c_zone3: Optional[DataReeferReturnAirTemperatureMilliCZone3] = FieldInfo(
        alias="reeferReturnAirTemperatureMilliCZone3", default=None
    )
    """Return air temperature of zone 3 of the reefer.

    This is the temperature of the air as it enters the cooling unit.
    """

    reefer_run_mode: Optional[DataReeferRunMode] = FieldInfo(alias="reeferRunMode", default=None)
    """The run mode of the reefer."""

    reefer_set_point_temperature_milli_c_zone1: Optional[DataReeferSetPointTemperatureMilliCZone1] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone1", default=None
    )
    """Set point temperature of zone 1 of the reefer."""

    reefer_set_point_temperature_milli_c_zone2: Optional[DataReeferSetPointTemperatureMilliCZone2] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone2", default=None
    )
    """Set point temperature of zone 2 of the reefer."""

    reefer_set_point_temperature_milli_c_zone3: Optional[DataReeferSetPointTemperatureMilliCZone3] = FieldInfo(
        alias="reeferSetPointTemperatureMilliCZone3", default=None
    )
    """Set point temperature of zone 3 of the reefer."""

    reefer_state_zone1: Optional[DataReeferStateZone1] = FieldInfo(alias="reeferStateZone1", default=None)
    """Reefer state event."""

    reefer_state_zone2: Optional[DataReeferStateZone2] = FieldInfo(alias="reeferStateZone2", default=None)
    """Reefer state event."""

    reefer_state_zone3: Optional[DataReeferStateZone3] = FieldInfo(alias="reeferStateZone3", default=None)
    """Reefer state event."""

    reefer_supply_air_temperature_milli_c_zone1: Optional[DataReeferSupplyAirTemperatureMilliCZone1] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone1", default=None
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone2: Optional[DataReeferSupplyAirTemperatureMilliCZone2] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone2", default=None
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
    """

    reefer_supply_air_temperature_milli_c_zone3: Optional[DataReeferSupplyAirTemperatureMilliCZone3] = FieldInfo(
        alias="reeferSupplyAirTemperatureMilliCZone3", default=None
    )
    """Supply or discharge air temperature of zone 2 of the reefer.

    This is the temperature of the air as it leaves the cooling unit.
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


class StatListResponse(BaseModel):
    data: List[Data]
    """List of trailers and their stats"""

    pagination: Pagination
    """Pagination parameters."""
