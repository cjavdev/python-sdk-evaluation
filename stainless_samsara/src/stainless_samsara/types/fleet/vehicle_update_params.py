# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VehicleUpdateParams", "Attribute", "GrossVehicleWeight"]


class VehicleUpdateParams(TypedDict, total=False):
    attributes: Iterable[Attribute]

    aux_input_type1: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType1"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type10: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType10"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type11: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType11"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type12: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType12"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type13: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType13"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type2: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType2"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type3: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType3"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type4: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType4"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type5: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType5"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type6: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType6"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type7: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType7"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type8: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType8"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    aux_input_type9: Annotated[
        Literal[
            "none",
            "emergencyLights",
            "emergencyAlarm",
            "stopPaddle",
            "powerTakeOff",
            "plow",
            "sweeper",
            "salter",
            "reefer",
            "door",
            "boom",
            "auxiliaryEngine",
            "generator",
            "eightWayLights",
            "panicButton",
            "privacyButton",
            "frontAxleDrive",
            "weightSensor",
            "other",
            "secondaryFuelSource",
            "ecuPowerTakeOff",
        ],
        PropertyInfo(alias="auxInputType9"),
    ]
    """
    The type of
    <a href="https://kb.samsara.com/hc/en-us/articles/360043040512-Auxiliary-Inputs" target="_blank">auxiliary
    input</a> configured for this Vehicle. Once configured, these inputs will
    generate dynamic, time-series data that will be available to view in the Samsara
    Dashboard. **By default**: empty. This can be set or updated through the Samsara
    Dashboard or the API at any time. Inputs 3-13 are only available on gateways
    with an attached aux expander. Valid values: `None`, `Emergency Lights`,
    `Emergency Alarm`, `Stop Paddle`, `Power Take-Off`, `Plow`, `Sweeper`, `Salter`,
    `Reefer`, `Door`, `Boom`, `Auxiliary Engine`, `Generator`, `Eight-Way Lights`,
    `Panic Button`, `Privacy Button`, `Front Axle Drive`, `Weight Sensor`, `Other`,
    `Secondary Fuel Source`, `(ECU) Power Take-Off`.
    """

    engine_hours: Annotated[int, PropertyInfo(alias="engineHours")]
    """A manual override for the vehicle's engine hours.

    You may only override a vehicle's engine hours if it cannot be read from
    on-board diagnostics. When you provide a manual engine hours override, Samsara
    will begin updating a vehicle's engine hours based on when the Samsara Vehicle
    Gateway is recieving power or not. Setting the value to 0 will unset the manual
    engine hours.
    """

    external_ids: Annotated[Dict[str, str], PropertyInfo(alias="externalIds")]
    """
    The <a href="/docs/external-ids" target="_blank">external IDs</a> for the given
    object.
    """

    gateway_serial: Annotated[str, PropertyInfo(alias="gatewaySerial")]
    """The serial number of the gateway.

    **By default**: empty. This can be set to a different gateway's serial number to
    pair this vehicle with a different gateway.
    """

    gross_vehicle_weight: Annotated[GrossVehicleWeight, PropertyInfo(alias="grossVehicleWeight")]
    """The gross weight of the vehicle in either pounds (lb) or kilograms (kg).

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    harsh_acceleration_setting_type: Annotated[
        Literal["passengerCar", "lightTruck", "heavyDuty", "off", "automatic"],
        PropertyInfo(alias="harshAccelerationSettingType"),
    ]
    """The harsh acceleration setting type.

    This setting influences the acceleration sensitivity from which a
    <a href="https://kb.samsara.com/hc/en-us/articles/360043051792-Safety-Event-Overview" target="_blank">harsh
    event</a> is triggered. **By default**, this setting is inferred by the Samsara
    Vehicle Gateway from the engine computer, but it may be set or updated through
    the Samsara Dashboard or the API at any time. If set to `off`, then no
    acceleration based harsh events are triggered for the vehicle. Valid values:
    `passengerCar`, `lightTruck`, `heavyDuty`, `off`, `automatic`.
    """

    license_plate: Annotated[str, PropertyInfo(alias="licensePlate")]
    """The license plate of the Vehicle.

    **By default**: empty. Can be set or updated through the Samsara Dashboard or
    the API at any time.
    """

    name: str
    """The human-readable name of the Vehicle.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. **By default**, this name is
    the serial number of the Samsara Vehicle Gateway. It can be set or updated
    through the Samsara Dashboard or through the API at any time.
    """

    notes: str
    """These are generic notes about the Vehicle.

    Empty by default. Can be set or updated through the Samsara Dashboard or the API
    at any time.
    """

    odometer_meters: Annotated[int, PropertyInfo(alias="odometerMeters")]
    """A manual override for the vehicle's odometer.

    You may only override a vehicle's odometer if it cannot be read from on-board
    diagnostics. When you provide a manual odometer override, Samsara will begin
    updating a vehicle's odometer using GPS distance traveled since this override
    was set. See
    <a href="https://kb.samsara.com/hc/en-us/articles/115005273667" target="_blank">here</a>
    for more details.
    """

    static_assigned_driver_id: Annotated[str, PropertyInfo(alias="staticAssignedDriverId")]
    """ID for the static assigned driver of the vehicle.

    Setting the value to 0 will unassign the current driver.
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """An array of IDs of tags to associate with this vehicle.

    If your access to the API is scoped by one or more tags, this field is required
    to pass in.
    """

    vehicle_regulation_mode: Annotated[
        Literal["regulated", "unregulated", "mixed"], PropertyInfo(alias="vehicleRegulationMode")
    ]
    """
    Whether or not the vehicle is regulated, unregulated (non-CMV), or a mixed use
    unregulated vehicle. Valid values: `regulated`, `unregulated`, `mixed`.
    """

    vehicle_type: Annotated[str, PropertyInfo(alias="vehicleType")]
    """The type of the vehicle.

    Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vin: str
    """The VIN of the Vehicle.

    Most of the time, this will be automatically read from the engine computer by
    the Samsara Vehicle Gateway. It will be empty if it cannot be read. It can be
    set or updated through the Samsara Dashboard or the API at any time.
    """


class Attribute(TypedDict, total=False):
    id: str
    """The samsara id of the attribute object."""

    name: str
    """Name of attribute."""

    number_values: Annotated[Iterable[float], PropertyInfo(alias="numberValues")]
    """Number values that are associated with this attribute."""

    string_values: Annotated[List[str], PropertyInfo(alias="stringValues")]
    """String values that are associated with this attribute."""


class GrossVehicleWeight(TypedDict, total=False):
    unit: Literal["lb", "kg"]
    """The unit of weight for the vehicle."""

    weight: int
    """The weight value of the vehicle."""
