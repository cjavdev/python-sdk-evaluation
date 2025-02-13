# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateDriverRequestAttributes(UniversalBaseModel):
    """
    A minified attribute.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The samsara id of the attribute object.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of attribute.
    """

    number_values: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="numberValues")
    ] = pydantic.Field(default=None)
    """
    Number values that are associated with this attribute.
    """

    string_values: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="stringValues")
    ] = pydantic.Field(default=None)
    """
    String values that are associated with this attribute.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
