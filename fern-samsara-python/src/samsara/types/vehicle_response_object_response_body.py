# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .goa_attribute_tiny_response_body import GoaAttributeTinyResponseBody
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from .goa_gateway_tiny_response_response_body import GoaGatewayTinyResponseResponseBody
from .vehicle_sensor_configuration_response_body import VehicleSensorConfigurationResponseBody
from .driver_object_response_body import DriverObjectResponseBody
from .goa_tag_tiny_response_response_body import GoaTagTinyResponseResponseBody
from .vehicle_response_object_response_body_vehicle_regulation_mode import (
    VehicleResponseObjectResponseBodyVehicleRegulationMode,
)
from .vehicle_response_object_response_body_vehicle_type import VehicleResponseObjectResponseBodyVehicleType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehicleResponseObjectResponseBody(UniversalBaseModel):
    """
    A single vehicle
    """

    attributes: typing.Optional[typing.List[GoaAttributeTinyResponseBody]] = pydantic.Field(default=None)
    """
    List of attributes associated with the entity
    """

    aux_input_type_1: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType1")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_10: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType10")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_11: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType11")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_12: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType12")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_13: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType13")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_2: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType2")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_3: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType3")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_4: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType4")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_5: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType5")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_6: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType6")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_7: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType7")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_8: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType8")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    aux_input_type_9: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="auxInputType9")] = (
        pydantic.Field(default=None)
    )
    """
    The type of auxiliary input configured for this Vehicle.
    """

    camera_serial: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="cameraSerial")] = (
        pydantic.Field(default=None)
    )
    """
    The serial number of the camera installed in the vehicle
    """

    created_at_time: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAtTime")] = pydantic.Field()
    """
    Time the vehicle was created in RFC 3339 format.
    """

    esn: typing.Optional[str] = pydantic.Field(default=None)
    """
    Engine serial number.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    gateway: typing.Optional[GoaGatewayTinyResponseResponseBody] = None
    harsh_acceleration_setting_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="harshAccelerationSettingType")
    ] = pydantic.Field(default=None)
    """
    The harsh acceleration setting type.
    """

    id: str = pydantic.Field()
    """
    ID of the vehicle
    """

    license_plate: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="licensePlate")] = (
        pydantic.Field(default=None)
    )
    """
    The license plate of the vehicle.
    """

    make: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Vehicle’s manufacturing make.
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Vehicle’s manufacturing model.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the vehicle
    """

    notes: typing.Optional[str] = pydantic.Field(default=None)
    """
    These are generic notes about the Vehicle.
    """

    sensor_configuration: typing_extensions.Annotated[
        typing.Optional[VehicleSensorConfigurationResponseBody], FieldMetadata(alias="sensorConfiguration")
    ] = None
    serial: typing.Optional[str] = pydantic.Field(default=None)
    """
    The serial number of the gateway installed in the vehicle.
    """

    static_assigned_driver: typing_extensions.Annotated[
        typing.Optional[DriverObjectResponseBody], FieldMetadata(alias="staticAssignedDriver")
    ] = None
    tags: typing.Optional[typing.List[GoaTagTinyResponseResponseBody]] = pydantic.Field(default=None)
    """
    The list of tags associated with the Vehicle.
    """

    updated_at_time: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updatedAtTime")] = (
        pydantic.Field(default=None)
    )
    """
    Time the vehicle was updated in RFC 3339 format.
    """

    vehicle_regulation_mode: typing_extensions.Annotated[
        typing.Optional[VehicleResponseObjectResponseBodyVehicleRegulationMode],
        FieldMetadata(alias="vehicleRegulationMode"),
    ] = pydantic.Field(default=None)
    """
    Whether the vehicle is regulated or unregulated (non-CMV).  Valid values: `regulated`, `unregulated`
    """

    vehicle_type: typing_extensions.Annotated[
        typing.Optional[VehicleResponseObjectResponseBodyVehicleType], FieldMetadata(alias="vehicleType")
    ] = pydantic.Field(default=None)
    """
    The type of the vehicle. Only returned for customers with commercial speed limits (CSL) enabled.  Valid values: `unset`, `passenger`, `truck`, `bus`
    """

    vehicle_weight: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vehicleWeight")] = (
        pydantic.Field(default=None)
    )
    """
    The weight of the vehicle in either pounds (lb) or kilograms (kg). Unit of weight is unknown. Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vehicle_weight_in_kilograms: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="vehicleWeightInKilograms")
    ] = pydantic.Field(default=None)
    """
    The weight of the vehicle in kilograms (kg). Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vehicle_weight_in_pounds: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="vehicleWeightInPounds")
    ] = pydantic.Field(default=None)
    """
    The weight of the vehicle in pounds (lb). Only returned for customers with commercial speed limits (CSL) enabled.
    """

    vin: typing.Optional[str] = pydantic.Field(default=None)
    """
    The VIN of the vehicle.
    """

    year: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
