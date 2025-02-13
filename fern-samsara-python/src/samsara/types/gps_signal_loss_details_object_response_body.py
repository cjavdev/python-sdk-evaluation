# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class GpsSignalLossDetailsObjectResponseBody(UniversalBaseModel):
    """
    Details specific to GPS Signal Loss
    """

    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    The number of milliseconds the trigger needs to stay active before alerting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
