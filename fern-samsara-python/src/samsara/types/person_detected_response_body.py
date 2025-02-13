# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .alert_object_onvif_camera_stream_response_body import AlertObjectOnvifCameraStreamResponseBody
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PersonDetectedResponseBody(UniversalBaseModel):
    """
    Details specific to Person Detected.
    """

    camera_stream: typing_extensions.Annotated[
        typing.Optional[AlertObjectOnvifCameraStreamResponseBody], FieldMetadata(alias="cameraStream")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
