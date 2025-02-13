# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "SafetyEventsListResponse",
    "Data",
    "DataBehaviorLabel",
    "DataDriver",
    "DataLocation",
    "DataVehicle",
    "Pagination",
]


class DataBehaviorLabel(BaseModel):
    label: Literal[
        "genericTailgating",
        "genericDistraction",
        "defensiveDriving",
        "rollingStop",
        "nearCollison",
        "speeding",
        "obstructedCamera",
        "didNotYield",
        "noSeatbelt",
        "mobileUsage",
        "drowsy",
        "laneDeparture",
        "followingDistanceSevere",
        "followingDistanceModerate",
        "lateResponse",
        "acceleration",
        "braking",
        "harshTurn",
        "crash",
        "rolloverProtection",
        "yawControl",
        "ranRedLight",
        "forwardCollisionWarning",
        "eatingDrinking",
        "smoking",
        "followingDistance",
        "edgeDistractedDriving",
    ]
    """The label associated with the safety event.

    This list often changes, so it is recommended that clients gracefully handle any
    types not enumerated in this list. Valid values: `genericTailgating`,
    `genericDistraction`, `defensiveDriving`, `rollingStop`, `nearCollison`,
    `speeding`, `obstructedCamera`, `didNotYield`, `noSeatbelt`, `mobileUsage`,
    `drowsy`, `laneDeparture`, `followingDistanceSevere`,
    `followingDistanceModerate`, `lateResponse`, `acceleration`, `braking`,
    `harshTurn`, `crash`, `rolloverProtection`, `yawControl`, `ranRedLight`,
    `forwardCollisionWarning`, `eatingDrinking`, `smoking`, `followingDistance`,
    `edgeDistractedDriving`.
    """

    source: Literal["automated", "userGenerated"]
    """The source of the label associated with the safety event.

    Valid values: `automated`, `userGenerated`.
    """

    name: Optional[str] = None
    """The name of the label associated with the safety event."""


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataLocation(BaseModel):
    latitude: float
    """GPS latitude represented in degrees"""

    longitude: float
    """GPS longitude represented in degrees"""


class DataVehicle(BaseModel):
    id: Optional[str] = None
    """ID of the vehicle."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="ExternalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    name: Optional[str] = None
    """Name of the vehicle."""


class Data(BaseModel):
    id: Optional[str] = None
    """The unique Samsara ID of the safety event."""

    behavior_labels: Optional[List[DataBehaviorLabel]] = FieldInfo(alias="behaviorLabels", default=None)
    """The most up-to-date behavior labels associated with the safety event.

    These labels can be updated by the Safety Report Admin.
    """

    coaching_state: Optional[
        Literal[
            "needsReview",
            "coached",
            "dismissed",
            "reviewed",
            "archived",
            "manualReview",
            "needsCoaching",
            "autoDismissed",
            "needsRecognition",
            "recognized",
            "invalid",
        ]
    ] = FieldInfo(alias="coachingState", default=None)
    """The current coaching status of the event.

    Valid values: `needsReview`, `coached`, `dismissed`, `reviewed`, `archived`,
    `manualReview`, `needsCoaching`, `autoDismissed`, `needsRecognition`,
    `recognized`, `invalid`.
    """

    download_forward_video_url: Optional[str] = FieldInfo(alias="downloadForwardVideoUrl", default=None)
    """URL to download the forward video."""

    download_inward_video_url: Optional[str] = FieldInfo(alias="downloadInwardVideoUrl", default=None)
    """URL to download the inward video."""

    download_tracked_inward_video_url: Optional[str] = FieldInfo(alias="downloadTrackedInwardVideoUrl", default=None)
    """URL to download the tracked inward video."""

    driver: Optional[DataDriver] = None
    """A minified driver object."""

    location: Optional[DataLocation] = None
    """Location object"""

    max_acceleration_g_force: Optional[float] = FieldInfo(alias="maxAccelerationGForce", default=None)
    """The maximum acceleration value as a multiplier on the force of gravity (g)."""

    time: Optional[str] = None
    """The time the safety event occurred in RFC 3339 milliseconds format."""

    vehicle: Optional[DataVehicle] = None
    """A minified vehicle object."""


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


class SafetyEventsListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
