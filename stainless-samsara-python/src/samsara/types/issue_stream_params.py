# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IssueStreamParams"]


class IssueStreamParams(TypedDict, total=False):
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

    asset_ids: Annotated[List[str], PropertyInfo(alias="assetIds")]
    """A comma-separated list containing up to 50 asset IDs to filter issues on.

    Issues with untracked assets can also be included by passing the value:
    'untracked'.
    """

    end_time: Annotated[str, PropertyInfo(alias="endTime")]
    """An end time in RFC 3339 format.

    Defaults to now if not provided. Millisecond precision and timezones are
    supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR
    2015-09-15T14:00:12-04:00).
    """

    include: List[str]
    """A comma separated list of additional fields to include on requested objects.

    Valid values: `externalIds`
    """

    status: List[str]
    """A comma-separated list containing status values to filter issues on.

    Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    """
