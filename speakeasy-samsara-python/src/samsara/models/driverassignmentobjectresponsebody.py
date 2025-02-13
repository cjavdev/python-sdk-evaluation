"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goadrivertinyresponseresponsebody import (
    GoaDriverTinyResponseResponseBody,
    GoaDriverTinyResponseResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DriverAssignmentObjectResponseBodyAssignmentType(str, Enum):
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""

    DRIVER_APP = "driverApp"


class DriverAssignmentObjectResponseBodyTypedDict(TypedDict):
    assignment_type: NotRequired[DriverAssignmentObjectResponseBodyAssignmentType]
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""
    driver: NotRequired[GoaDriverTinyResponseResponseBodyTypedDict]
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""
    end_time: NotRequired[str]
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    is_passenger: NotRequired[bool]
    r"""Boolean indicating whether the driver is a passenger."""
    start_time: NotRequired[str]
    r"""A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""


class DriverAssignmentObjectResponseBody(BaseModel):
    assignment_type: Annotated[
        Optional[DriverAssignmentObjectResponseBodyAssignmentType],
        pydantic.Field(alias="assignmentType"),
    ] = None
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""

    driver: Optional[GoaDriverTinyResponseResponseBody] = None
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""

    end_time: Annotated[Optional[str], pydantic.Field(alias="endTime")] = None
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    is_passenger: Annotated[Optional[bool], pydantic.Field(alias="isPassenger")] = None
    r"""Boolean indicating whether the driver is a passenger."""

    start_time: Annotated[Optional[str], pydantic.Field(alias="startTime")] = None
    r"""A start time in RFC 3339 format. Defaults to now if not provided. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
