"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .driverassignmentmetadatatinyobjectresponsebody import (
    DriverAssignmentMetadataTinyObjectResponseBody,
    DriverAssignmentMetadataTinyObjectResponseBodyTypedDict,
)
from .goadrivertinyresponseresponsebody import (
    GoaDriverTinyResponseResponseBody,
    GoaDriverTinyResponseResponseBodyTypedDict,
)
from .goavehicletinyresponseresponsebody import (
    GoaVehicleTinyResponseResponseBody,
    GoaVehicleTinyResponseResponseBodyTypedDict,
)
from enum import Enum
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AssignmentType(str, Enum):
    r"""Name of the assigning source for the driver assignment record.  Valid values: `invalid`, `unknown`, `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`"""

    INVALID = "invalid"
    UNKNOWN = "unknown"
    HOS = "HOS"
    ID_CARD = "idCard"
    STATIC = "static"
    FACE_ID = "faceId"
    TACHOGRAPH = "tachograph"
    SAFETY_MANUAL = "safetyManual"
    RFID = "RFID"
    TRAILER = "trailer"
    EXTERNAL = "external"
    QR_CODE = "qrCode"


class DriverVehicleAssignmentV2ObjectResponseBodyTypedDict(TypedDict):
    r"""Object with driver assignment info and associated driver and vehicle info."""

    driver: GoaDriverTinyResponseResponseBodyTypedDict
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""
    is_passenger: bool
    r"""Boolean indicating whether the driver is a passenger."""
    start_time: str
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    vehicle: GoaVehicleTinyResponseResponseBodyTypedDict
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""
    assigned_at_time: NotRequired[str]
    r"""An assigned at time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    assignment_type: NotRequired[AssignmentType]
    r"""Name of the assigning source for the driver assignment record.  Valid values: `invalid`, `unknown`, `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`"""
    end_time: NotRequired[str]
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""
    metadata: NotRequired[DriverAssignmentMetadataTinyObjectResponseBodyTypedDict]
    r"""Metadata object for external assignment source data."""


class DriverVehicleAssignmentV2ObjectResponseBody(BaseModel):
    r"""Object with driver assignment info and associated driver and vehicle info."""

    driver: GoaDriverTinyResponseResponseBody
    r"""A minified driver object. This object is only returned if the route is assigned to the driver."""

    is_passenger: Annotated[bool, pydantic.Field(alias="isPassenger")]
    r"""Boolean indicating whether the driver is a passenger."""

    start_time: Annotated[str, pydantic.Field(alias="startTime")]
    r"""A start time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    vehicle: GoaVehicleTinyResponseResponseBody
    r"""A minified vehicle object. This object is only returned if the route is assigned to the vehicle."""

    assigned_at_time: Annotated[
        Optional[str], pydantic.Field(alias="assignedAtTime")
    ] = None
    r"""An assigned at time in RFC 3339 format. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    assignment_type: Annotated[
        Optional[AssignmentType], pydantic.Field(alias="assignmentType")
    ] = None
    r"""Name of the assigning source for the driver assignment record.  Valid values: `invalid`, `unknown`, `HOS`, `idCard`, `static`, `faceId`, `tachograph`, `safetyManual`, `RFID`, `trailer`, `external`, `qrCode`"""

    end_time: Annotated[Optional[str], pydantic.Field(alias="endTime")] = None
    r"""An end time in RFC 3339 format. Omitted if not applicable. Millisecond precision and timezones are supported. (Examples: 2019-06-13T19:08:25Z, 2019-06-13T19:08:25.455Z, OR 2015-09-15T14:00:12-04:00)."""

    metadata: Optional[DriverAssignmentMetadataTinyObjectResponseBody] = None
    r"""Metadata object for external assignment source data."""
