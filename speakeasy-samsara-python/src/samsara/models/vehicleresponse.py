"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .vehicle import Vehicle, VehicleTypedDict
from samsara.types import BaseModel
from typing_extensions import TypedDict


class VehicleResponseTypedDict(TypedDict):
    r"""A single vehicle."""

    data: VehicleTypedDict
    r"""The vehicle object."""


class VehicleResponse(BaseModel):
    r"""A single vehicle."""

    data: Vehicle
    r"""The vehicle object."""
