# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class HosEldEventLocationObjectResponseBody(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The best effort city for the latitude and longitude.
    """

    eld_location: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="eldLocation")] = (
        pydantic.Field(default=None)
    )
    """
    Relative location to the city, village, or town with population of 5,000 or greater.
    """

    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The latitude of the location.
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The longitude of the location.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The best effort state for the latitude and longitude.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
