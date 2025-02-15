"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import List
from typing_extensions import Annotated, TypedDict


class DaysOfWeek(str, Enum):
    r"""The day of the week.  Valid values: `FRIDAY`, `MONDAY`, `SATURDAY`, `SUNDAY`, `THURSDAY`, `TUESDAY`, `WEDNESDAY`"""

    FRIDAY = "FRIDAY"
    MONDAY = "MONDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"
    THURSDAY = "THURSDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"


class TimeRangeObjectResponseBodyTypedDict(TypedDict):
    r"""A daily time range. If start time of day is greater than end time of day, then the time range applies overnight from the specified day of week into the following day."""

    days_of_week: List[DaysOfWeek]
    r"""Which days this timezone applies to."""
    end_time: str
    r"""The time of day at which the time range starts. In 24 hour kitchen clock format."""
    start_time: str
    r"""The time of day at which the time range starts. In 24 hour kitchen clock format."""
    timezone: str
    r"""The timezone of the time range uses [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html)."""


class TimeRangeObjectResponseBody(BaseModel):
    r"""A daily time range. If start time of day is greater than end time of day, then the time range applies overnight from the specified day of week into the following day."""

    days_of_week: Annotated[List[DaysOfWeek], pydantic.Field(alias="daysOfWeek")]
    r"""Which days this timezone applies to."""

    end_time: Annotated[str, pydantic.Field(alias="endTime")]
    r"""The time of day at which the time range starts. In 24 hour kitchen clock format."""

    start_time: Annotated[str, pydantic.Field(alias="startTime")]
    r"""The time of day at which the time range starts. In 24 hour kitchen clock format."""

    timezone: str
    r"""The timezone of the time range uses [IANA timezone database](https://www.iana.org/time-zones) keys (e.g. `America/Los_Angeles`, `America/New_York`, `Europe/London`, etc.). You can find a mapping of common timezone formats to IANA timezone keys [here](https://unicode.org/cldr/charts/latest/supplemental/zone_tzid.html)."""
