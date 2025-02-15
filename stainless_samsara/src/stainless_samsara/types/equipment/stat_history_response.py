# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "StatHistoryResponse",
    "Data",
    "DataEngineRpm",
    "DataEngineSecond",
    "DataEngineState",
    "DataFuelPercent",
    "DataGatewayEngineSecond",
    "DataGatewayEngineState",
    "DataGatewayJ1939EngineSecond",
    "DataGp",
    "DataGpAddress",
    "DataGpReverseGeo",
    "DataGpsOdometerMeter",
    "DataObdEngineSecond",
    "DataObdEngineState",
    "Pagination",
]


class DataEngineRpm(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """The revolutions per minute of the engine."""


class DataEngineSecond(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """
    An approximation of the number of seconds the engine has been running since it
    was new, based on the amount of time the AG26 device is receiving power and an
    offset provided manually through the Samsara cloud dashboard.
    """


class DataEngineState(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: Literal["Off", "On"]
    """
    An approximation of engine state based on readings the AG26 receives from the
    aux/digio cable. Valid values: `Off`, `On`.
    """


class DataFuelPercent(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """The percent of fuel in the unit of equipment."""


class DataGatewayEngineSecond(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """
    An approximation of the number of seconds the engine has been running since it
    was new, based on the amount of time the AG26 device is receiving power and an
    offset provided manually through the Samsara cloud dashboard.
    """


class DataGatewayEngineState(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: Literal["Off", "On"]
    """
    An approximation of engine state based on readings the AG26 receives from the
    aux/digio cable. Valid values: `Off`, `On`.
    """


class DataGatewayJ1939EngineSecond(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """
    An approximation of the number of seconds the engine has been running since it
    was new, based on the amount of time the AG26 device is receiving power and an
    offset provided manually through the Samsara cloud dashboard.
    """


class DataGpAddress(BaseModel):
    id: Optional[str] = None
    """Address book identifier"""

    name: Optional[str] = None
    """Name of this address book entry"""


class DataGpReverseGeo(BaseModel):
    formatted_location: Optional[str] = FieldInfo(alias="formattedLocation", default=None)
    """Formatted address of the reverse geocoding data."""


class DataGp(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""

    time: str
    """UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    address: Optional[DataGpAddress] = None
    """Address book entry, if one exists"""

    heading_degrees: Optional[float] = FieldInfo(alias="headingDegrees", default=None)
    """Heading of the asset in degrees."""

    reverse_geo: Optional[DataGpReverseGeo] = FieldInfo(alias="reverseGeo", default=None)
    """Reverse geocoded information."""

    speed_miles_per_hour: Optional[float] = FieldInfo(alias="speedMilesPerHour", default=None)
    """GPS speed of the asset in miles per hour."""


class DataGpsOdometerMeter(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """
    An approximation of odometer reading based on GPS calculations since the AG26
    was activated, and a manual odometer offset provided in the Samsara cloud
    dashboard.
    """


class DataObdEngineSecond(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: int
    """The number of seconds the engine has been running since it was new.

    This value is provided directly from on-board diagnostics.
    """


class DataObdEngineState(BaseModel):
    time: str
    """
    UTC timestamp of the time the data point was generated by the equipment, in
    RFC3339 format.
    """

    value: Literal["Off", "On", "Idle"]
    """The state of the engine read from on-board diagnostics.

    Valid values: `Off`, `On`, `Idle`.
    """


class Data(BaseModel):
    id: str
    """Unique Samsara ID for the equipment."""

    name: str
    """Name of the equipment."""

    engine_rpm: Optional[List[DataEngineRpm]] = FieldInfo(alias="engineRpm", default=None)
    """A time-series of engine RPM readings for the given unit of equipment."""

    engine_seconds: Optional[List[DataEngineSecond]] = FieldInfo(alias="engineSeconds", default=None)
    """
    [DEPRECATED] Please use either `gatewayEngineSeconds`, `obdEngineSeconds`, or
    `gatewayJ1939EngineSeconds`.
    """

    engine_states: Optional[List[DataEngineState]] = FieldInfo(alias="engineStates", default=None)
    """[DEPRECATED] Please use either `gatewayEngineStates` or `obdEngineStates`."""

    fuel_percents: Optional[List[DataFuelPercent]] = FieldInfo(alias="fuelPercents", default=None)
    """A time-series of fuel percent level changes for the given unit of equipment."""

    gateway_engine_seconds: Optional[List[DataGatewayEngineSecond]] = FieldInfo(
        alias="gatewayEngineSeconds", default=None
    )
    """
    A time-series of engine seconds readings for the given unit of equipment as an
    approximate based on readings from the AG26's aux/digio cable.
    """

    gateway_engine_states: Optional[List[DataGatewayEngineState]] = FieldInfo(alias="gatewayEngineStates", default=None)
    """
    A time-series of engine state changes (as read from the AG26's aux/digio cable)
    for the given unit of equipment.
    """

    gateway_j1939_engine_seconds: Optional[List[DataGatewayJ1939EngineSecond]] = FieldInfo(
        alias="gatewayJ1939EngineSeconds", default=None
    )
    """
    A time-series of engine seconds readings for the given unit of equipment as an
    approximate based on readings from the AG26's CAT/J1939 cable.
    """

    gps: Optional[List[DataGp]] = None
    """A time-series of GPS locations."""

    gps_odometer_meters: Optional[List[DataGpsOdometerMeter]] = FieldInfo(alias="gpsOdometerMeters", default=None)
    """A time-series of GPS odometer readings for the given unit of equipment."""

    obd_engine_seconds: Optional[List[DataObdEngineSecond]] = FieldInfo(alias="obdEngineSeconds", default=None)
    """
    A time-series of engine seconds readings for the given unit of equipment
    directly from on-board diagnostics.
    """

    obd_engine_states: Optional[List[DataObdEngineState]] = FieldInfo(alias="obdEngineStates", default=None)
    """
    A time-series of engine state changes (as read from on-board diagnostics) for
    the given unit of equipment.
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


class StatHistoryResponse(BaseModel):
    data: List[Data]
    """Time-series of stats for the specified units of equipment and stat types."""

    pagination: Pagination
    """Pagination parameters."""
