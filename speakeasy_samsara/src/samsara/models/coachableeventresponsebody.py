"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class CoachableEventResponseBodyTypedDict(TypedDict):
    r"""Object reference for the coachable event within the behavior."""

    id: str
    r"""Unique ID for an event within the item in a coaching session."""


class CoachableEventResponseBody(BaseModel):
    r"""Object reference for the coachable event within the behavior."""

    id: str
    r"""Unique ID for an event within the item in a coaching session."""
