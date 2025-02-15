"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class AssetResponseParentAssetTypedDict(TypedDict):
    r"""The asset's parent"""

    id: str
    r"""The id of the parent asset that the asset belongs to."""
    name: str
    r"""The name of the asset."""


class AssetResponseParentAsset(BaseModel):
    r"""The asset's parent"""

    id: str
    r"""The id of the parent asset that the asset belongs to."""

    name: str
    r"""The name of the asset."""
