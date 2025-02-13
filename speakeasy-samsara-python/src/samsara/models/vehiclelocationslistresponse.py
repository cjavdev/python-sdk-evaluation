"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from .vehiclelocationslistresponse_data import (
    VehicleLocationsListResponseData,
    VehicleLocationsListResponseDataTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class VehicleLocationsListResponseTypedDict(TypedDict):
    r"""List of vehicle location events and pagination info."""

    data: List[VehicleLocationsListResponseDataTypedDict]
    r"""A list of vehicles and an array of location events for each vehicle."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class VehicleLocationsListResponse(BaseModel):
    r"""List of vehicle location events and pagination info."""

    data: List[VehicleLocationsListResponseData]
    r"""A list of vehicles and an array of location events for each vehicle."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
