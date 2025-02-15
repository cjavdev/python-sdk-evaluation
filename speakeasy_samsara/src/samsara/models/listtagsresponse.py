"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .paginationresponse import PaginationResponse, PaginationResponseTypedDict
from .tag import Tag, TagTypedDict
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ListTagsResponseTypedDict(TypedDict):
    r"""A list of tags."""

    data: NotRequired[List[TagTypedDict]]
    pagination: NotRequired[PaginationResponseTypedDict]
    r"""Pagination parameters."""


class ListTagsResponse(BaseModel):
    r"""A list of tags."""

    data: Optional[List[Tag]] = None

    pagination: Optional[PaginationResponse] = None
    r"""Pagination parameters."""
