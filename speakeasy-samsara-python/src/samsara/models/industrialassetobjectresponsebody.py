"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class IndustrialAssetObjectResponseBodyTypedDict(TypedDict):
    r"""industrialAssetObject"""

    id: str
    r"""Id of the device"""
    name: str
    r"""Name of the industrial asset"""


class IndustrialAssetObjectResponseBody(BaseModel):
    r"""industrialAssetObject"""

    id: str
    r"""Id of the device"""

    name: str
    r"""Name of the industrial asset"""
