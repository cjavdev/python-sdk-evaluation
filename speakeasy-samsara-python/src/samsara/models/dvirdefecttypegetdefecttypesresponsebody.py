"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .defecttypesresponsedataresponsebody import (
    DefectTypesResponseDataResponseBody,
    DefectTypesResponseDataResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class DvirDefectTypeGetDefectTypesResponseBodyTypedDict(TypedDict):
    data: List[DefectTypesResponseDataResponseBodyTypedDict]
    r"""List of defect types."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class DvirDefectTypeGetDefectTypesResponseBody(BaseModel):
    data: List[DefectTypesResponseDataResponseBody]
    r"""List of defect types."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
