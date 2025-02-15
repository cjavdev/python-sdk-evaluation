"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from .jobresponseobjectresponsebody import (
    JobResponseObjectResponseBody,
    JobResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class JobsGetJobsResponseBodyTypedDict(TypedDict):
    data: List[JobResponseObjectResponseBodyTypedDict]
    r"""List of Job Objects"""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""
    id: NotRequired[str]
    r"""The job id of the failed request"""
    uuid: NotRequired[str]
    r"""The uuid of the failed request"""


class JobsGetJobsResponseBody(BaseModel):
    data: List[JobResponseObjectResponseBody]
    r"""List of Job Objects"""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""

    id: Optional[str] = None
    r"""The job id of the failed request"""

    uuid: Optional[str] = None
    r"""The uuid of the failed request"""
