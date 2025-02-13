# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssetCreateParams", "Location"]


class AssetCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the asset."""

    custom_metadata: Annotated[Dict[str, str], PropertyInfo(alias="customMetadata")]
    """The custom fields of an asset."""

    location: Location
    """For locationType "point", latitude and longitude are required.

    For "address", formattedAddress must be provided, and lat/long can be optionally
    included for displaying a dot on the assets map. For "dataInput", this object
    should not be passed in.
    """

    location_data_input_id: Annotated[str, PropertyInfo(alias="locationDataInputId")]
    """Required if locationType is "dataInput".

    Specifies the id of a location data input which will determine the asset's
    location. **The data input will be moved to the new asset.**
    """

    location_type: Annotated[Literal["point", "address", "dataInput"], PropertyInfo(alias="locationType")]
    """The format of the location.

    This field is required if a location is provided. Valid values: `point`,
    `address`, `dataInput`.
    """

    parent_id: Annotated[str, PropertyInfo(alias="parentId")]
    """The id of the parent asset that the asset belongs to."""

    running_status_data_input_id: Annotated[str, PropertyInfo(alias="runningStatusDataInputId")]
    """
    The asset's isRunning status will be true when the associated data input's value
    is 1. Data input cannot be of location format. **The data input will be moved to
    the new asset.**
    """

    tag_ids: Annotated[List[str], PropertyInfo(alias="tagIds")]
    """The ids of the tags that the asset should belong to."""


class Location(TypedDict, total=False):
    formatted_address: Annotated[str, PropertyInfo(alias="formattedAddress")]
    """Formatted address of the location"""

    latitude: float
    """The latitude of the asset in decimal degrees."""

    longitude: float
    """The longitude of the asset in decimal degrees."""
