# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FollowingDistanceDetectionAlertSettingsObjectResponseBody(UniversalBaseModel):
    """
    Enables AI detection of tailgating or unsafe following distances, surfaces events in Safety Inbox, and enables configurable alerts. By default, Following Distance will impact the drivers' safety score.
    """

    duration_ms: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="durationMs")] = pydantic.Field(
        default=None
    )
    """
    Duration of following distance at which to alert, measured in milliseconds.
    """

    has_in_cab_audio_alerts_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasInCabAudioAlertsEnabled")
    ] = pydantic.Field(default=None)
    """
    Indicates whether in-cab audio alerts for following distance are turned on.
    """

    is_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isEnabled")] = pydantic.Field(
        default=None
    )
    """
    Indicates whether AI event detection for following distance is turned on.
    """

    speeding_threshold_mph: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="speedingThresholdMph")
    ] = pydantic.Field(default=None)
    """
    Alert when speed is over this many miles per hour.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
