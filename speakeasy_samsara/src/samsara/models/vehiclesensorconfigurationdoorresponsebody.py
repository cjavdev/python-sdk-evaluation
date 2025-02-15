"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .sensorresponsebody import SensorResponseBody, SensorResponseBodyTypedDict
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleSensorConfigurationDoorResponseBodyPosition(str, Enum):
    r"""Position of the door monitor on the vehicle  Valid values: `back`, `left`, `right`"""

    BACK = "back"
    LEFT = "left"
    RIGHT = "right"


class VehicleSensorConfigurationDoorResponseBodyTypedDict(TypedDict):
    r"""A door monitor configuration on a vehicle"""

    position: VehicleSensorConfigurationDoorResponseBodyPosition
    r"""Position of the door monitor on the vehicle  Valid values: `back`, `left`, `right`"""
    sensor: SensorResponseBodyTypedDict
    r"""A sensor"""


class VehicleSensorConfigurationDoorResponseBody(BaseModel):
    r"""A door monitor configuration on a vehicle"""

    position: VehicleSensorConfigurationDoorResponseBodyPosition
    r"""Position of the door monitor on the vehicle  Valid values: `back`, `left`, `right`"""

    sensor: SensorResponseBody
    r"""A sensor"""
