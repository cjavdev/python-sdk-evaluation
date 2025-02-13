"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SeverityLevel(str, Enum):
    r"""The severity level name.  Valid values: `light`, `moderate`, `heavy`, `severe`"""

    LIGHT = "light"
    MODERATE = "moderate"
    HEAVY = "heavy"
    SEVERE = "severe"


class SpeedingSeverityLevelResponseBodyTypedDict(TypedDict):
    r"""The settings for a specific speeding severity level."""

    duration_ms: int
    r"""The amount of time the vehicle is speeding in this category before being attributed to this level"""
    severity_level: SeverityLevel
    r"""The severity level name.  Valid values: `light`, `moderate`, `heavy`, `severe`"""
    speed_over_limit_threshold: float
    r"""The minimum speed above the speed limit that will get attributed to this severity level."""
    is_enabled: NotRequired[bool]
    r"""Indicates the severity level is enabled"""


class SpeedingSeverityLevelResponseBody(BaseModel):
    r"""The settings for a specific speeding severity level."""

    duration_ms: Annotated[int, pydantic.Field(alias="durationMs")]
    r"""The amount of time the vehicle is speeding in this category before being attributed to this level"""

    severity_level: Annotated[SeverityLevel, pydantic.Field(alias="severityLevel")]
    r"""The severity level name.  Valid values: `light`, `moderate`, `heavy`, `severe`"""

    speed_over_limit_threshold: Annotated[
        float, pydantic.Field(alias="speedOverLimitThreshold")
    ]
    r"""The minimum speed above the speed limit that will get attributed to this severity level."""

    is_enabled: Annotated[Optional[bool], pydantic.Field(alias="isEnabled")] = True
    r"""Indicates the severity level is enabled"""
