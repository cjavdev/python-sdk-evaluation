"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from samsara.types import BaseModel
from typing_extensions import TypedDict


class Value(str, Enum):
    r"""The door state of zone 2 of the reefer.  Valid values: `open`, `closed`"""

    OPEN = "open"
    CLOSED = "closed"


class TrailerStatReeferDoorStateZone1TypeResponseBodyTypedDict(TypedDict):
    r"""The door state of the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""
    value: Value
    r"""The door state of zone 2 of the reefer.  Valid values: `open`, `closed`"""


class TrailerStatReeferDoorStateZone1TypeResponseBody(BaseModel):
    r"""The door state of the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    value: Value
    r"""The door state of zone 2 of the reefer.  Valid values: `open`, `closed`"""
