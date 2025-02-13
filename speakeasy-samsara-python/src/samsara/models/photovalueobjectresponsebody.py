"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class PhotoValueObjectResponseBodyTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Id of the photo."""
    url: NotRequired[str]
    r"""Url of the photo."""


class PhotoValueObjectResponseBody(BaseModel):
    id: Optional[str] = None
    r"""Id of the photo."""

    url: Optional[str] = None
    r"""Url of the photo."""
