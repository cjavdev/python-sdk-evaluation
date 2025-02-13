# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingCourseListParams"]


class TrainingCourseListParams(TypedDict, total=False):
    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    category_ids: Annotated[List[str], PropertyInfo(alias="categoryIds")]
    """Optional string of comma separated course category IDs.

    If courseCategoryId is present, training courses for the specified course
    category(s) will be returned. Max value for this value is 100 objects. Defaults
    to returning all courses. Example:
    `categoryIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    """

    course_ids: Annotated[List[str], PropertyInfo(alias="courseIds")]
    """Optional string of comma separated course IDs.

    If course ID is present, training assignments for the specified course ID(s)
    will be returned. Max value for this value is 100 objects. Defaults to returning
    all courses. Example:
    `courseIds=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    """

    status: List[str]
    """Optional string of comma separated values.

    If status is present, training courses with the specified status(s) will be
    returned. Valid values: “published”, “deleted”, “archived”. Defaults to
    returning all courses.
    """
