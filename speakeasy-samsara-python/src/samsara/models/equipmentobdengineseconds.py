"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class EquipmentObdEngineSecondsTypedDict(TypedDict):
    r"""Engine seconds reading from on-board diagnostics."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""
    value: int
    r"""The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics."""


class EquipmentObdEngineSeconds(BaseModel):
    r"""Engine seconds reading from on-board diagnostics."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""

    value: int
    r"""The number of seconds the engine has been running since it was new. This value is provided directly from on-board diagnostics."""
