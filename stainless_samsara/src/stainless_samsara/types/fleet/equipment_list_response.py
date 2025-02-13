# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EquipmentListResponse", "Data", "DataInstalledGateway", "DataTag", "Pagination"]


class DataInstalledGateway(BaseModel):
    model: Optional[str] = None
    """The model of the installed Samsara gateway."""

    serial: Optional[str] = None
    """The serial of the installed Samsara gateway."""


class DataTag(BaseModel):
    id: Optional[str] = None
    """ID of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """Unique Samsara ID for the equipment."""

    asset_serial: Optional[str] = FieldInfo(alias="assetSerial", default=None)
    """An equipment identification number."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """
    The [external IDs](https://developers.samsara.com/docs/external-ids) for the
    given object.
    """

    installed_gateway: Optional[DataInstalledGateway] = FieldInfo(alias="installedGateway", default=None)

    name: Optional[str] = None
    """Name of the equipment."""

    notes: Optional[str] = None
    """Notes about a piece of equipment. Samsara supports a maximum of 255 chars."""

    tags: Optional[List[DataTag]] = None
    """An array of all tag mini-objects that are associated with the given equipment."""


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


class EquipmentListResponse(BaseModel):
    data: List[Data]
    """List of equipment objects."""

    pagination: Pagination
    """Pagination parameters."""
