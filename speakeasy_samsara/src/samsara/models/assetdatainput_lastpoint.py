"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class AssetDataInputLastPointTypedDict(TypedDict):
    r"""The last reported point of a data input."""

    time: NotRequired[str]
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: NotRequired[float]
    r"""Numeric value of the data point."""


class AssetDataInputLastPoint(BaseModel):
    r"""The last reported point of a data input."""

    time: Optional[str] = None
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: Optional[float] = None
    r"""Numeric value of the data point."""
