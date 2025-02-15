# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .driver_tachograph_activity_data import DriverTachographActivityData
from .pagination_response import PaginationResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DriverTachographActivityResponse(UniversalBaseModel):
    """
    List of all driver tachograph activities in a specified time range.
    """

    data: typing.Optional[DriverTachographActivityData] = None
    pagination: typing.Optional[PaginationResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
