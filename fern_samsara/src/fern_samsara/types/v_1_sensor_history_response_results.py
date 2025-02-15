# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1SensorHistoryResponseResults(UniversalBaseModel):
    series: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    List of datapoints, one for each requested (sensor, field) pair.
    """

    time_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="timeMs")] = pydantic.Field(
        default=None
    )
    """
    Timestamp in UNIX milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
