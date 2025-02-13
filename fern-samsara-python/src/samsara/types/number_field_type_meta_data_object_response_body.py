# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class NumberFieldTypeMetaDataObjectResponseBody(UniversalBaseModel):
    """
    The number field metadata.
    """

    number_of_decimal_places: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="numberOfDecimalPlaces")
    ] = pydantic.Field(default=None)
    """
    The number of decimal places allowed for the field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
