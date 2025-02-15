"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsDecorationsDefLevelMilliPercentTypedDict(TypedDict):
    value: int
    r"""The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc)."""


class VehicleStatsDecorationsDefLevelMilliPercent(BaseModel):
    value: int
    r"""The Diesel Exhaust Fluid (DEF) level in milli percentage points (e.g. `99001`, `49999`, etc)."""
