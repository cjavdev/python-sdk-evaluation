# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["HistoryListResponse", "Data", "DataActivity", "DataDriver", "Pagination"]


class DataActivity(BaseModel):
    end_time: Optional[str] = FieldInfo(alias="endTime", default=None)
    """End time of state in RFC 3339 format."""

    is_manual_entry: Optional[bool] = FieldInfo(alias="isManualEntry", default=None)
    """A flag indicating whether the activity was manually entered by the driver.

    If this is `true`, the state cannot be "UNKNOWN"
    """

    start_time: Optional[str] = FieldInfo(alias="startTime", default=None)
    """Start time of state in RFC 3339 format."""

    state: Optional[Literal["BREAK/REST", "WORK", "AVAILABILITY", "DRIVING", "UNKNOWN"]] = None
    """Tachograph activity state.

    Valid values: `BREAK/REST`, `WORK`, `AVAILABILITY`, `DRIVING`, `UNKNOWN`.
    """


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class Data(BaseModel):
    activity: Optional[List[DataActivity]] = None
    """List of all driver tachograph activities in a specified time range."""

    driver: Optional[DataDriver] = None
    """A minified driver object."""


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


class HistoryListResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
