"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .trailerstatdecorationresponsebody import (
    TrailerStatDecorationResponseBody,
    TrailerStatDecorationResponseBodyTypedDict,
)
from .trailerstatreeferalarmresponsebody import (
    TrailerStatReeferAlarmResponseBody,
    TrailerStatReeferAlarmResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TrailerStatReeferAlarmWithDecorationsTypeResponseBodyTypedDict(TypedDict):
    r"""Alarms that have been emitted by the reefer."""

    alarms: List[TrailerStatReeferAlarmResponseBodyTypedDict]
    r"""The alarms reported by the reefer."""
    time: str
    r"""UTC timestamp in RFC 3339 format."""
    decorations: NotRequired[TrailerStatDecorationResponseBodyTypedDict]
    r"""Decorated values for the primary trailer stat datapoints."""


class TrailerStatReeferAlarmWithDecorationsTypeResponseBody(BaseModel):
    r"""Alarms that have been emitted by the reefer."""

    alarms: List[TrailerStatReeferAlarmResponseBody]
    r"""The alarms reported by the reefer."""

    time: str
    r"""UTC timestamp in RFC 3339 format."""

    decorations: Optional[TrailerStatDecorationResponseBody] = None
    r"""Decorated values for the primary trailer stat datapoints."""
