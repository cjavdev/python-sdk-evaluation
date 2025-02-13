# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "VehiclesListVehiclesResponseBody",
    "Data",
    "DataAttribute",
    "DataGateway",
    "DataSensorConfiguration",
    "DataSensorConfigurationArea",
    "DataSensorConfigurationAreaCargoSensor",
    "DataSensorConfigurationAreaHumiditySensor",
    "DataSensorConfigurationAreaTemperatureSensor",
    "DataSensorConfigurationDoor",
    "DataSensorConfigurationDoorSensor",
    "DataStaticAssignedDriver",
    "DataTag",
    "Pagination",
]


class DataAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataGateway(BaseModel):
    model: Literal[
        "AG15",
        "AG24",
        "AG24EU",
        "AG26",
        "AG26EU",
        "AG41",
        "AG41EU",
        "AG45",
        "AG45EU",
        "AG46",
        "AG46EU",
        "AG46P",
        "AG46PEU",
        "AG51",
        "AG51EU",
        "AG52",
        "AG52EU",
        "AG53",
        "AG53EU",
        "IG15",
        "IG21",
        "IG41",
        "IG61",
        "SG1",
        "SG1B",
        "SG1G",
        "SG1G32",
        "SG1x",
        "VG32",
        "VG33",
        "VG34",
        "VG34EU",
        "VG34FN",
        "VG34M",
        "VG54ATT",
        "VG54EU",
        "VG54FN",
        "VG54NA",
        "VG54NAE",
        "VG54NAH",
        "VG55EU",
        "VG55FN",
        "VG55NA",
    ]
    """The model of the gateway installed on the asset.

    Valid values: `AG15`, `AG24`, `AG24EU`, `AG26`, `AG26EU`, `AG41`, `AG41EU`,
    `AG45`, `AG45EU`, `AG46`, `AG46EU`, `AG46P`, `AG46PEU`, `AG51`, `AG51EU`,
    `AG52`, `AG52EU`, `AG53`, `AG53EU`, `IG15`, `IG21`, `IG41`, `IG61`, `SG1`,
    `SG1B`, `SG1G`, `SG1G32`, `SG1x`, `VG32`, `VG33`, `VG34`, `VG34EU`, `VG34FN`,
    `VG34M`, `VG54ATT`, `VG54EU`, `VG54FN`, `VG54NA`, `VG54NAE`, `VG54NAH`,
    `VG55EU`, `VG55FN`, `VG55NA`
    """

    serial: str
    """The serial number of the gateway installed on the asset."""


class DataSensorConfigurationAreaCargoSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """The MAC address of the sensor"""

    name: str
    """The name of the sensor"""


class DataSensorConfigurationAreaHumiditySensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """The MAC address of the sensor"""

    name: str
    """The name of the sensor"""


class DataSensorConfigurationAreaTemperatureSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """The MAC address of the sensor"""

    name: str
    """The name of the sensor"""


class DataSensorConfigurationArea(BaseModel):
    position: Literal["back", "front", "middle"]
    """Position of the area on vehicle Valid values: `back`, `front`, `middle`"""

    cargo_sensors: Optional[List[DataSensorConfigurationAreaCargoSensor]] = FieldInfo(
        alias="cargoSensors", default=None
    )

    humidity_sensors: Optional[List[DataSensorConfigurationAreaHumiditySensor]] = FieldInfo(
        alias="humiditySensors", default=None
    )

    temperature_sensors: Optional[List[DataSensorConfigurationAreaTemperatureSensor]] = FieldInfo(
        alias="temperatureSensors", default=None
    )


class DataSensorConfigurationDoorSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """The MAC address of the sensor"""

    name: str
    """The name of the sensor"""


class DataSensorConfigurationDoor(BaseModel):
    position: Literal["back", "left", "right"]
    """
    Position of the door monitor on the vehicle Valid values: `back`, `left`,
    `right`
    """

    sensor: DataSensorConfigurationDoorSensor
    """A sensor"""


class DataSensorConfiguration(BaseModel):
    areas: Optional[List[DataSensorConfigurationArea]] = None
    """Configured sensor areas on the vehicle with its associated sensors"""

    doors: Optional[List[DataSensorConfigurationDoor]] = None
    """Configured door monitors on the vehicle"""


class DataStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """ID of the vehicle"""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time the vehicle was created in RFC 3339 format."""

    attributes: Optional[List[DataAttribute]] = None
    """List of attributes associated with the entity"""

    aux_input_type1: Optional[str] = FieldInfo(alias="auxInputType1", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type10: Optional[str] = FieldInfo(alias="auxInputType10", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type11: Optional[str] = FieldInfo(alias="auxInputType11", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type12: Optional[str] = FieldInfo(alias="auxInputType12", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type13: Optional[str] = FieldInfo(alias="auxInputType13", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type2: Optional[str] = FieldInfo(alias="auxInputType2", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type3: Optional[str] = FieldInfo(alias="auxInputType3", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type4: Optional[str] = FieldInfo(alias="auxInputType4", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type5: Optional[str] = FieldInfo(alias="auxInputType5", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type6: Optional[str] = FieldInfo(alias="auxInputType6", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type7: Optional[str] = FieldInfo(alias="auxInputType7", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type8: Optional[str] = FieldInfo(alias="auxInputType8", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    aux_input_type9: Optional[str] = FieldInfo(alias="auxInputType9", default=None)
    """The type of auxiliary input configured for this Vehicle."""

    camera_serial: Optional[str] = FieldInfo(alias="cameraSerial", default=None)
    """The serial number of the camera installed in the vehicle"""

    esn: Optional[str] = None
    """Engine serial number."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    gateway: Optional[DataGateway] = None
    """A minified gateway object"""

    harsh_acceleration_setting_type: Optional[str] = FieldInfo(alias="harshAccelerationSettingType", default=None)
    """The harsh acceleration setting type."""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the vehicle."""

    make: Optional[str] = None
    """The Vehicle’s manufacturing make."""

    model: Optional[str] = None
    """The Vehicle’s manufacturing model."""

    name: Optional[str] = None
    """Name of the vehicle"""

    notes: Optional[str] = None
    """These are generic notes about the Vehicle."""

    sensor_configuration: Optional[DataSensorConfiguration] = FieldInfo(alias="sensorConfiguration", default=None)
    """The sensors configured on a vehicle"""

    serial: Optional[str] = None
    """The serial number of the gateway installed in the vehicle."""

    static_assigned_driver: Optional[DataStaticAssignedDriver] = FieldInfo(alias="staticAssignedDriver", default=None)
    """Current driver of the vehicle.

    Note: this parameter includes all assignment sources, not just static
    assignments.
    """

    tags: Optional[List[DataTag]] = None
    """The list of tags associated with the Vehicle."""

    updated_at_time: Optional[datetime] = FieldInfo(alias="updatedAtTime", default=None)
    """Time the vehicle was updated in RFC 3339 format."""

    vehicle_regulation_mode: Optional[Literal["regulated", "unregulated"]] = FieldInfo(
        alias="vehicleRegulationMode", default=None
    )
    """Whether the vehicle is regulated or unregulated (non-CMV).

    Valid values: `regulated`, `unregulated`
    """

    vehicle_type: Optional[Literal["unset", "passenger", "truck", "bus"]] = FieldInfo(alias="vehicleType", default=None)
    """The type of the vehicle.

    Only returned for customers with commercial speed limits (CSL) enabled. Valid
    values: `unset`, `passenger`, `truck`, `bus`
    """

    vehicle_weight: Optional[int] = FieldInfo(alias="vehicleWeight", default=None)
    """The weight of the vehicle in either pounds (lb) or kilograms (kg).

    Unit of weight is unknown. Only returned for customers with commercial speed
    limits (CSL) enabled.
    """

    vehicle_weight_in_kilograms: Optional[int] = FieldInfo(alias="vehicleWeightInKilograms", default=None)
    """The weight of the vehicle in kilograms (kg).

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vehicle_weight_in_pounds: Optional[int] = FieldInfo(alias="vehicleWeightInPounds", default=None)
    """The weight of the vehicle in pounds (lb).

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vin: Optional[str] = None
    """The VIN of the vehicle."""

    year: Optional[str] = None


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


class VehiclesListVehiclesResponseBody(BaseModel):
    data: List[Data]
    """Multiple vehicles."""

    pagination: Pagination
    """Pagination parameters."""
