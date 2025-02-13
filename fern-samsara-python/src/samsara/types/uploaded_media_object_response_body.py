# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from .uploaded_media_object_response_body_input import UploadedMediaObjectResponseBodyInput
import typing
from .uploaded_media_object_response_body_trigger_reason import UploadedMediaObjectResponseBodyTriggerReason
from .url_info_object_response_body import UrlInfoObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UploadedMediaObjectResponseBody(UniversalBaseModel):
    available_at_time: typing_extensions.Annotated[str, FieldMetadata(alias="availableAtTime")] = pydantic.Field()
    """
    Timestamp, in RFC 3339 format, at which the media item was made available. Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00
    """

    end_time: typing_extensions.Annotated[str, FieldMetadata(alias="endTime")] = pydantic.Field()
    """
     An end time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    input: UploadedMediaObjectResponseBodyInput = pydantic.Field()
    """
    Input type for this media. Examples: dashcamForwardFacing  Valid values: `dashcamForwardFacing`, `dashcamInwardFacing`, `dashcamRearFacing`
    """

    media_type: typing_extensions.Annotated[typing.Literal["image"], FieldMetadata(alias="mediaType")] = pydantic.Field(
        default="image"
    )
    """
    Type of media. Examples: image  Valid values: `image`
    """

    start_time: typing_extensions.Annotated[str, FieldMetadata(alias="startTime")] = pydantic.Field()
    """
     A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00).
    """

    trigger_reason: typing_extensions.Annotated[
        UploadedMediaObjectResponseBodyTriggerReason, FieldMetadata(alias="triggerReason")
    ] = pydantic.Field()
    """
    Trigger reason for this media capture. Examples: api  Valid values: `api`, `panicButton`, `periodicStill`, `tripEndStill`, `tripStartStill`, `videoRetrieval`
    """

    url_info: typing_extensions.Annotated[
        typing.Optional[UrlInfoObjectResponseBody], FieldMetadata(alias="urlInfo")
    ] = None
    vehicle_id: typing_extensions.Annotated[str, FieldMetadata(alias="vehicleId")] = pydantic.Field()
    """
    Vehicle ID for which this media was captured. Examples: 1234
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
