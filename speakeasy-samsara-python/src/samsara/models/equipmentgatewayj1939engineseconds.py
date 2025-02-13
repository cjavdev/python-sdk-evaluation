"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing_extensions import TypedDict


class EquipmentGatewayJ1939EngineSecondsTypedDict(TypedDict):
    r"""Engine seconds reading from the J1939/CAT cable."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""
    value: int
    r"""An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power and an offset provided manually through the Samsara cloud dashboard."""


class EquipmentGatewayJ1939EngineSeconds(BaseModel):
    r"""Engine seconds reading from the J1939/CAT cable."""

    time: str
    r"""UTC timestamp of the time the data point was generated by the equipment, in RFC3339 format."""

    value: int
    r"""An approximation of the number of seconds the engine has been running since it was new, based on the amount of time the AG26 device is receiving power and an offset provided manually through the Samsara cloud dashboard."""
