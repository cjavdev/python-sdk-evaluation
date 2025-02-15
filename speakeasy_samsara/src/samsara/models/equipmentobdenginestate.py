"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class EquipmentObdEngineStateValue(str, Enum):
    r"""The state of the engine read from on-board diagnostics. Valid values: `Off`, `On`, `Idle`."""

    OFF = "Off"
    ON = "On"
    IDLE = "Idle"


class EquipmentObdEngineStateTypedDict(TypedDict):
    r"""Engine state reading from on-board diagnostics."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""
    value: EquipmentObdEngineStateValue
    r"""The state of the engine read from on-board diagnostics. Valid values: `Off`, `On`, `Idle`."""


class EquipmentObdEngineState(BaseModel):
    r"""Engine state reading from on-board diagnostics."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""

    value: EquipmentObdEngineStateValue
    r"""The state of the engine read from on-board diagnostics. Valid values: `Off`, `On`, `Idle`."""
