"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsResponseSpreaderBlastStateValue(str, Enum):
    r"""Whether vehicle is actively spreading material in ‘blast mode’."""

    ON = "On"
    OFF = "Off"


class VehicleStatsResponseSpreaderBlastStateTypedDict(TypedDict):
    r"""Whether vehicle is actively spreading material in ‘blast mode’."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: VehicleStatsResponseSpreaderBlastStateValue
    r"""Whether vehicle is actively spreading material in ‘blast mode’."""


class VehicleStatsResponseSpreaderBlastState(BaseModel):
    r"""Whether vehicle is actively spreading material in ‘blast mode’."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: VehicleStatsResponseSpreaderBlastStateValue
    r"""Whether vehicle is actively spreading material in ‘blast mode’."""
