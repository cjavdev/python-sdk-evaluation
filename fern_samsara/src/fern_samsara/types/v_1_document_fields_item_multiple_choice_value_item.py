# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1DocumentFieldsItemMultipleChoiceValueItem(UniversalBaseModel):
    selected: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean representing if the choice has been selected.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the choice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
