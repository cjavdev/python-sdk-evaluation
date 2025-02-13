# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AssetListResponse", "Data", "DataTag", "Pagination"]


class DataTag(BaseModel):
    id: str
    """ID of the tag"""

    name: str
    """Name of the tag."""

    parent_tag_id: Optional[str] = FieldInfo(alias="parentTagId", default=None)
    """
    If this tag is part a hierarchical tag tree, this is the ID of the parent tag,
    otherwise this will be omitted.
    """


class Data(BaseModel):
    id: str
    """The unique ID of the asset."""

    created_at_time: str = FieldInfo(alias="createdAtTime")
    """The time the asset was created in RFC 3339 format."""

    updated_at_time: str = FieldInfo(alias="updatedAtTime")
    """The time the asset was last updated in RFC 3339 format."""

    external_ids: Optional[Dict[str, str]] = FieldInfo(alias="externalIds", default=None)
    """A map of external ids"""

    license_plate: Optional[str] = FieldInfo(alias="licensePlate", default=None)
    """The license plate of the asset."""

    make: Optional[str] = None
    """The manufacturer of the asset.

    (If a VIN is entered and the system detects it is registered to a different
    manufacturer than provided an error will be returned).
    """

    model: Optional[str] = None
    """The manufacturer model of the asset.

    (If a VIN is entered and the system detects it is registered to a different
    model than provided an error will be returned).
    """

    name: Optional[str] = None
    """The human-readable name of the asset.

    This is set by a fleet administrator and will appear in both Samsara’s cloud
    dashboard as well as the Samsara Driver mobile app. By default, this name is the
    serial number of the Samsara Asset Gateway. It can be set or updated through the
    Samsara Dashboard or through the API at any time.
    """

    notes: Optional[str] = None
    """These are generic notes about the asset.

    Can be set or updated through the Samsara Dashboard or the API at any time.
    """

    regulation_mode: Optional[Literal["mixed", "regulated", "unregulated"]] = FieldInfo(
        alias="regulationMode", default=None
    )
    """
    Whether or not the asset is regulated, unregulated (non-CMV), or a mixed use
    unregulated asset. Primarily used with vehicles. Valid values: `mixed`,
    `regulated`, `unregulated`
    """

    serial_number: Optional[str] = FieldInfo(alias="serialNumber", default=None)
    """The serial number of the asset."""

    tags: Optional[List[DataTag]] = None
    """
    The list of
    [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting)
    associated with the Asset.
    """

    type: Optional[Literal["uncategorized", "trailer", "equipment", "unpowered", "vehicle"]] = None
    """The operational context in which the asset interacts with the Samsara system.

    Examples: Vehicle (eg: truck, bus...), Trailer (eg: dry van, reefer,
    flatbed...), Powered Equipment (eg: dozer, crane...), Unpowered Equipment (eg:
    container, dumpster...), or Uncategorized. Valid values: `uncategorized`,
    `trailer`, `equipment`, `unpowered`, `vehicle`
    """

    vin: Optional[str] = None
    """The vehicle identification number of the asset."""

    year: Optional[int] = None
    """The year of manufacture of the asset.

    (If a VIN is entered and the system detects it is registered to a different year
    than provided an error will be returned).
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


class AssetListResponse(BaseModel):
    data: List[Data]
    """List of assets"""

    pagination: Pagination
    """Pagination parameters."""
