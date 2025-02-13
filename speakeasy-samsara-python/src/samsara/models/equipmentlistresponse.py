"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .equipment import Equipment, EquipmentTypedDict
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class EquipmentListResponseTypedDict(TypedDict):
    r"""List of all equipment objects, and pagination information."""

    data: List[EquipmentTypedDict]
    r"""List of equipment objects."""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class EquipmentListResponse(BaseModel):
    r"""List of all equipment objects, and pagination information."""

    data: List[Equipment]
    r"""List of equipment objects."""

    pagination: PaginationResponse
    r"""Pagination parameters."""
