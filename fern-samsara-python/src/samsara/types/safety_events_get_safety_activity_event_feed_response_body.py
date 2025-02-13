# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .safety_event_activity_feed_item_response_body import SafetyEventActivityFeedItemResponseBody
import pydantic
from .goa_pagination_response_response_body import GoaPaginationResponseResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SafetyEventsGetSafetyActivityEventFeedResponseBody(UniversalBaseModel):
    data: typing.List[SafetyEventActivityFeedItemResponseBody] = pydantic.Field()
    """
    Paginated safety event activity feed limited to 10 events.
    """

    pagination: GoaPaginationResponseResponseBody

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
