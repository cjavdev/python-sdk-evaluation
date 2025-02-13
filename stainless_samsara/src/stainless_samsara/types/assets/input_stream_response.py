# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "InputStreamResponse",
    "Data",
    "DataAsset",
    "DataAssetAttribute",
    "DataAssetTag",
    "DataAuxInput",
    "Pagination",
]


class DataAssetAttribute(BaseModel):
    id: Optional[str] = None
    """Id of the attribute"""

    name: Optional[str] = None
    """Name of the attribute"""

    number_values: Optional[List[float]] = FieldInfo(alias="numberValues", default=None)
    """List of number values associated with the attribute"""

    string_values: Optional[List[str]] = FieldInfo(alias="stringValues", default=None)
    """List of string values associated with the attribute."""


class DataAssetTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class DataAsset(BaseModel):
    id: str
    """ID of the asset"""

    attributes: Optional[List[DataAssetAttribute]] = None
    """List of attributes associated with the entity"""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    tags: Optional[List[DataAssetTag]] = None
    """
    The array of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Asset.
    """


class DataAuxInput(BaseModel):
    name: str
    """Name of the auxiliary input"""


class Data(BaseModel):
    asset: DataAsset
    """Asset that the input data is from."""

    happened_at_time: str = FieldInfo(alias="happenedAtTime")
    """UTC timestamp in RFC 3339 format of the event."""

    units: Literal["boolean", "millivolts", "microamps"]
    """Units of the values in the returned data.

    Valid values: `boolean`, `millivolts`, `microamps`
    """

    value: str
    """Value of the data point."""

    aux_input: Optional[DataAuxInput] = FieldInfo(alias="auxInput", default=None)
    """Auxiliary input metadata"""


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


class InputStreamResponse(BaseModel):
    data: List[Data]
    """Array of assets inputs objects."""

    pagination: Pagination
    """Pagination parameters."""
