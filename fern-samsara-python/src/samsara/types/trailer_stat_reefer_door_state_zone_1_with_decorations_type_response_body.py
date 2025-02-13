# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .trailer_stat_decoration_response_body import TrailerStatDecorationResponseBody
import pydantic
from .trailer_stat_reefer_door_state_zone_1_with_decorations_type_response_body_value import (
    TrailerStatReeferDoorStateZone1WithDecorationsTypeResponseBodyValue,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TrailerStatReeferDoorStateZone1WithDecorationsTypeResponseBody(UniversalBaseModel):
    """
    Door stats that have been emitted by the reefer.
    """

    decorations: typing.Optional[TrailerStatDecorationResponseBody] = None
    time: str = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format.
    """

    value: TrailerStatReeferDoorStateZone1WithDecorationsTypeResponseBodyValue = pydantic.Field()
    """
    The door state of zone 2 of the reefer.  Valid values: `open`, `closed`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
