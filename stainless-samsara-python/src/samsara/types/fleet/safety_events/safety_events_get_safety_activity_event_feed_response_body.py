# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SafetyEventsGetSafetyActivityEventFeedResponseBody",
    "Data",
    "DataSafetyEvent",
    "DataSafetyEventBehaviorLabel",
    "DataSafetyEventDriver",
    "DataSafetyEventVehicle",
    "Pagination",
]


class DataSafetyEventBehaviorLabel(BaseModel):
    name: Optional[str] = None
    """Name of the behavior label."""

    type: Optional[
        Literal[
            "Acceleration",
            "Braking",
            "Crash",
            "DefensiveDriving",
            "DidNotYield",
            "Drinking",
            "Drowsy",
            "Eating",
            "EatingDrinking",
            "EdgeDistractedDriving",
            "EdgeRailroadCrossingViolation",
            "FollowingDistance",
            "FollowingDistanceModerate",
            "FollowingDistanceSevere",
            "ForwardCollisionWarning",
            "GenericDistraction",
            "GenericTailgating",
            "HarshTurn",
            "Invalid",
            "LaneDeparture",
            "LateResponse",
            "MobileUsage",
            "NearCollison",
            "NoSeatbelt",
            "ObstructedCamera",
            "PolicyViolationMask",
            "RanRedLight",
            "RollingStop",
            "RolloverProtection",
            "Smoking",
            "Speeding",
            "YawControl",
        ]
    ] = None
    """Type of the BehaviorLabel.

    Valid values: `Acceleration`, `Braking`, `Crash`, `DefensiveDriving`,
    `DidNotYield`, `Drinking`, `Drowsy`, `Eating`, `EatingDrinking`,
    `EdgeDistractedDriving`, `EdgeRailroadCrossingViolation`, `FollowingDistance`,
    `FollowingDistanceModerate`, `FollowingDistanceSevere`,
    `ForwardCollisionWarning`, `GenericDistraction`, `GenericTailgating`,
    `HarshTurn`, `Invalid`, `LaneDeparture`, `LateResponse`, `MobileUsage`,
    `NearCollison`, `NoSeatbelt`, `ObstructedCamera`, `PolicyViolationMask`,
    `RanRedLight`, `RollingStop`, `RolloverProtection`, `Smoking`, `Speeding`,
    `YawControl`
    """


class DataSafetyEventDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""


class DataSafetyEventVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""


class DataSafetyEvent(BaseModel):
    id: Optional[str] = None
    """The unique Samsara ID of the safety event."""

    behavior_labels: Optional[List[DataSafetyEventBehaviorLabel]] = FieldInfo(alias="behaviorLabels", default=None)
    """Behavior labels for a safety event."""

    driver: Optional[DataSafetyEventDriver] = None
    """A minified driver object."""

    time: Optional[str] = None
    """The time the safety event occurred in RFC 3339 milliseconds format."""

    vehicle: Optional[DataSafetyEventVehicle] = None
    """A minified vehicle object."""


class Data(BaseModel):
    id: str
    """The ID of the activity event feed line item."""

    safety_event: DataSafetyEvent = FieldInfo(alias="safetyEvent")
    """The safety event that was updated."""

    time: str
    """
    The time the activity occurred in the corresponding safety event in RFC 3339
    milliseconds format.
    """

    type: Literal["BehaviorLabelActivityType", "CoachingStateActivityType", "CreateSafetyEventActivityType"]
    """The type of activity that occurred in the safety event.

    We currently only support CoachingStateActivityType, BehaviorLabelActivityType,
    and CreateSafetyEventActivityType, but we may add support for more activity
    types in the future. Valid values: `BehaviorLabelActivityType`,
    `CoachingStateActivityType`, `CreateSafetyEventActivityType`
    """


class Pagination(BaseModel):
    end_cursor: str = FieldInfo(alias="endCursor")
    """Cursor identifier representing the last element in the response.

    This value should be used in conjunction with a subsequent request's 'after'
    query parameter. This may be an empty string if there are no more pages left to
    view.
    """

    has_next_page: bool = FieldInfo(alias="hasNextPage")
    """
    True if there are more pages of results immediately available after this
    endCursor.
    """


class SafetyEventsGetSafetyActivityEventFeedResponseBody(BaseModel):
    data: List[Data]
    """Paginated safety event activity feed limited to 10 events."""

    pagination: Pagination
    """Pagination parameters."""
