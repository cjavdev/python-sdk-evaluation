"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsDecorationsObdOdometerMetersTypedDict(TypedDict):
    value: int
    r"""Number of meters the vehicle has traveled according to the on-board diagnostics."""


class VehicleStatsDecorationsObdOdometerMeters(BaseModel):
    value: int
    r"""Number of meters the vehicle has traveled according to the on-board diagnostics."""
