"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipmentlocationslistresponse_data import (
    EquipmentLocationsListResponseData,
    EquipmentLocationsListResponseDataTypedDict,
)
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class EquipmentLocationsListResponseTypedDict(TypedDict):
    r"""A time-series of equipment locations and pagination information"""

    data: List[EquipmentLocationsListResponseDataTypedDict]
    r"""Time-series of locations for the specified units of equipment."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class EquipmentLocationsListResponse(BaseModel):
    r"""A time-series of equipment locations and pagination information"""

    data: List[EquipmentLocationsListResponseData]
    r"""Time-series of locations for the specified units of equipment."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
