"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class HosDriveTypedDict(TypedDict):
    r"""Remaining durations for the HOS driving shift limits."""

    drive_remaining_duration_ms: NotRequired[float]
    r"""Remaining driving time the driver has in the current shift in milliseconds. For property-carrying drivers, this is the amount of time the driver can drive before hitting the 11-hour limit."""


class HosDrive(BaseModel):
    r"""Remaining durations for the HOS driving shift limits."""

    drive_remaining_duration_ms: Annotated[
        Optional[float], pydantic.Field(alias="driveRemainingDurationMs")
    ] = None
    r"""Remaining driving time the driver has in the current shift in milliseconds. For property-carrying drivers, this is the amount of time the driver can drive before hitting the 11-hour limit."""
