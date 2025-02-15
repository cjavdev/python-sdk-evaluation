"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectdriverresponsebody import (
    AlertObjectDriverResponseBody,
    AlertObjectDriverResponseBodyTypedDict,
)
from .alertobjectvehicleresponsebody import (
    AlertObjectVehicleResponseBody,
    AlertObjectVehicleResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class HarshEventDataResponseBodyTypedDict(TypedDict):
    r"""Details specific to Harsh Event."""

    driver: NotRequired[AlertObjectDriverResponseBodyTypedDict]
    r"""A driver associated with the alert"""
    vehicle: NotRequired[AlertObjectVehicleResponseBodyTypedDict]
    r"""The vehicle associated with the alert."""


class HarshEventDataResponseBody(BaseModel):
    r"""Details specific to Harsh Event."""

    driver: Optional[AlertObjectDriverResponseBody] = None
    r"""A driver associated with the alert"""

    vehicle: Optional[AlertObjectVehicleResponseBody] = None
    r"""The vehicle associated with the alert."""
