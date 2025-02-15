"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DriverTinyResponseTypedDict(TypedDict):
    r"""A minified driver object."""

    id: NotRequired[str]
    r"""ID of the driver."""
    name: NotRequired[str]
    r"""Name of the driver."""


class DriverTinyResponse(BaseModel):
    r"""A minified driver object."""

    id: Optional[str] = None
    r"""ID of the driver."""

    name: Optional[str] = None
    r"""Name of the driver."""
