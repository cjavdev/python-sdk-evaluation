# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrailerStatReeferStateZone2TypeResponseBody(UniversalBaseModel):
    """
    Reefer state event.
    """

    substate_value: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="substateValue")] = (
        pydantic.Field(default=None)
    )
    """
    The substate zone 2 of the reefer, if available.
    """

    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format.
    """

    value: str = pydantic.Field()
    """
    The state zone 2 of the reefer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
