# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .vehicle_batter_voltage_details_object_request_body_operation import (
    VehicleBatterVoltageDetailsObjectRequestBodyOperation,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class VehicleBatterVoltageDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Vehicle Battery Voltage
    """

    battery_volts: typing_extensions.Annotated[int, FieldMetadata(alias="batteryVolts")] = pydantic.Field()
    """
    The battery volt threshold value.
    """

    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    The number of milliseconds the trigger needs to stay active before alerting.
    """

    operation: VehicleBatterVoltageDetailsObjectRequestBodyOperation = pydantic.Field()
    """
    How to evaluate the threshold.  Valid values: `GREATER`, `LESS`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
