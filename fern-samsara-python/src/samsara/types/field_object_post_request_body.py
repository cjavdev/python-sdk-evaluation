# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .field_object_post_request_body_type import FieldObjectPostRequestBodyType
import typing
from .field_object_value_request_body import FieldObjectValueRequestBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FieldObjectPostRequestBody(UniversalBaseModel):
    label: str = pydantic.Field()
    """
    The name of the field.
    """

    type: FieldObjectPostRequestBodyType = pydantic.Field()
    """
    The type of field.  Valid values: `photo`, `string`, `number`, `multipleChoice`, `signature`, `dateTime`, `scannedDocument`, `barcode`
    """

    value: typing.Optional[FieldObjectValueRequestBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
