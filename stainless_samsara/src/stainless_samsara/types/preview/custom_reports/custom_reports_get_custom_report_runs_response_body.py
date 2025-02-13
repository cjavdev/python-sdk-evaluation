# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["CustomReportsGetCustomReportRunsResponseBody", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Unique ID for the custom report run object."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Time of when the custom report run was created in RFC 3339 format."""

    custom_report_id: str = FieldInfo(alias="customReportId")
    """Unique ID for the custom report that it belongs to."""

    end_time: datetime = FieldInfo(alias="endTime")
    """The end time of the custom report run in RFC 3339 format."""

    percent_complete: int = FieldInfo(alias="percentComplete")
    """The percentage completed of this custom report run.

    Valid values from 0-100, inclusive.
    """

    start_time: datetime = FieldInfo(alias="startTime")
    """The start time of the custom report run in RFC 3339 format."""

    status: Literal["completed", "pending", "failed", "cancelled"]
    """The status of the custom report run.

    Valid values: `completed`, `pending`, `failed`, `cancelled`
    """

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Time of when the custom report run was last updated in RFC 3339 format."""

    attribute_value_ids: Optional[List[str]] = FieldInfo(alias="attributeValueIds", default=None)
    """
    The optional array of attribute value ids to filter the custom report run data
    by.
    """

    tag_ids: Optional[List[str]] = FieldInfo(alias="tagIds", default=None)
    """The optional array of tag ids to filter the custom report run by."""


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


class CustomReportsGetCustomReportRunsResponseBody(BaseModel):
    data: List[Data]
    """List of custom report runs."""

    pagination: Pagination
    """Pagination parameters."""
