# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .alert_object_driver_response_body import AlertObjectDriverResponseBody
from .alert_object_trailer_response_body import AlertObjectTrailerResponseBody
from .alert_object_vehicle_response_body import AlertObjectVehicleResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TireFaultsResponseBody(UniversalBaseModel):
    """
    Details specific to Tire Faults.
    """

    driver: typing.Optional[AlertObjectDriverResponseBody] = None
    trailer: typing.Optional[AlertObjectTrailerResponseBody] = None
    vehicle: typing.Optional[AlertObjectVehicleResponseBody] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
