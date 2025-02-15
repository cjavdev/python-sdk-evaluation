# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .vehicle_response_object_response_body import VehicleResponseObjectResponseBody
import pydantic
from .goa_pagination_response_response_body import GoaPaginationResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class VehiclesListVehiclesResponseBody(UniversalBaseModel):
    data: typing.List[VehicleResponseObjectResponseBody] = pydantic.Field()
    """
    Multiple vehicles.
    """

    pagination: GoaPaginationResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
