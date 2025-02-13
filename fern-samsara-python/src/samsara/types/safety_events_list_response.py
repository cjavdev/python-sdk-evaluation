# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .safety_event import SafetyEvent
from .pagination_response import PaginationResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SafetyEventsListResponse(UniversalBaseModel):
    """
    List of safety events.
    """

    data: typing.Optional[typing.List[SafetyEvent]] = None
    pagination: typing.Optional[PaginationResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
