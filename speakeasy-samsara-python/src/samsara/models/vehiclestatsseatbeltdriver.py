"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsSeatbeltDriverValue(str, Enum):
    r"""Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""

    BUCKLED = "Buckled"
    UNBUCKLED = "Unbuckled"


class VehicleStatsSeatbeltDriverTypedDict(TypedDict):
    r"""Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""
    value: VehicleStatsSeatbeltDriverValue
    r"""Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""


class VehicleStatsSeatbeltDriver(BaseModel):
    r"""Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""

    time: str
    r"""UTC timestamp in RFC 3339 format. Example: `2020-01-27T07:06:25Z`."""

    value: VehicleStatsSeatbeltDriverValue
    r"""Seatbelt Driver Status as read from the vehicle. `Buckled` or `Unbuckled`."""
