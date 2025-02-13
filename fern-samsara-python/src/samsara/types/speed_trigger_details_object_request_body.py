# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .speed_trigger_details_object_request_body_operation import SpeedTriggerDetailsObjectRequestBodyOperation
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class SpeedTriggerDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Speed
    """

    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    The number of milliseconds the trigger needs to stay active before alerting.
    """

    operation: SpeedTriggerDetailsObjectRequestBodyOperation = pydantic.Field()
    """
    How to evaluate the threshold.  Valid values: `GREATER`, `LESS`
    """

    speed_kilometers_per_hour: typing_extensions.Annotated[int, FieldMetadata(alias="speedKilometersPerHour")] = (
        pydantic.Field()
    )
    """
    The speed threshold value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
