# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrainingAssignmentCreateParams"]


class TrainingAssignmentCreateParams(TypedDict, total=False):
    course_id: Required[Annotated[str, PropertyInfo(alias="courseId")]]
    """String for the course ID."""

    due_at_time: Required[Annotated[str, PropertyInfo(alias="dueAtTime")]]
    """Due date of the training assignment in RFC 3339 format.

    Millisecond precision and timezones are supported.
    """

    learner_ids: Required[Annotated[List[str], PropertyInfo(alias="learnerIds")]]
    """Optional string of comma separated learner IDs.

    If learner ID is present, training assignments for the specified learner(s) will
    be returned. Max value for this value is 100 objects. Example:
    `learnerIds=driver-281474,driver-46282156`
    """
