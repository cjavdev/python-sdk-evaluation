"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class TrailersUpdateTrailerBadRequestErrorResponseBodyTypedDict(TypedDict):
    r"""Bad Request parameters"""

    message: str
    r"""Message of error"""
    request_id: str
    r"""The request ID; used when reaching out to support for issues with requests."""


class TrailersUpdateTrailerBadRequestErrorResponseBody(BaseModel):
    r"""Bad Request parameters"""

    message: str
    r"""Message of error"""

    request_id: Annotated[str, pydantic.Field(alias="requestId")]
    r"""The request ID; used when reaching out to support for issues with requests."""
