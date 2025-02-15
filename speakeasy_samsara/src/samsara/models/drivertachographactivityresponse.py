"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from .tachographactivitylistwrapper import (
    TachographActivityListWrapper,
    TachographActivityListWrapperTypedDict,
)
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class DriverTachographActivityResponseTypedDict(TypedDict):
    r"""List of all driver tachograph activities in a specified time range."""

    data: NotRequired[List[TachographActivityListWrapperTypedDict]]
    pagination: NotRequired[PaginationResponseTypedDict]
    r"""Pagination parameters."""


class DriverTachographActivityResponse(BaseModel):
    r"""List of all driver tachograph activities in a specified time range."""

    data: Optional[List[TachographActivityListWrapper]] = None

    pagination: Optional[PaginationResponse] = None
    r"""Pagination parameters."""
