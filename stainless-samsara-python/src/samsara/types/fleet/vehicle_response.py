# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "VehicleResponse",
    "Data",
    "DataAttribute",
    "DataGateway",
    "DataGrossVehicleWeight",
    "DataSensorConfiguration",
    "DataSensorConfigurationArea",
    "DataSensorConfigurationAreaCargoSensor",
    "DataSensorConfigurationAreaHumiditySensor",
    "DataSensorConfigurationAreaTemperatureSensor",
    "DataSensorConfigurationDoor",
    "DataSensorConfigurationDoorSensor",
    "DataStaticAssignedDriver",
    "DataTag",
]


class DataAttribute(BaseModel):
    id: Optional[str] = None
    """The samsara id of the attribute object."""

    name: Optional[str] = None
    """Name of attribute."""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """Number values that are associated with this attribute."""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """String values that are associated with this attribute."""


class DataGateway(BaseModel):
    model: Optional[str] = None
    """The gateway model"""

    serial: Optional[str] = None
    """The serial number of the gateway."""


class DataGrossVehicleWeight(BaseModel):
    unit: Optional[Literal["lb", "kg"]] = None
    """The unit of weight for the vehicle."""

    weight: Optional[int] = None
    """The weight value of the vehicle."""


class DataSensorConfigurationAreaCargoSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """MAC address of the sensor"""

    name: str
    """Name of the sensor"""


class DataSensorConfigurationAreaHumiditySensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """MAC address of the sensor"""

    name: str
    """Name of the sensor"""


class DataSensorConfigurationAreaTemperatureSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """MAC address of the sensor"""

    name: str
    """Name of the sensor"""


class DataSensorConfigurationArea(BaseModel):
    cargo_sensors: Optional[List[DataSensorConfigurationAreaCargoSensor]] = FieldInfo(
        alias="cargoSensors", default=None
    )
    """Cargo sensors configured in this position of the vehicle"""

    humidity_sensors: Optional[List[DataSensorConfigurationAreaHumiditySensor]] = FieldInfo(
        alias="humiditySensors", default=None
    )
    """Humidity sensors configured in this position of the vehicle"""

    position: Optional[Literal["Position_Front", "Position_Middle", "Position_Back"]] = None
    """Position of the area on vehicle"""

    temperature_sensors: Optional[List[DataSensorConfigurationAreaTemperatureSensor]] = FieldInfo(
        alias="temperatureSensors", default=None
    )
    """Temperature sensors configured in this position of the vehicle"""


class DataSensorConfigurationDoorSensor(BaseModel):
    id: str
    """ID of the sensor"""

    mac: str
    """MAC address of the sensor"""

    name: str
    """Name of the sensor"""


class DataSensorConfigurationDoor(BaseModel):
    position: Optional[Literal["Position_Left", "Position_Right"]] = None
    """Position of the door monitor on the vehicle"""

    sensor: Optional[DataSensorConfigurationDoorSensor] = None


class DataSensorConfiguration(BaseModel):
    areas: Optional[List[DataSensorConfigurationArea]] = None

    doors: Optional[List[DataSensorConfigurationDoor]] = None


class DataStaticAssignedDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """The unique Samsara ID of the Vehicle.

    This is automatically generated when the Vehicle object is created. It cannot be
    changed.
    """

    attributes: Optional[List[DataAttribute]] = None
    """A minified attribute"""

    aux_input_type1: Optional[str] = FieldInfo(alias="auxInputType1", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type10: Optional[str] = FieldInfo(alias="auxInputType10", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type11: Optional[str] = FieldInfo(alias="auxInputType11", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type12: Optional[str] = FieldInfo(alias="auxInputType12", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type13: Optional[str] = FieldInfo(alias="auxInputType13", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type2: Optional[str] = FieldInfo(alias="auxInputType2", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type3: Optional[str] = FieldInfo(alias="auxInputType3", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type4: Optional[str] = FieldInfo(alias="auxInputType4", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type5: Optional[str] = FieldInfo(alias="auxInputType5", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type6: Optional[str] = FieldInfo(alias="auxInputType6", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type7: Optional[str] = FieldInfo(alias="auxInputType7", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type8: Optional[str] = FieldInfo(alias="auxInputType8", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    aux_input_type9: Optional[str] = FieldInfo(alias="auxInputType9", default=None)
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. The value returned will match what is configured
    in the dashboard per vehicle.
    """

    camera_serial: Optional[str] = FieldInfo(alias="cameraSerial", default=None)
    """The serial number of the camera installed in the vehicle"""

    esn: Optional[str] = None
    """Engine serial number."""

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given
    object.
    """

    gateway: Optional[DataGateway] = None
    """A minified gateway including serial number and model."""

    gross_vehicle_weight: Optional[DataGrossVehicleWeight] = FieldInfo(alias="grossVehicleWeight", default=None)
    """The gross weight of the vehicle in either pounds (lb) or kilograms (kg).

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    harsh_acceleration_setting_type: Optional[
        Literal["passengerCar", "lightTruck", "heavyDuty", "off", "automatic"]
    ] = FieldInfo(alias="harshAccelerationSettingType", default=None)
    """The harsh acceleration setting type.

    This setting influences the acceleration sensitivity from which a
    <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh
    event</a> is triggered. **By default**, this setting is inferred by the Samsara
    Vehicle Gateway from the engine computer, but it may be set or updated through
    the Samsara Dashboard or the API at any time. If set to `off`, then no
    acceleration based harsh events are triggered for the vehicle. Valid values:
    `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.
    """

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the Vehicle.

    **By default**: empty. Can be set or updated through the Samsara Dashboard or
    the API at any time.
    """

    make: Optional[str] = None
    """The Vehicle’s manufacturing make.

    Automatically read from the engine computer if available. Empty if not
    available. Cannot be manually set.
    """

    model: Optional[str] = None
    """The Vehicle’s manufacturing model.

    Automatically read from the engine computer if available. Empty if not
    available. Cannot be manually set.
    """

    name: Optional[str] = None
    """The human-readable name of the Vehicle.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. **By default**, this name is
    the serial number of the Samsara Vehicle Gateway. It can be set or updated
    through the Samsara Dashboard or through the API at any time.
    """

    notes: Optional[str] = None
    """These are generic notes about the Vehicle.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    sensor_configuration: Optional[DataSensorConfiguration] = FieldInfo(alias="sensorConfiguration", default=None)
    """The sensors configured on a vehicle"""

    serial: Optional[str] = None
    """The serial number of the gateway installed in the vehicle."""

    static_assigned_driver: Optional[DataStaticAssignedDriver] = FieldInfo(alias="staticAssignedDriver", default=None)
    """A minified driver object."""

    tags: Optional[List[DataTag]] = None
    """
    The list of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043275091-Creating-and-Using-Tags" target="_blank">tags</a>
    associated with the Vehicle. **By default**: empty. Can be set or updated
    through the Samsara Dashboard or the API at any time.
    """

    vehicle_regulation_mode: Optional[Literal["regulated", "unregulated", "mixed"]] = FieldInfo(
        alias="vehicleRegulationMode", default=None
    )
    """
    Whether or not the vehicle is regulated, unregulated (non-CMV), or a mixed use
    unregulated vehicle. Valid values: `regulated`, `unregulated`, `mixed`.
    """

    vehicle_type: Optional[str] = FieldInfo(alias="vehicleType", default=None)
    """The type of the vehicle.

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vin: Optional[str] = None
    """The VIN of the Vehicle.

    Most of the time, this will be automatically read from the engine computer by
    the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be
    set or updated through the Samsara Dashboard or the API at any time.
    """

    year: Optional[str] = None
    """Year of the Vehicle."""


class VehicleResponse(BaseModel):
    data: Data
    """The vehicle object."""
