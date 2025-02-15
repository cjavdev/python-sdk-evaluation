"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .goavehicletinyresponseresponsebody import (
    GoaVehicleTinyResponseResponseBody,
    GoaVehicleTinyResponseResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class VehicleAssignmentObjectResponseBodyAssignmentType(str, Enum):
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""

    DRIVER_APP = "driverApp"


class VehicleAssignmentObjectResponseBodyTypedDict(TypedDict):
    assignment_type: VehicleAssignmentObjectResponseBodyAssignmentType
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""
    is_passenger: bool
    r"""Boolean indicating whether the driver is a passenger."""
    start_time: str
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    vehicle: GoaVehicleTinyResponseResponseBodyTypedDict
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""
    end_time: NotRequired[str]
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""


class VehicleAssignmentObjectResponseBody(BaseModel):
    assignment_type: Annotated[
        VehicleAssignmentObjectResponseBodyAssignmentType,
        pydantic.Field(alias="assignmentType"),
    ]
    r"""Assignment type of the driver-vehicle assignment, indicating the provenance of the assignment. The only type of assignment supported right now is `driverApp` assignments. This list could change, so it is recommended that clients gracefully handle any types not enumerated in this list.  Valid values: `driverApp`"""

    is_passenger: Annotated[bool, pydantic.Field(alias="isPassenger")]
    r"""Boolean indicating whether the driver is a passenger."""

    start_time: Annotated[str, pydantic.Field(alias="startTime")]
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    vehicle: GoaVehicleTinyResponseResponseBody
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""

    end_time: Annotated[Optional[str], pydantic.Field(alias="endTime")] = None
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
