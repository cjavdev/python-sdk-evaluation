# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .location_object_request_body import LocationObjectRequestBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class GeofenceExitTriggerDetailsObjectRequestBody(UniversalBaseModel):
    """
    Details specific to Geofence Exit
    """

    location: LocationObjectRequestBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
