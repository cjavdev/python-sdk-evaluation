"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .dvir import Dvir, DvirTypedDict
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DvirResponseTypedDict(TypedDict):
    r"""The DVIR response."""

    data: NotRequired[DvirTypedDict]
    r"""Information about a DVIR."""


class DvirResponse(BaseModel):
    r"""The DVIR response."""

    data: Optional[Dvir] = None
    r"""Information about a DVIR."""
