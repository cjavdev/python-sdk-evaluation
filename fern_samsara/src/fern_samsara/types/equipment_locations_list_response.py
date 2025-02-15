# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .equipment_locations_list_response_data import EquipmentLocationsListResponseData
import pydantic
from .pagination_response import PaginationResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class EquipmentLocationsListResponse(UniversalBaseModel):
    """
    A time-series of equipment locations and pagination information
    """

    data: typing.List[EquipmentLocationsListResponseData] = pydantic.Field()
    """
    Time-series of locations for the specified units of equipment.
    """

    pagination: PaginationResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
