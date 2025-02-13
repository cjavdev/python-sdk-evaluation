"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailerstatreeferalarmresponsebody import (
    TrailerStatReeferAlarmResponseBody,
    TrailerStatReeferAlarmResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class TrailerStatReeferAlarmTypeResponseBodyTypedDict(TypedDict):
    r"""Alarms that have been emitted by the reefer."""

    alarms: List[TrailerStatReeferAlarmResponseBodyTypedDict]
    r"""The alarms reported by the reefer."""
    time: str
    r"""UTC timestamp in RFC 3339 format."""


class TrailerStatReeferAlarmTypeResponseBody(BaseModel):
    r"""Alarms that have been emitted by the reefer."""

    alarms: List[TrailerStatReeferAlarmResponseBody]
    r"""The alarms reported by the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""
