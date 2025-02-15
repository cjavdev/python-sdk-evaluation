"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class InlineObject8TypedDict(TypedDict):
    sensors: List[int]
    r"""List of sensor IDs to query."""


class InlineObject8(BaseModel):
    sensors: List[int]
    r"""List of sensor IDs to query."""
