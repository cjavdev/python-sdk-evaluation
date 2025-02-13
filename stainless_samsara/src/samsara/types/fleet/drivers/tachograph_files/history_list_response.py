# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["HistoryListResponse", "Data", "DataDriver", "DataFile", "Pagination"]


class DataDriver(BaseModel):
    id: Optional[str] = None
    """ID of the driver."""

    name: Optional[str] = None
    """Name of the driver."""


class DataFile(BaseModel):
    id: Optional[str] = None
    """ID of the file."""

    card_number: Optional[str] = FieldInfo(alias="cardNumber", default=None)
    """Tachograph card number associated with the file."""

    created_at_time: Optional[str] = FieldInfo(alias="createdAtTime", default=None)
    """Creation time of files in RFC 3339 format.

    This is either the download time from the tachograph itself (for files
    downloaded via Samsara VG) or upload time (for files manually uploaded via
    Samsara UI).
    """

    url: Optional[str] = None
    """A temporary URL which can be used to download the file.

    The link can be used multiple times and expires after an hour.
    """


class Data(BaseModel):
    driver: Optional[DataDriver] = None
    """A minified driver object."""

    files: Optional[List[DataFile]] = None
    """List of all tachograph driver files in a specified time range."""


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
