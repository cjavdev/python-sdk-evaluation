"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .timerangeobjectresponsebody import (
    TimeRangeObjectResponseBody,
    TimeRangeObjectResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List
from typing_extensions import Annotated, TypedDict


class TimeRangeType(str, Enum):
    r"""The type of time ranges.  Valid values: `activeBetween`, `inactiveBetween`"""

    ACTIVE_BETWEEN = "activeBetween"
    INACTIVE_BETWEEN = "inactiveBetween"


class OperationalSettingsObjectResponseBodyTypedDict(TypedDict):
    r"""Settings on when the alert should be operational."""

    time_range_type: TimeRangeType
    r"""The type of time ranges.  Valid values: `activeBetween`, `inactiveBetween`"""
    time_ranges: List[TimeRangeObjectResponseBodyTypedDict]
    r"""The time ranges this alert applies to."""


class OperationalSettingsObjectResponseBody(BaseModel):
    r"""Settings on when the alert should be operational."""

    time_range_type: Annotated[TimeRangeType, pydantic.Field(alias="timeRangeType")]
    r"""The type of time ranges.  Valid values: `activeBetween`, `inactiveBetween`"""

    time_ranges: Annotated[
        List[TimeRangeObjectResponseBody], pydantic.Field(alias="timeRanges")
    ]
    r"""The time ranges this alert applies to."""
