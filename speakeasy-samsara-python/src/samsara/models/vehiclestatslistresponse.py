"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from .vehiclestatslistresponse_data import (
    VehicleStatsListResponseData,
    VehicleStatsListResponseDataTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class VehicleStatsListResponseTypedDict(TypedDict):
    r"""List of vehicle stat events and pagination info."""

    data: List[VehicleStatsListResponseDataTypedDict]
    r"""A list of vehicles and an array of stat events for each vehicle."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class VehicleStatsListResponse(BaseModel):
    r"""List of vehicle stat events and pagination info."""

    data: List[VehicleStatsListResponseData]
    r"""A list of vehicles and an array of stat events for each vehicle."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
