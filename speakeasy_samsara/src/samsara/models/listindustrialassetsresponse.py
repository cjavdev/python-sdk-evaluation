"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .assetresponse import AssetResponse, AssetResponseTypedDict
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListIndustrialAssetsResponseTypedDict(TypedDict):
    data: NotRequired[List[AssetResponseTypedDict]]
    pagination: NotRequired[PaginationResponseTypedDict]
    r"""Pagination parameters."""


class ListIndustrialAssetsResponse(BaseModel):
    data: Optional[List[AssetResponse]] = None

    pagination: Optional[PaginationResponse] = None
    r"""Pagination parameters."""
