"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentresponseobjectresponsebody import (
    DocumentResponseObjectResponseBody,
    DocumentResponseObjectResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class DocumentsGetDocumentsResponseBodyTypedDict(TypedDict):
    data: List[DocumentResponseObjectResponseBodyTypedDict]
    r"""Multiple documents."""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class DocumentsGetDocumentsResponseBody(BaseModel):
    data: List[DocumentResponseObjectResponseBody]
    r"""Multiple documents."""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
