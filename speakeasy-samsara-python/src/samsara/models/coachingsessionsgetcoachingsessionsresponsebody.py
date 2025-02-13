"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .coachingsessionsresponseresponsebody import (
    CoachingSessionsResponseResponseBody,
    CoachingSessionsResponseResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class CoachingSessionsGetCoachingSessionsResponseBodyTypedDict(TypedDict):
    data: List[CoachingSessionsResponseResponseBodyTypedDict]
    r"""List of coaching sessions objects."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class CoachingSessionsGetCoachingSessionsResponseBody(BaseModel):
    data: List[CoachingSessionsResponseResponseBody]
    r"""List of coaching sessions objects."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
