# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody",
    "Data",
    "DataCourse",
    "DataLearner",
    "Pagination",
]


class DataCourse(BaseModel):
    id: str
    """ID of the course."""

    revision_id: str = FieldInfo(alias="revisionId")
    """ID of the course's specific version."""


class DataLearner(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver"]
    """The type of the polymorphic user. Valid values: `driver`"""


class Data(BaseModel):
    id: str
    """ID of the training assignment."""

    course: DataCourse
    """Course that is associated with the training assignments."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the training assignment. UTC timestamp in RFC 3339 format."""

    created_by_id: str = FieldInfo(alias="createdById")
    """ID of the user who created the training assignment."""

    duration_minutes: int = FieldInfo(alias="durationMinutes")
    """Time spent on the training assignment."""

    learner: DataLearner
    """Learner that is associated with the training assignment.

    Only driver learners are supported currently.
    """

    status: Literal["notStarted", "inProgress", "completed"]
    """State for the Training Assignment.

    Always returned. Valid values: `notStarted`, `inProgress`, `completed`
    """

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time training assignment was updated by either a learner or an admin.

    UTC timestamp in RFC 3339 format.
    """

    updated_by_id: str = FieldInfo(alias="updatedById")
    """
    ID of the user who updated the training assignment, either an admin or a
    learner.
    """

    completed_at_time: Optional[datetime] = FieldInfo(alias="completedAtTime", default=None)
    """Time training assignment is completed.

    UTC timestamp in RFC 3339 format. Returned when a training assignment completion
    status is "complete".
    """

    deleted_at_time: Optional[datetime] = FieldInfo(alias="deletedAtTime", default=None)
    """Time training assignment is deleted. UTC timestamp in RFC 3339 format."""

    due_at_time: Optional[datetime] = FieldInfo(alias="dueAtTime", default=None)
    """Time training assignment is due.

    UTC timestamp in RFC 3339 format. Returned when an assignment has a due date set
    by an admin.
    """

    is_completed_late: Optional[bool] = FieldInfo(alias="isCompletedLate", default=None)
    """Indicates whether the training assignment was completed on time or not.

    Returned when a training assignment completion status is "complete" and has a
    dueAtTime set by an admin.
    """

    is_overdue: Optional[bool] = FieldInfo(alias="isOverdue", default=None)
    """Indicates whether the training assignment is past the due date.

    Returned when a training assignment completion status is 'inProgress' or
    'notStarted' and has a dueAtTime set by an admin.
    """

    score_percent: Optional[float] = FieldInfo(alias="scorePercent", default=None)
    """Quiz score associated with training assignment.

    Returned when a training assignment completion status is "complete".
    """

    started_at_time: Optional[datetime] = FieldInfo(alias="startedAtTime", default=None)
    """Time training assignment is started.

    UTC timestamp in RFC 3339 format. Returned when a training assignment completion
    status is "complete" or "inProgress".
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


class TrainingAssignmentsGetTrainingAssignmentsStreamResponseBody(BaseModel):
    data: List[Data]
    """List of training assignments."""

    pagination: Pagination
    """Pagination parameters."""
