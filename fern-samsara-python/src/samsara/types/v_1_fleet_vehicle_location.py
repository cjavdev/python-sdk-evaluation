# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class V1FleetVehicleLocation(UniversalBaseModel):
    """
    Contains the location and speed of a vehicle at a particular time
    """

    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The latitude of the location in degrees.
    """

    location: typing.Optional[str] = pydantic.Field(default=None)
    """
    The best effort (street,city,state) for the latitude and longitude.
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The longitude of the location in degrees.
    """

    speed_miles_per_hour: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="speedMilesPerHour")
    ] = pydantic.Field(default=None)
    """
    The speed calculated from GPS that the asset was traveling at in miles per hour.
    """

    time_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="timeMs")] = pydantic.Field(
        default=None
    )
    """
    Time in Unix milliseconds since epoch when the asset was at the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
