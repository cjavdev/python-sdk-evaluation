# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .vehicle_stats_fault_codes_value_j_1939 import VehicleStatsFaultCodesValueJ1939
from .vehicle_stats_fault_codes_value_obdii import VehicleStatsFaultCodesValueObdii
from .vehicle_stats_fault_codes_value_oem import VehicleStatsFaultCodesValueOem
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehicleStatsFaultCodesValue(UniversalBaseModel):
    """
    Fault codes for the vehicle
    """

    can_bus_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="canBusType")] = pydantic.Field(
        default=None
    )
    """
    The CAN bus type of the vehicle.
    """

    j_1939: typing_extensions.Annotated[
        typing.Optional[VehicleStatsFaultCodesValueJ1939], FieldMetadata(alias="j1939")
    ] = None
    obdii: typing.Optional[VehicleStatsFaultCodesValueObdii] = None
    oem: typing.Optional[VehicleStatsFaultCodesValueOem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
