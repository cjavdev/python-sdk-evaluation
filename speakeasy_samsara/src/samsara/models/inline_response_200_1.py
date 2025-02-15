"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .v1asset import V1Asset, V1AssetTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class InlineResponse2001TypedDict(TypedDict):
    assets: NotRequired[List[V1AssetTypedDict]]


class InlineResponse2001(BaseModel):
    assets: Optional[List[V1Asset]] = None
