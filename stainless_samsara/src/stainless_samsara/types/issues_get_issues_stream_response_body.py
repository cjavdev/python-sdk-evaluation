# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "IssuesGetIssuesStreamResponseBody",
    "Data",
    "DataIssueSource",
    "DataSubmittedBy",
    "DataAsset",
    "DataAssignedTo",
    "DataMediaList",
    "Pagination",
]


class DataIssueSource(BaseModel):
    type: Literal["form", "ad-hoc"]
    """The type of issue source. Valid values: `form`, `ad-hoc`"""

    id: Optional[str] = None
    """ID of the issue's source object.

    The format depends on the 'type'. Included if 'type' is not 'ad-hoc'.
    """


class DataSubmittedBy(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataAsset(BaseModel):
    entry_type: Literal["tracked", "untracked"] = FieldInfo(alias="entryType")
    """The type of entry for the asset. Valid values: `tracked`, `untracked`"""

    id: Optional[str] = None
    """ID of a tracked asset. Included if 'entryType' is 'tracked'."""

    name: Optional[str] = None
    """Name of an untracked (i.e. manually entered) asset."""


class DataAssignedTo(BaseModel):
    id: str
    """ID of the polymorphic user."""

    type: Literal["driver", "user"]
    """The type of the polymorphic user. Valid values: `driver`, `user`"""


class DataMediaList(BaseModel):
    id: str
    """ID of the media record."""

    processing_status: Literal["unknown", "processing", "finished"] = FieldInfo(alias="processingStatus")
    """Status of the media record. Valid values: `unknown`, `processing`, `finished`"""

    url: Optional[str] = None
    """URL containing a link to associated media content.

    Included if 'processingStatus' is 'finished'.
    """

    url_expires_at: Optional[datetime] = FieldInfo(alias="urlExpiresAt", default=None)
    """Expiration time of the media record 'url'. UTC timestamp in RFC 3339 format."""


class Data(BaseModel):
    id: str
    """ID of the issue."""

    created_at_time: datetime = FieldInfo(alias="createdAtTime")
    """Creation time of the issue. UTC timestamp in RFC 3339 format."""

    issue_source: DataIssueSource = FieldInfo(alias="issueSource")
    """Contains information about where an issue came from."""

    status: Literal["open", "inProgress", "resolved", "dismissed"]
    """Status of the issue.

    Valid values: `open`, `inProgress`, `resolved`, `dismissed`
    """

    submitted_at_time: datetime = FieldInfo(alias="submittedAtTime")
    """Submission time of the issue. UTC timestamp in RFC 3339 format."""

    submitted_by: DataSubmittedBy = FieldInfo(alias="submittedBy")
    """User or driver object."""

    title: str
    """Title of the issue."""

    updated_at_time: datetime = FieldInfo(alias="updatedAtTime")
    """Update time of the issue. UTC timestamp in RFC 3339 format."""

    asset: Optional[DataAsset] = None
    """Tracked or untracked (i.e. manually entered) asset object."""

    assigned_to: Optional[DataAssignedTo] = FieldInfo(alias="assignedTo", default=None)
    """User or driver object."""

    description: Optional[str] = None
    """Description of the issue. Included if the issue was given a description."""

    due_date: Optional[datetime] = FieldInfo(alias="dueDate", default=None)
    """Due date of the issue.

    UTC timestamp in RFC 3339 format. Included if the issue was assigned a due date.
    """

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    media_list: Optional[List[DataMediaList]] = FieldInfo(alias="mediaList", default=None)
    """List of media objects for the issue. Included if the issue has media."""

    priority: Optional[Literal["low", "medium", "high"]] = None
    """Priority of the issue.

    Included if the issue was assigned a priority. Valid values: `low`, `medium`,
    `high`
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


class IssuesGetIssuesStreamResponseBody(BaseModel):
    data: List[Data]
    """List of issues."""

    pagination: Pagination
    """Pagination parameters."""
