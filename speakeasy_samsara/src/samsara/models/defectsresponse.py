"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .defect import Defect, DefectTypedDict
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DefectsResponseTypedDict(TypedDict):
    r"""A list of defects."""

    data: NotRequired[List[DefectTypedDict]]
    pagination: NotRequired[PaginationResponseTypedDict]
    r"""Pagination parameters."""


class DefectsResponse(BaseModel):
    r"""A list of defects."""

    data: Optional[List[Defect]] = None

    pagination: Optional[PaginationResponse] = None
    r"""Pagination parameters."""
