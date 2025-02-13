# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class InAppNotificationOptionsObjectRequestBody(UniversalBaseModel):
    """
    Options for in-app notifications
    """

    can_dictate_alert_title: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="canDictateAlertTitle")
    ] = pydantic.Field(default=None)
    """
    Whether the alert will dictate the title of the alert. Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled together.
    """

    can_play_alert_sound: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="canPlayAlertSound")
    ] = pydantic.Field(default=None)
    """
    Whether the alert will play a sound. Both canDictateAlertTitle and canPlayAlertSound should be enabled or disabled together.
    """

    custom_text: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="customText")] = pydantic.Field(
        default=None
    )
    """
    Custom text to display in the notification (320 character max).
    """

    is_enabled: typing_extensions.Annotated[bool, FieldMetadata(alias="isEnabled")] = pydantic.Field()
    """
    Whether in-app notifications are enabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
