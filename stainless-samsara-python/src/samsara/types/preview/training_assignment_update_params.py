# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingAssignmentUpdateParams"]


class TrainingAssignmentUpdateParams(TypedDict, total=False):
    due_at_time: Required[Annotated[str, PropertyInfo(alias="dueAtTime")]]
    """Due date of the training assignment in RFC 3339 format.

    Millisecond precision and timezones are supported.
    """

    ids: Required[List[str]]
    """String of comma separated assignments IDs.

    Max value for this value is 100 objects .Example:
    `ids=a4db8702-79d5-4396-a717-e301d52ecc11,c6490f6a-d84e-49b5-b0ad-b6baae304075`
    """
