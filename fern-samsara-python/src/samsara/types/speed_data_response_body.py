# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import typing
from .alert_object_driver_response_body import AlertObjectDriverResponseBody
from .speed_data_response_body_operation import SpeedDataResponseBodyOperation
from .alert_object_trailer_response_body import AlertObjectTrailerResponseBody
from .alert_object_vehicle_response_body import AlertObjectVehicleResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SpeedDataResponseBody(UniversalBaseModel):
    """
    Details specific to Speed.
    """

    current_speed_kilometers_per_hour: typing_extensions.Annotated[
        int, FieldMetadata(alias="currentSpeedKilometersPerHour")
    ] = pydantic.Field()
    """
    Current speed of the vehicle in kilometers per hour.
    """

    driver: typing.Optional[AlertObjectDriverResponseBody] = None
    min_duration_milliseconds: typing_extensions.Annotated[int, FieldMetadata(alias="minDurationMilliseconds")] = (
        pydantic.Field()
    )
    """
    Minimum duration of the current speed in milliseconds.
    """

    operation: SpeedDataResponseBodyOperation = pydantic.Field()
    """
    Operation of the current and threshold comparison.  Valid values: `GREATER`, `INSIDE_RANGE`, `LESS`, `OUTSIDE_RANGE`
    """

    threshold_speed_kilometers_per_hour: typing_extensions.Annotated[
        int, FieldMetadata(alias="thresholdSpeedKilometersPerHour")
    ] = pydantic.Field()
    """
    Threshold speed of the vehicle in kilometers per hour.
    """

    trailer: typing.Optional[AlertObjectTrailerResponseBody] = None
    vehicle: typing.Optional[AlertObjectVehicleResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
