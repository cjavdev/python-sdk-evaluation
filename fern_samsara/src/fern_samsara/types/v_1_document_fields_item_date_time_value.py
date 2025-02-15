# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1DocumentFieldsItemDateTimeValue(UniversalBaseModel):
    """
    The value of a date time field. Only present for date time fields.
    """

    date_time_ms: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="dateTimeMs")] = (
        pydantic.Field(default=None)
    )
    """
    Date time value in milliseconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
