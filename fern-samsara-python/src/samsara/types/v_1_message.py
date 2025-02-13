# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class V1Message(UniversalBaseModel):
    driver_id: typing_extensions.Annotated[int, FieldMetadata(alias="driverId")] = pydantic.Field()
    """
    ID of the driver for whom the message is sent to or sent by.
    """

    text: str = pydantic.Field()
    """
    The text sent in the message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
