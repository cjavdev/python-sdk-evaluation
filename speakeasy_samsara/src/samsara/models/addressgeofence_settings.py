"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AddressGeofenceSettingsTypedDict(TypedDict):
    r"""Information about a geofence's settings."""

    show_addresses: NotRequired[bool]
    r"""If this property is set to true, then underlying geofence addresses will be shown in reports instead of a geofence's name."""


class AddressGeofenceSettings(BaseModel):
    r"""Information about a geofence's settings."""

    show_addresses: Annotated[Optional[bool], pydantic.Field(alias="showAddresses")] = (
        None
    )
    r"""If this property is set to true, then underlying geofence addresses will be shown in reports instead of a geofence's name."""
