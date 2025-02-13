# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .trailer_stat_decoration_response_body import TrailerStatDecorationResponseBody
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrailerStatReeferStateZone1WithDecorationsTypeResponseBody(UniversalBaseModel):
    """
    Reefer state event.
    """

    decorations: typing.Optional[TrailerStatDecorationResponseBody] = None
    substate_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="substateValue")] = (
        pydantic.Field(default=None)
    )
    """
    The substate zone 1 of the reefer, if available.
    """

    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format.
    """

    value: str = pydantic.Field()
    """
    The state zone 1 of the reefer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
