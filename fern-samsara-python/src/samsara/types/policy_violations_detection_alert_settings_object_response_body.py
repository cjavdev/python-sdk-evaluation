# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from .policy_violations_detection_alert_settings_object_response_body_events_available_for_testing_item import (
    PolicyViolationsDetectionAlertSettingsObjectResponseBodyEventsAvailableForTestingItem,
)
from ..core.serialization import FieldMetadata
import pydantic
from .policy_violations_detection_alert_settings_object_response_body_events_to_coach_item import (
    PolicyViolationsDetectionAlertSettingsObjectResponseBodyEventsToCoachItem,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PolicyViolationsDetectionAlertSettingsObjectResponseBody(UniversalBaseModel):
    """
    Enables detection of policy violations, surfaces events in Safety Inbox, and enables configurable alerts. While the feature is in beta, in-cab alerts are recommended for testing use only.
    """

    events_available_for_testing: typing_extensions.Annotated[
        typing.Optional[
            typing.List[PolicyViolationsDetectionAlertSettingsObjectResponseBodyEventsAvailableForTestingItem]
        ],
        FieldMetadata(alias="eventsAvailableForTesting"),
    ] = pydantic.Field(default=None)
    """
    List of selectable beta policy violation events to be tested.
    """

    events_to_coach: typing_extensions.Annotated[
        typing.Optional[typing.List[PolicyViolationsDetectionAlertSettingsObjectResponseBodyEventsToCoachItem]],
        FieldMetadata(alias="eventsToCoach"),
    ] = pydantic.Field(default=None)
    """
    List of selectable policy violation events to enable coaching for.
    """

    has_in_cab_audio_alerts_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasInCabAudioAlertsEnabled")
    ] = pydantic.Field(default=None)
    """
    Indicates whether in-cab audio alerts for rolling stops are turned on.
    """

    is_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isEnabled")] = pydantic.Field(
        default=None
    )
    """
    Indicates whether AI event detection for rolling stops is turned on.
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
