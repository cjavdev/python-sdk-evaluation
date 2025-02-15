"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from .vehiclestatsresponse_data import (
    VehicleStatsResponseData,
    VehicleStatsResponseDataTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class VehicleStatsResponseTypedDict(TypedDict):
    r"""Vehicle stats snapshot and pagination info."""

    data: List[VehicleStatsResponseDataTypedDict]
    r"""List of vehicles and a snapshot of the request stats."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class VehicleStatsResponse(BaseModel):
    r"""Vehicle stats snapshot and pagination info."""

    data: List[VehicleStatsResponseData]
    r"""List of vehicles and a snapshot of the request stats."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
