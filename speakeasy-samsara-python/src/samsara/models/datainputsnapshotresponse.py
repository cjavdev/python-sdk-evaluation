"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .datainputsnapshot import DataInputSnapshot, DataInputSnapshotTypedDict
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DataInputSnapshotResponseTypedDict(TypedDict):
    data: NotRequired[List[DataInputSnapshotTypedDict]]
    r"""An array of data inputs' latest data points. Each object in the array represents a data input and its most recent data point."""
    pagination: NotRequired[PaginationResponseTypedDict]
    r"""Pagination parameters."""


class DataInputSnapshotResponse(BaseModel):
    data: Optional[List[DataInputSnapshot]] = None
    r"""An array of data inputs' latest data points. Each object in the array represents a data input and its most recent data point."""

    pagination: Optional[PaginationResponse] = None
    r"""Pagination parameters."""
