"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .documentresponseobjectresponsebody import (
    DocumentResponseObjectResponseBody,
    DocumentResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DocumentsGetDocumentResponseBodyTypedDict(TypedDict):
    data: NotRequired[DocumentResponseObjectResponseBodyTypedDict]
    r"""A single document."""


class DocumentsGetDocumentResponseBody(BaseModel):
    data: Optional[DocumentResponseObjectResponseBody] = None
    r"""A single document."""
