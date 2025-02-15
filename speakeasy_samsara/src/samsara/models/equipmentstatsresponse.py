"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipmentstatsresponse_data import (
    EquipmentStatsResponseData,
    EquipmentStatsResponseDataTypedDict,
)
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class EquipmentStatsResponseTypedDict(TypedDict):
    r"""The most recent equipment stats and pagination information"""

    data: List[EquipmentStatsResponseDataTypedDict]
    r"""List of the most recent stats for the specified units of equipment and stat types."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class EquipmentStatsResponse(BaseModel):
    r"""The most recent equipment stats and pagination information"""

    data: List[EquipmentStatsResponseData]
    r"""List of the most recent stats for the specified units of equipment and stat types."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
