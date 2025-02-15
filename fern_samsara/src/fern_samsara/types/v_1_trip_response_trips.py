# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .v_1_trip_response_end_address import V1TripResponseEndAddress
from .v_1_trip_response_end_coordinates import V1TripResponseEndCoordinates
from .v_1_trip_response_start_address import V1TripResponseStartAddress
from .v_1_trip_response_start_coordinates import V1TripResponseStartCoordinates
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1TripResponseTrips(UniversalBaseModel):
    asset_ids: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="assetIds")] = (
        pydantic.Field(default=None)
    )
    """
    List of associated asset IDs
    """

    codriver_ids: typing_extensions.Annotated[typing.Optional[typing.List[int]], FieldMetadata(alias="codriverIds")] = (
        pydantic.Field(default=None)
    )
    """
    List of codriver IDs
    """

    distance_meters: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="distanceMeters")] = (
        pydantic.Field(default=None)
    )
    """
    Length of the trip in meters. This value is calculated from the GPS data collected by the Samsara Vehicle Gateway.
    """

    driver_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="driverId")] = pydantic.Field(
        default=None
    )
    """
    ID of the driver.
    """

    end_address: typing_extensions.Annotated[
        typing.Optional[V1TripResponseEndAddress], FieldMetadata(alias="endAddress")
    ] = None
    end_coordinates: typing_extensions.Annotated[
        typing.Optional[V1TripResponseEndCoordinates], FieldMetadata(alias="endCoordinates")
    ] = None
    end_location: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="endLocation")] = (
        pydantic.Field(default=None)
    )
    """
    Geocoded street address of start (latitude, longitude) coordinates.
    """

    end_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="endMs")] = pydantic.Field(
        default=None
    )
    """
    End of the trip in UNIX milliseconds. Ongoing trips are indicated by an endMs value of 9223372036854775807.
    """

    end_odometer: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="endOdometer")] = (
        pydantic.Field(default=None)
    )
    """
    Odometer reading (in meters) at the end of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.
    """

    fuel_consumed_ml: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="fuelConsumedMl")] = (
        pydantic.Field(default=None)
    )
    """
    Amount in milliliters of fuel consumed on this trip.
    """

    start_address: typing_extensions.Annotated[
        typing.Optional[V1TripResponseStartAddress], FieldMetadata(alias="startAddress")
    ] = None
    start_coordinates: typing_extensions.Annotated[
        typing.Optional[V1TripResponseStartCoordinates], FieldMetadata(alias="startCoordinates")
    ] = None
    start_location: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="startLocation")] = (
        pydantic.Field(default=None)
    )
    """
    Geocoded street address of start (latitude, longitude) coordinates.
    """

    start_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="startMs")] = pydantic.Field(
        default=None
    )
    """
    Beginning of the trip in UNIX milliseconds.
    """

    start_odometer: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="startOdometer")] = (
        pydantic.Field(default=None)
    )
    """
    Odometer reading (in meters) at the beginning of the trip. This is read from the vehicle's on-board diagnostics. If Samsara cannot read the vehicle's odometer values from on-board diagnostics, this value will be 0.
    """

    toll_meters: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="tollMeters")] = pydantic.Field(
        default=None
    )
    """
    Length in meters trip spent on toll roads.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
