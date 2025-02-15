# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .safety_event_behavior_labels_response_body_type import SafetyEventBehaviorLabelsResponseBodyType
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SafetyEventBehaviorLabelsResponseBody(UniversalBaseModel):
    """
    Behavior label for a safety event.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the behavior label.
    """

    type: typing.Optional[SafetyEventBehaviorLabelsResponseBodyType] = pydantic.Field(default=None)
    """
    Type of the BehaviorLabel.  Valid values: `Acceleration`, `Braking`, `Crash`, `DefensiveDriving`, `DidNotYield`, `Drinking`, `Drowsy`, `Eating`, `EatingDrinking`, `EdgeDistractedDriving`, `EdgeRailroadCrossingViolation`, `FollowingDistance`, `FollowingDistanceModerate`, `FollowingDistanceSevere`, `ForwardCollisionWarning`, `GenericDistraction`, `GenericTailgating`, `HarshTurn`, `Invalid`, `LaneDeparture`, `LateResponse`, `MobileUsage`, `NearCollison`, `NoSeatbelt`, `ObstructedCamera`, `PolicyViolationMask`, `RanRedLight`, `RollingStop`, `RolloverProtection`, `Smoking`, `Speeding`, `YawControl`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
