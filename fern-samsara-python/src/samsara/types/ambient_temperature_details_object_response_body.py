# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .ambient_temperature_details_object_response_body_operation import (
    AmbientTemperatureDetailsObjectResponseBodyOperation,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AmbientTemperatureDetailsObjectResponseBody(UniversalBaseModel):
    """
    Details specific to Ambient Temperature.
    """

    cargo_is_full: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="cargoIsFull")] = (
        pydantic.Field(default=None)
    )
    """
    Whether the cargo is full.
    """

    doors_are_closed: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="doorsAreClosed")] = (
        pydantic.Field(default=None)
    )
    """
    Whether the doors are closed.
    """

    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    The number of milliseconds the trigger needs to stay active before alerting.
    """

    operation: AmbientTemperatureDetailsObjectResponseBodyOperation = pydantic.Field()
    """
    How to evaluate the threshold.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    temperature_celcius: typing_extensions.Annotated[int, FieldMetadata(alias="temperatureCelcius")] = pydantic.Field()
    """
    The temperature in Celcius threshold value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
