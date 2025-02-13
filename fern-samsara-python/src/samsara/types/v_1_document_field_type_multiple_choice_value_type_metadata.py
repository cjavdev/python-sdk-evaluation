# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .v_1_document_field_type_multiple_choice_value_type_metadata_multiple_choice_option_labels import (
    V1DocumentFieldTypeMultipleChoiceValueTypeMetadataMultipleChoiceOptionLabels,
)
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1DocumentFieldTypeMultipleChoiceValueTypeMetadata(UniversalBaseModel):
    """
    Metadata about the multiple choice field. Only present for value type `ValueType_MultipleChoice`
    """

    multiple_choice_option_labels: typing_extensions.Annotated[
        typing.Optional[typing.List[V1DocumentFieldTypeMultipleChoiceValueTypeMetadataMultipleChoiceOptionLabels]],
        FieldMetadata(alias="multipleChoiceOptionLabels"),
    ] = pydantic.Field(default=None)
    """
    Array of the multiple choice option labels for the field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
