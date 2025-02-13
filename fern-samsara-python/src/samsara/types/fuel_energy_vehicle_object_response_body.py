# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .fuel_energy_vehicle_object_response_body_energy_type import FuelEnergyVehicleObjectResponseBodyEnergyType
from ..core.serialization import FieldMetadata
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FuelEnergyVehicleObjectResponseBody(UniversalBaseModel):
    """
    A minified vehicle object.
    """

    energy_type: typing_extensions.Annotated[
        FuelEnergyVehicleObjectResponseBodyEnergyType, FieldMetadata(alias="energyType")
    ] = pydantic.Field()
    """
    Type of energy used by the vehicle  Valid values: `fuel`, `hybrid`, `electric`
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the vehicle
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the vehicle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
