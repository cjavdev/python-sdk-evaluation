# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrainingAssignmentStreamParams"]


class TrainingAssignmentStreamParams(TypedDict, total=False):
    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """A start time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    course_ids: Annotated[List[str], PropertyInfo(alias="courseIds")]
    """Optional string of comma separated course IDs.

    If course ID is present, training assignments for the specified course ID(s)
    will be returned. Max value for this value is 100 objects. Defaults to returning
    all courses. Example:
    `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    learner_ids: Annotated[List[str], PropertyInfo(alias="learnerIds")]
    """Optional string of comma separated learner IDs.

    If learner ID is present, training assignments for the specified learner(s) will
    be returned. Max value for this value is 100 objects. Example:
    `learnerIds=driver-281474,driver-46282156`
    """

    status: List[str]
    """Optional string of comma separated values.

    If status is present, training assignments for the specified status(s) will be
    returned. Valid values: "notStarted", "inProgress", "completed". Defaults to
    returning all courses.
    """
