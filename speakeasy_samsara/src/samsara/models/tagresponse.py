"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tag import Tag, TagTypedDict
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class TagResponseTypedDict(TypedDict):
    r"""A single tag."""

    data: NotRequired[TagTypedDict]


class TagResponse(BaseModel):
    r"""A single tag."""

    data: Optional[Tag] = None
