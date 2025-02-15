# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AlertEventDvirTrailer(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the Trailer
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Trailer
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
