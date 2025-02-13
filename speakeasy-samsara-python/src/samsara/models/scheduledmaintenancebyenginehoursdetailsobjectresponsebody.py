"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing_extensions import Annotated, TypedDict


class ScheduledMaintenanceByEngineHoursDetailsObjectResponseBodyTypedDict(TypedDict):
    r"""Details specific to Scheduled Maintenance By Engine Hours"""

    due_in_hours: int
    r"""Alert when maintenance is due in the specified number of hours."""
    schedule_id: str
    r"""The id of the maintenance schedule."""


class ScheduledMaintenanceByEngineHoursDetailsObjectResponseBody(BaseModel):
    r"""Details specific to Scheduled Maintenance By Engine Hours"""

    due_in_hours: Annotated[int, pydantic.Field(alias="dueInHours")]
    r"""Alert when maintenance is due in the specified number of hours."""

    schedule_id: Annotated[str, pydantic.Field(alias="scheduleId")]
    r"""The id of the maintenance schedule."""
