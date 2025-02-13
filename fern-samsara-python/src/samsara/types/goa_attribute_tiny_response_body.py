# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GoaAttributeTinyResponseBody(UniversalBaseModel):
    """
    Attribute properties.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of the attribute
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the attribute
    """

    number_values: typing_extensions.Annotated[
        typing.Optional[typing.List[float]], FieldMetadata(alias="numberValues")
    ] = pydantic.Field(default=None)
    """
    List of number values associated with the attribute
    """

    string_values: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="stringValues")
    ] = pydantic.Field(default=None)
    """
    List of string values associated with the attribute.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
