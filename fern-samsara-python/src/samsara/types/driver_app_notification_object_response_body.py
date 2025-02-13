# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .in_app_notification_options_object_response_body import InAppNotificationOptionsObjectResponseBody
from ..core.serialization import FieldMetadata
from .push_notification_options_object_response_body import PushNotificationOptionsObjectResponseBody
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DriverAppNotificationObjectResponseBody(UniversalBaseModel):
    """
    Driver app notification settings
    """

    in_app_notification_options: typing_extensions.Annotated[
        typing.Optional[InAppNotificationOptionsObjectResponseBody], FieldMetadata(alias="inAppNotificationOptions")
    ] = None
    push_notification_options: typing_extensions.Annotated[
        typing.Optional[PushNotificationOptionsObjectResponseBody], FieldMetadata(alias="pushNotificationOptions")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
