# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GoaRouteTinyResponseResponseBody(UniversalBaseModel):
    """
    A minified representation of a single route.
    """

    external_ids: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]], FieldMetadata(alias="externalIds")
    ] = pydantic.Field(default=None)
    """
    A map of external ids
    """

    id: str = pydantic.Field()
    """
    Unique identifier for the route.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the route.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
