"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PatchDriverTrailerAssignmentsResponseBodyResponseBodyTypedDict(TypedDict):
    r"""Response after successfully updating a Driver Trailer Assignment"""

    driver_id: str
    r"""Samsara ID for the driver that this assignment is for."""
    end_time: str
    r"""Time when the driver trailer assignment ends, in RFC 3339 format"""
    id: str
    r"""Samsara ID for the assignment."""
    start_time: str
    r"""Time when the driver trailer assignment starts, in RFC 3339 format"""
    trailer_id: str
    r"""Samsara ID of the trailer"""
    created_at_time: NotRequired[str]
    r"""Time when the driver trailer assignment was created, in RFC 3339 format"""
    updated_at_time: NotRequired[str]
    r"""Time when the driver trailer assignment was last updated, in RFC 3339 format"""


class PatchDriverTrailerAssignmentsResponseBodyResponseBody(BaseModel):
    r"""Response after successfully updating a Driver Trailer Assignment"""

    driver_id: Annotated[str, pydantic.Field(alias="driverId")]
    r"""Samsara ID for the driver that this assignment is for."""

    end_time: Annotated[str, pydantic.Field(alias="endTime")]
    r"""Time when the driver trailer assignment ends, in RFC 3339 format"""

    id: str
    r"""Samsara ID for the assignment."""

    start_time: Annotated[str, pydantic.Field(alias="startTime")]
    r"""Time when the driver trailer assignment starts, in RFC 3339 format"""

    trailer_id: Annotated[str, pydantic.Field(alias="trailerId")]
    r"""Samsara ID of the trailer"""

    created_at_time: Annotated[Optional[str], pydantic.Field(alias="createdAtTime")] = (
        None
    )
    r"""Time when the driver trailer assignment was created, in RFC 3339 format"""

    updated_at_time: Annotated[Optional[str], pydantic.Field(alias="updatedAtTime")] = (
        None
    )
    r"""Time when the driver trailer assignment was last updated, in RFC 3339 format"""
