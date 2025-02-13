# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .media_object_response_body import MediaObjectResponseBody
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetMediaRetrievalObjectResponseBody(UniversalBaseModel):
    media: typing.List[MediaObjectResponseBody] = pydantic.Field()
    """
    List of media retrieval objects.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
