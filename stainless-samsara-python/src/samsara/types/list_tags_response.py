# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ListTagsResponse",
    "Data",
    "DataAddress",
    "DataAsset",
    "DataDriver",
    "DataMachine",
    "DataParentTag",
    "DataSensor",
    "DataVehicle",
    "Pagination",
]


class DataAddress(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class DataAsset(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class DataDriver(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class DataMachine(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class DataParentTag(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The tag name."""


class DataSensor(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class DataVehicle(BaseModel):
    id: str
    """The object ID."""

    name: Optional[str] = None
    """The object name."""


class Data(BaseModel):
    id: Optional[str] = None
    """Unique Samsara ID of this tag."""

    addresses: Optional[List[DataAddress]] = None
    """The addresses that belong to this tag."""

    assets: Optional[List[DataAsset]] = None
    """The trailers, unpowered, and powered assets that belong to this tag."""

    drivers: Optional[List[DataDriver]] = None
    """The drivers that belong to this tag."""

    external_ids: Optional[object] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    machines: Optional[List[DataMachine]] = None
    """The machines that belong to thistag."""

    name: Optional[str] = None
    """Name of this tag."""

    parent_tag: Optional[DataParentTag] = FieldInfo(alias="parentTag", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the parent tag, otherwise
    this will be omitted.
    """

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """

    sensors: Optional[List[DataSensor]] = None
    """The sensors that belong to this tag."""

    vehicles: Optional[List[DataVehicle]] = None
    """The vehicles that belong to this tag."""


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


class ListTagsResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
    """Pagination parameters."""
