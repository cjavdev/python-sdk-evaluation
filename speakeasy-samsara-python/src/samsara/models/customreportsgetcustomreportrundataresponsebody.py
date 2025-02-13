"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .getcustomreportrundataobjectresponsebody import (
    GetCustomReportRunDataObjectResponseBody,
    GetCustomReportRunDataObjectResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class CustomReportsGetCustomReportRunDataResponseBodyTypedDict(TypedDict):
    data: GetCustomReportRunDataObjectResponseBodyTypedDict
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class CustomReportsGetCustomReportRunDataResponseBody(BaseModel):
    data: GetCustomReportRunDataObjectResponseBody

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
