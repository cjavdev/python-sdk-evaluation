"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class DeviceAssetResponseResponseBodyTypedDict(TypedDict):
    r"""Asset that the device is tied to."""

    id: str
    r"""The unique ID of the asset."""
    name: str
    r"""The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""


class DeviceAssetResponseResponseBody(BaseModel):
    r"""Asset that the device is tied to."""

    id: str
    r"""The unique ID of the asset."""

    name: str
    r"""The human-readable name of the asset. This is set by a fleet administrator and will appear in both Samsara’s cloud dashboard as well as the Samsara Driver mobile app. By default, this name is the serial number of the Samsara Asset Gateway. It can be set or updated through the Samsara Dashboard or through the API at any time."""
