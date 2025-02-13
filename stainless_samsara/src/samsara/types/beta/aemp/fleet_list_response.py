# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "FleetListResponse",
    "Fleet",
    "FleetEquipment",
    "FleetEquipmentEquipmentHeader",
    "FleetEquipmentLocation",
    "FleetEquipmentCumulativeOperatingHours",
    "FleetEquipmentDefRemaining",
    "FleetEquipmentDistance",
    "FleetEquipmentEngineStatus",
    "FleetEquipmentFuelRemaining",
    "FleetLink",
]


class FleetEquipmentEquipmentHeader(BaseModel):
    equipment_id: Optional[str] = FieldInfo(alias="EquipmentID", default=None)
    """The unique Samsara ID of the equipment.

    This is automatically generated when the Equipment object is created. It cannot
    be changed.
    """

    model: Optional[str] = FieldInfo(alias="Model", default=None)
    """The model of the equipment."""

    oem_name: Optional[str] = FieldInfo(alias="OEMName", default=None)
    """The make of the equipment."""

    pin: Optional[str] = FieldInfo(alias="PIN", default=None)
    """The PIN number of the equipment."""

    serial_number: Optional[str] = FieldInfo(alias="SerialNumber", default=None)
    """The serial number of the equipment."""

    unit_install_date_time: Optional[str] = FieldInfo(alias="UnitInstallDateTime", default=None)
    """Telematics unit install date in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """


class FleetEquipmentLocation(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    latitude: Optional[float] = FieldInfo(alias="Latitude", default=None)
    """Location latitude."""

    longitude: Optional[float] = FieldInfo(alias="Longitude", default=None)
    """Location longitude."""


class FleetEquipmentCumulativeOperatingHours(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    hour: Optional[float] = FieldInfo(alias="Hour", default=None)
    """Total number of equipment operating hours."""


class FleetEquipmentDefRemaining(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    percent: Optional[float] = FieldInfo(alias="Percent", default=None)
    """Percent of DEF remaining in tank."""


class FleetEquipmentDistance(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    odometer: Optional[float] = FieldInfo(alias="Odometer", default=None)
    """Odometer value reported by equipment."""

    odometer_units: Optional[str] = FieldInfo(alias="OdometerUnits", default=None)
    """Unit of measurement for distance."""


class FleetEquipmentEngineStatus(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    running: Optional[bool] = FieldInfo(alias="Running", default=None)
    """Boolean value for whether engine is running or not."""


class FleetEquipmentFuelRemaining(BaseModel):
    datetime: Optional[str] = None
    """Date time in RFC 3339 format.

    Millisecond precision and timezones are supported. (Examples:
    2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    percent: Optional[float] = FieldInfo(alias="Percent", default=None)
    """Percent of fuel remaining in tank."""


class FleetEquipment(BaseModel):
    equipment_header: FleetEquipmentEquipmentHeader = FieldInfo(alias="EquipmentHeader")
    """Equipment header fields."""

    location: FleetEquipmentLocation = FieldInfo(alias="Location")
    """Equipment location."""

    cumulative_operating_hours: Optional[FleetEquipmentCumulativeOperatingHours] = FieldInfo(
        alias="CumulativeOperatingHours", default=None
    )
    """Equipment operating hours."""

    def_remaining: Optional[FleetEquipmentDefRemaining] = FieldInfo(alias="DEFRemaining", default=None)
    """DEF remaining in equipment."""

    distance: Optional[FleetEquipmentDistance] = FieldInfo(alias="Distance", default=None)
    """Equipment odometer distance."""

    engine_status: Optional[FleetEquipmentEngineStatus] = FieldInfo(alias="EngineStatus", default=None)
    """Equipment engine status."""

    fuel_remaining: Optional[FleetEquipmentFuelRemaining] = FieldInfo(alias="FuelRemaining", default=None)
    """Fuel remaining in equipment."""


class FleetLink(BaseModel):
    href: str
    """The hyperlink of the relationship."""

    rel: str
    """The link relationship to the current call."""


class Fleet(BaseModel):
    equipment: List[FleetEquipment] = FieldInfo(alias="Equipment")
    """The list of Equipment objects."""

    links: List[FleetLink] = FieldInfo(alias="Links")
    """The list of links associated with the current API request."""

    snapshot_time: str = FieldInfo(alias="snapshotTime")
    """
    Date and time at which the snapshot of the fleet was created in RFC 3339 format.
    """

    version: str
    """The version of the ISO/TS 15143-3 standard"""


class FleetListResponse(BaseModel):
    fleet: Fleet = FieldInfo(alias="Fleet")
    """Contains a list of equipment objects and links"""
