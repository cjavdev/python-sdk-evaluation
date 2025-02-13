# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TrainingAssignmentsPostTrainingAssignmentsResponseBody", "Data", "DataCourse", "DataLearner"]


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

    is_existing_assignment: bool = FieldInfo(alias="isExistingAssignment")
    """Indicates whether the training assignment was already created."""

    learner: DataLearner
    """Learner that is associated with the training assignment.

    Only driver learners are supported currently.
    """

    due_at_time: Optional[datetime] = FieldInfo(alias="dueAtTime", default=None)
    """Time training assignment is due.

    UTC timestamp in RFC 3339 format. Returned when an assignment has a due date set
    by an admin.
    """


class TrainingAssignmentsPostTrainingAssignmentsResponseBody(BaseModel):
    data: List[Data]
    """List of created training assignments."""
