"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .speedingintervallocationresponseresponsebody import (
    SpeedingIntervalLocationResponseResponseBody,
    SpeedingIntervalLocationResponseResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class SpeedingIntervalResponseBodySeverityLevel(str, Enum):
    r"""Specifies the severity level of the speeding interval.  Valid values: `light`, `moderate`, `heavy`, `severe`"""

    LIGHT = "light"
    MODERATE = "moderate"
    HEAVY = "heavy"
    SEVERE = "severe"


class SpeedingIntervalResponseBodyTypedDict(TypedDict):
    r"""Speeding Interval Object"""

    end_time: str
    r"""UTC time the interval ended in RFC 3339 format."""
    is_dismissed: bool
    r"""Whether the interval is dismissed."""
    location: SpeedingIntervalLocationResponseResponseBodyTypedDict
    r"""Location object of the closest location point to the interval."""
    max_speed_kilometers_per_hour: float
    r"""The max speed exceeded for the speeding interval."""
    posted_speed_limit_kilometers_per_hour: float
    r"""The posted speed limit associated with the speeding interval."""
    severity_level: SpeedingIntervalResponseBodySeverityLevel
    r"""Specifies the severity level of the speeding interval.  Valid values: `light`, `moderate`, `heavy`, `severe`"""
    start_time: str
    r"""UTC time the interval started in RFC 3339 format."""


class SpeedingIntervalResponseBody(BaseModel):
    r"""Speeding Interval Object"""

    end_time: Annotated[str, pydantic.Field(alias="endTime")]
    r"""UTC time the interval ended in RFC 3339 format."""

    is_dismissed: Annotated[bool, pydantic.Field(alias="isDismissed")]
    r"""Whether the interval is dismissed."""

    location: SpeedingIntervalLocationResponseResponseBody
    r"""Location object of the closest location point to the interval."""

    max_speed_kilometers_per_hour: Annotated[
        float, pydantic.Field(alias="maxSpeedKilometersPerHour")
    ]
    r"""The max speed exceeded for the speeding interval."""

    posted_speed_limit_kilometers_per_hour: Annotated[
        float, pydantic.Field(alias="postedSpeedLimitKilometersPerHour")
    ]
    r"""The posted speed limit associated with the speeding interval."""

    severity_level: Annotated[
        SpeedingIntervalResponseBodySeverityLevel, pydantic.Field(alias="severityLevel")
    ]
    r"""Specifies the severity level of the speeding interval.  Valid values: `light`, `moderate`, `heavy`, `severe`"""

    start_time: Annotated[str, pydantic.Field(alias="startTime")]
    r"""UTC time the interval started in RFC 3339 format."""
