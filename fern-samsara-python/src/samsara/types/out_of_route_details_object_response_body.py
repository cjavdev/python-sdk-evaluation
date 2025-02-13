# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class OutOfRouteDetailsObjectResponseBody(UniversalBaseModel):
    """
    Details specific to Out Of Route
    """

    max_off_route_meters: typing_extensions.Annotated[int, FieldMetadata(alias="maxOffRouteMeters")] = pydantic.Field()
    """
    The minimum distance in meters a vehicle has to be from its active route path to be considered out of its route.
    """

    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    The number of milliseconds the trigger needs to stay active before alerting.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
