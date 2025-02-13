# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DataInputsTinyResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the data input."""

    asset_id: Optional[str] = FieldInfo(alias="assetId", default=None)
    """Unique identifier for the data input's asset."""

    data_group: Optional[str] = FieldInfo(alias="dataGroup", default=None)
    """Data group for this data input."""

    name: Optional[str] = None
    """Name of this data input."""

    units: Optional[str] = None
    """Units of data for this data input."""


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


class DataInputsTinyResponse(BaseModel):
    data: Optional[List[Data]] = None
    """An array of data input objects.

    Each object contains the data input's name, ID, and other metadata.
    """

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
