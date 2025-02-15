"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class LocationType(str, Enum):
    r"""The format of the location. This field is required if a location is provided. Valid values: `point`, `address`, `dataInput`."""

    POINT = "point"
    ADDRESS = "address"
    DATA_INPUT = "dataInput"
