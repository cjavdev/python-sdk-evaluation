"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetlocation import AssetLocation, AssetLocationTypedDict
from .locationtype import LocationType
import pydantic
from samsara.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetCreateTypedDict(TypedDict):
    r"""The asset creation arguments"""

    name: str
    r"""The name of the asset."""
    custom_metadata: NotRequired[Dict[str, str]]
    r"""The custom fields of an asset."""
    location: NotRequired[AssetLocationTypedDict]
    r"""For locationType \"point\", latitude and longitude are required. For \"address\", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For \"dataInput\", this object should not be passed in."""
    location_data_input_id: NotRequired[str]
    r"""Required if locationType is \"dataInput\". Specifies the id of a location data input which will determine the asset's location. **The data input will be moved to the new asset.**"""
    location_type: NotRequired[LocationType]
    r"""The format of the location. This field is required if a location is provided. Valid values: `point`, `address`, `dataInput`."""
    parent_id: NotRequired[str]
    r"""The id of the parent asset that the asset belongs to."""
    running_status_data_input_id: NotRequired[str]
    r"""The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. **The data input will be moved to the new asset.**"""
    tag_ids: NotRequired[List[str]]
    r"""The ids of the tags that the asset should belong to."""


class AssetCreate(BaseModel):
    r"""The asset creation arguments"""

    name: str
    r"""The name of the asset."""

    custom_metadata: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="customMetadata")
    ] = None
    r"""The custom fields of an asset."""

    location: Optional[AssetLocation] = None
    r"""For locationType \"point\", latitude and longitude are required. For \"address\", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For \"dataInput\", this object should not be passed in."""

    location_data_input_id: Annotated[
        Optional[str], pydantic.Field(alias="locationDataInputId")
    ] = None
    r"""Required if locationType is \"dataInput\". Specifies the id of a location data input which will determine the asset's location. **The data input will be moved to the new asset.**"""

    location_type: Annotated[
        Optional[LocationType], pydantic.Field(alias="locationType")
    ] = None
    r"""The format of the location. This field is required if a location is provided. Valid values: `point`, `address`, `dataInput`."""

    parent_id: Annotated[Optional[str], pydantic.Field(alias="parentId")] = None
    r"""The id of the parent asset that the asset belongs to."""

    running_status_data_input_id: Annotated[
        Optional[str], pydantic.Field(alias="runningStatusDataInputId")
    ] = None
    r"""The asset's isRunning status will be true when the associated data input's value is 1. Data input cannot be of location format. **The data input will be moved to the new asset.**"""

    tag_ids: Annotated[Optional[List[str]], pydantic.Field(alias="tagIds")] = None
    r"""The ids of the tags that the asset should belong to."""
