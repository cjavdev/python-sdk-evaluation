"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from .tripresponsebody import TripResponseBody, TripResponseBodyTypedDict
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class TripsGetTripsResponseBodyTypedDict(TypedDict):
    data: List[TripResponseBodyTypedDict]
    r"""List of trips"""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class TripsGetTripsResponseBody(BaseModel):
    data: List[TripResponseBody]
    r"""List of trips"""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
