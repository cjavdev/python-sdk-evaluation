# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .asset_response_response_body import AssetResponseResponseBody
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .location_response_response_body import LocationResponseResponseBody
import typing
from .speed_response_response_body import SpeedResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LocationAndSpeedResponseResponseBody(UniversalBaseModel):
    """
    Full location and speed objects.
    """

    asset: AssetResponseResponseBody
    happened_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="happenedAtTime")] = pydantic.Field()
    """
    UTC timestamp in RFC 3339 format of the event.
    """

    location: LocationResponseResponseBody
    speed: typing.Optional[SpeedResponseResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
