"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleStatsDecorationsEngineRpmTypedDict(TypedDict):
    value: int
    r"""The revolutions per minute of the engine."""


class VehicleStatsDecorationsEngineRpm(BaseModel):
    value: int
    r"""The revolutions per minute of the engine."""
