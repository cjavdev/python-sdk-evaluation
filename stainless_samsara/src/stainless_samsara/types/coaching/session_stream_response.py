# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionStreamResponse", "Data", "DataBehavior", "DataBehaviorCoachableEvent", "DataDriver", "Pagination"]


class DataBehaviorCoachableEvent(BaseModel):
    id: str
    """Unique ID for an event within the item in a coaching session."""


class DataBehavior(BaseModel):
    id: str
    """Unique ID for the coaching behavior."""

    coachable_behavior_type: Literal[
        "acceleration",
        "braking",
        "cameraObstruction",
        "crash",
        "defensiveDriving",
        "didNotYield",
        "drinkPolicy",
        "drowsy",
        "eatingDrinking",
        "event",
        "falsePositive",
        "foodPolicy",
        "forwardCollisionWarning",
        "genericDistraction",
        "harshTurn",
        "laneDeparture",
        "lateResponse",
        "maskPolicy",
        "maxSpeed",
        "mobileUsage",
        "nearCollison",
        "noSeatbelt",
        "obstructedCamera",
        "outwardObstruction",
        "passengerPolicy",
        "ranRedLight",
        "rollingRailroadCrossing",
        "rollingStop",
        "rollover",
        "rolloverProtection",
        "rolloverProtectionBrakeControlActivated",
        "rolloverProtectionEngineControlActivated",
        "severeSpeeding",
        "smoking",
        "speeding",
        "tailgating",
        "unknown",
        "yawControl",
        "yawControlBrakeControlActivated",
        "yawControlEngineControlActivated",
    ] = FieldInfo(alias="coachableBehaviorType")
    """Coachable behavior type for the behavior in the coaching session.

    Valid values: `acceleration`, `braking`, `cameraObstruction`, `crash`,
    `defensiveDriving`, `didNotYield`, `drinkPolicy`, `drowsy`, `eatingDrinking`,
    `event`, `falsePositive`, `foodPolicy`, `forwardCollisionWarning`,
    `genericDistraction`, `harshTurn`, `laneDeparture`, `lateResponse`,
    `maskPolicy`, `maxSpeed`, `mobileUsage`, `nearCollison`, `noSeatbelt`,
    `obstructedCamera`, `outwardObstruction`, `passengerPolicy`, `ranRedLight`,
    `rollingRailroadCrossing`, `rollingStop`, `rollingStop`, `rollover`,
    `rolloverProtection`, `rolloverProtectionBrakeControlActivated`,
    `rolloverProtectionEngineControlActivated`, `severeSpeeding`, `smoking`,
    `speeding`, `tailgating`, `unknown`, `yawControl`,
    `yawControlBrakeControlActivated`, `yawControlEngineControlActivated`
    """

    last_coached_time: datetime = FieldInfo(alias="lastCoachedTime")
    """Time of last coached date for the same behavior label."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time of coaching behavior update in UTC."""

    coachable_events: Optional[List[DataBehaviorCoachableEvent]] = FieldInfo(alias="coachableEvents", default=None)
    """Object references for the coachableEvents within the behavior.

    For non Speeding events, corresponds to the unique Samsara ID of the safety
    event as “vehicleId - eventMS”, for Speeding events corresponds to the unique
    UUID of the event. Returned when includeCoachableEvents is 'true'. Capped at 100
    coachable events per Coaching session. For sessions where coachable events
    exceed 100, please visit the Samsara dashboard to address this coaching session.
    """

    note: Optional[str] = None
    """Associated note for the coaching behavior. Returned when present."""


class DataDriver(BaseModel):
    driver_id: str = FieldInfo(alias="driverId")
    """Samsara ID of the driver."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""


class Data(BaseModel):
    id: str
    """Unique ID for the coaching session."""

    behaviors: List[DataBehavior]
    """Object references for the behaviors within the session."""

    coaching_type: Literal["fullySharedWithManager", "selfCoaching", "unknown", "unshared", "withManager"] = FieldInfo(
        alias="coachingType"
    )
    """Coaching type for the coaching session.

    Valid values: `fullySharedWithManager`, `selfCoaching`, `unknown`, `unshared`,
    `withManager`
    """

    driver: DataDriver
    """A driver object with an id and map of external ids."""

    due_at_time: datetime = FieldInfo(alias="dueAtTime")
    """Time coaching session is due in UTC."""

    session_status: Literal["unknown", "upcoming", "completed", "deleted"] = FieldInfo(alias="sessionStatus")
    """Status for the coaching session.

    Valid values: `unknown`, `upcoming`, `completed`, `deleted`
    """

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time coaching session was updated in UTC."""

    assigned_coach_id: Optional[str] = FieldInfo(alias="assignedCoachId", default=None)
    """Unique user ID for a coaching session.

    Returned when a coaching session status is “incomplete”.
    """

    completed_at_time: Optional[datetime] = FieldInfo(alias="completedAtTime", default=None)
    """Time coaching session is completed in UTC.

    Returned when a coaching session status is “completed”.
    """

    completed_coach_id: Optional[str] = FieldInfo(alias="completedCoachId", default=None)
    """Unique user ID for a completed coaching session.

    Returned when a coaching session status is “completed”.
    """

    session_note: Optional[str] = FieldInfo(alias="sessionNote", default=None)
    """Associated note for the coaching session. Returned when present."""


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


class SessionStreamResponse(BaseModel):
    data: List[Data]
    """List of coaching sessions objects."""

    pagination: Pagination
    """Pagination parameters."""
