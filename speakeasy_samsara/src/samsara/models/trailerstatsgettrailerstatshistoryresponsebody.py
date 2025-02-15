"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from .trailerstatsobjectresponsebody import (
    TrailerStatsObjectResponseBody,
    TrailerStatsObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class TrailerStatsGetTrailerStatsHistoryResponseBodyTypedDict(TypedDict):
    data: List[TrailerStatsObjectResponseBodyTypedDict]
    r"""List of trailers and their stats"""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class TrailerStatsGetTrailerStatsHistoryResponseBody(BaseModel):
    data: List[TrailerStatsObjectResponseBody]
    r"""List of trailers and their stats"""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
