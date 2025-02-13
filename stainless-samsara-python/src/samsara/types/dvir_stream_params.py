# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DvirStreamParams"]


class DvirStreamParams(TypedDict, total=False):
    start_time: Required[Annotated[str, PropertyInfo(alias="startTime")]]
    """
    Required RFC 3339 timestamp to begin the feed or history by `updatedAtTime` at
    `startTime`.
    """

    after: str
    """
    If specified, this should be the endCursor value from the previous page of
    results. When present, this request will return the next page of results that
    occur immediately after the previous page of results.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """Optional RFC 3339 timestamp.

    If not provided then the endpoint behaves as an unending feed of changes.
    """

    include_external_ids: Annotated[bool, PropertyInfo(alias="includeExternalIds")]
    """
    Optional boolean indicating whether to return external IDs on supported entities
    """

    limit: int
    """The limit for how many objects will be in the response.

    Default and max for this value is 200 objects.
    """

    safety_status: Annotated[List[str], PropertyInfo(alias="safetyStatus")]
    """Optional list of safety statuses. Valid values: [safe, unsafe, resolved]"""
