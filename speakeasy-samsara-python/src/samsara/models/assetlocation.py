"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssetLocationTypedDict(TypedDict):
    r"""For locationType \"point\", latitude and longitude are required. For \"address\", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For \"dataInput\", this object should not be passed in."""

    formatted_address: NotRequired[str]
    r"""Formatted address of the location"""
    latitude: NotRequired[float]
    r"""The latitude of the asset in decimal degrees."""
    longitude: NotRequired[float]
    r"""The longitude of the asset in decimal degrees."""


class AssetLocation(BaseModel):
    r"""For locationType \"point\", latitude and longitude are required. For \"address\", formattedAddress must be provided, and lat/long can be optionally included for displaying a dot on the assets map. For \"dataInput\", this object should not be passed in."""

    formatted_address: Annotated[
        Optional[str], pydantic.Field(alias="formattedAddress")
    ] = None
    r"""Formatted address of the location"""

    latitude: Optional[float] = None
    r"""The latitude of the asset in decimal degrees."""

    longitude: Optional[float] = None
    r"""The longitude of the asset in decimal degrees."""
