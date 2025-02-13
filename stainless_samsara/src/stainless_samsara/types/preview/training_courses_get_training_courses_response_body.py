# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TrainingCoursesGetTrainingCoursesResponseBody", "Data", "DataCategory", "DataLabel", "Pagination"]


class DataCategory(BaseModel):
    id: str
    """Category ID of the course."""

    name: str
    """Category name of the course."""


class DataLabel(BaseModel):
    name: str
    """Name of the course label. Valid values: “safety”."""

    type: str
    """Type of the course label.

    Valid values when course.label.name is ‘safety’: accel, braking, crashSharpTurn,
    rolloverProtection, yawControl, speeding, rolledStopSign, tileRollingRailroad,
    seatbeltPolicy, nearCollision, phonePolicy, drowsy, defensiveDriving,
    driverObstructionPolicy, didNotYield, distractedDriving, tailgating,
    laneDeparture, lateResponse, ranRedLight, forwardCollisionWarning,
    foodDrinkPolicy, smokingPolicy, maskPolicy, maxSpeed, severeSpeeding,
    drinkPolicy, foodPolicy, unknown.
    """


class Data(BaseModel):
    id: str
    """ID of the training course."""

    category: DataCategory
    """Category of the training course."""

    estimated_time_to_complete_minutes: int = FieldInfo(alias="estimatedTimeToCompleteMinutes")
    """Estimated time it takes to complete the course."""

    revision_id: str = FieldInfo(alias="revisionId")
    """ID of the course's specific version."""

    status: Literal["published", "deleted", "archived", "unknown"]
    """Status of the training course.

    Always returned. Note: Only courses in a ‘published’ state are assignable to
    learners. Archiving a course deletes only ‘inProgress’ assignments associated
    with that course, and deleting a course deletes all assignments associated with
    that course. Valid values: `published`, `deleted`, `archived`, `unknown`
    """

    title: str
    """Title of the course."""

    description: Optional[str] = None
    """Description of the course."""

    label: Optional[DataLabel] = None
    """Label of the training course."""


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


class TrainingCoursesGetTrainingCoursesResponseBody(BaseModel):
    data: List[Data]
    """List of training courses."""

    pagination: Pagination
    """Pagination parameters."""
