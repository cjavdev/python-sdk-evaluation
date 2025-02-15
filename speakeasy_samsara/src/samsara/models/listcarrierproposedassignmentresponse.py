"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .carrierproposedassignment import (
    CarrierProposedAssignment,
    CarrierProposedAssignmentTypedDict,
)
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class ListCarrierProposedAssignmentResponseTypedDict(TypedDict):
    r"""A list of carrier-proposed assignments and pagination information."""

    data: List[CarrierProposedAssignmentTypedDict]
    r"""A list of carrier-proposed assignments"""
    pagination: PaginationResponseTypedDict
    r"""Pagination parameters."""


class ListCarrierProposedAssignmentResponse(BaseModel):
    r"""A list of carrier-proposed assignments and pagination information."""

    data: List[CarrierProposedAssignment]
    r"""A list of carrier-proposed assignments"""

    pagination: PaginationResponse
    r"""Pagination parameters."""
