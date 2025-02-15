"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class EquipmentEngineRpmTypedDict(TypedDict):
    r"""Engine RPM reading."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""
    value: int
    r"""The revolutions per minute of the engine."""


class EquipmentEngineRpm(BaseModel):
    r"""Engine RPM reading."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""

    value: int
    r"""The revolutions per minute of the engine."""
