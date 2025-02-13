"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ParentTagTypedDict(TypedDict):
    r"""If this tag is part a hierarchical tag tree, this is the parent tag, otherwise this will be omitted."""

    id: str
    r"""The object ID."""
    name: NotRequired[str]
    r"""The tag name."""


class ParentTag(BaseModel):
    r"""If this tag is part a hierarchical tag tree, this is the parent tag, otherwise this will be omitted."""

    id: str
    r"""The object ID."""

    name: Optional[str] = None
    r"""The tag name."""
