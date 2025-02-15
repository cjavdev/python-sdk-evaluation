# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FuelRemainingResponseBody(UniversalBaseModel):
    """
    Fuel remaining in equipment.
    """

    percent: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="Percent")] = pydantic.Field(
        default=None
    )
    """
    Percent of fuel remaining in tank.
    """

    datetime: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
