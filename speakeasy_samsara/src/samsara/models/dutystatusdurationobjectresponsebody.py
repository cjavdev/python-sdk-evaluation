"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DutyStatusDurationObjectResponseBodyTypedDict(TypedDict):
    r"""The currently applied duty status durations on the driver's log."""

    active_duration_ms: NotRequired[int]
    r"""Duration the driver was active for in the log period in milliseconds."""
    drive_duration_ms: NotRequired[int]
    r"""Duration the driver was driving for in the log period in milliseconds."""
    off_duty_duration_ms: NotRequired[int]
    r"""Duration the driver was off duty for in the log period in milliseconds."""
    on_duty_duration_ms: NotRequired[int]
    r"""Duration the driver was on duty for in the log period in milliseconds."""
    personal_conveyance_duration_ms: NotRequired[int]
    r"""Duration the driver was driving for personal conveyance for in the log period in milliseconds."""
    sleeper_berth_duration_ms: NotRequired[int]
    r"""Duration the driver was in their sleeper berth for in the log period in milliseconds."""
    waiting_time_duration_ms: NotRequired[int]
    r"""Duration the driver was waiting for in the log period in milliseconds."""
    yard_move_duration_ms: NotRequired[int]
    r"""Duration the driver was driving for yard moves for in the log period in milliseconds."""


class DutyStatusDurationObjectResponseBody(BaseModel):
    r"""The currently applied duty status durations on the driver's log."""

    active_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="activeDurationMs")
    ] = None
    r"""Duration the driver was active for in the log period in milliseconds."""

    drive_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="driveDurationMs")
    ] = None
    r"""Duration the driver was driving for in the log period in milliseconds."""

    off_duty_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="offDutyDurationMs")
    ] = None
    r"""Duration the driver was off duty for in the log period in milliseconds."""

    on_duty_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="onDutyDurationMs")
    ] = None
    r"""Duration the driver was on duty for in the log period in milliseconds."""

    personal_conveyance_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="personalConveyanceDurationMs")
    ] = None
    r"""Duration the driver was driving for personal conveyance for in the log period in milliseconds."""

    sleeper_berth_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="sleeperBerthDurationMs")
    ] = None
    r"""Duration the driver was in their sleeper berth for in the log period in milliseconds."""

    waiting_time_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="waitingTimeDurationMs")
    ] = None
    r"""Duration the driver was waiting for in the log period in milliseconds."""

    yard_move_duration_ms: Annotated[
        Optional[int], pydantic.Field(alias="yardMoveDurationMs")
    ] = None
    r"""Duration the driver was driving for yard moves for in the log period in milliseconds."""
