"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateDvirRequestTypedDict(TypedDict):
    r"""Information about resolving a DVIR."""

    author_id: str
    r"""The user who is resolving the dvir."""
    is_resolved: bool
    r"""Resolves the DVIR. Must be `true`."""
    mechanic_notes: NotRequired[str]
    r"""The mechanics notes on the DVIR."""
    signed_at_time: NotRequired[str]
    r"""Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""


class UpdateDvirRequest(BaseModel):
    r"""Information about resolving a DVIR."""

    author_id: Annotated[str, pydantic.Field(alias="authorId")]
    r"""The user who is resolving the dvir."""

    is_resolved: Annotated[bool, pydantic.Field(alias="isResolved")]
    r"""Resolves the DVIR. Must be `true`."""

    mechanic_notes: Annotated[Optional[str], pydantic.Field(alias="mechanicNotes")] = (
        None
    )
    r"""The mechanics notes on the DVIR."""

    signed_at_time: Annotated[Optional[str], pydantic.Field(alias="signedAtTime")] = (
        None
    )
    r"""Time when user signed this DVIR. Defaults to now. UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
