"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from .listuploadedmediaobjectresponsebody import (
    ListUploadedMediaObjectResponseBody,
    ListUploadedMediaObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class MediaRetrievalListUploadedMediaResponseBodyTypedDict(TypedDict):
    data: ListUploadedMediaObjectResponseBodyTypedDict
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class MediaRetrievalListUploadedMediaResponseBody(BaseModel):
    data: ListUploadedMediaObjectResponseBody

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
