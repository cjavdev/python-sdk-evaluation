"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectdriverresponsebody import (
    AlertObjectDriverResponseBody,
    AlertObjectDriverResponseBodyTypedDict,
)
from .alertobjecttrailerresponsebody import (
    AlertObjectTrailerResponseBody,
    AlertObjectTrailerResponseBodyTypedDict,
)
from .alertobjectvehicleresponsebody import (
    AlertObjectVehicleResponseBody,
    AlertObjectVehicleResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CloudBackupUploadIssueResponseBodyTypedDict(TypedDict):
    r"""Details specific to Cloud Backup Upload Issue."""

    driver: NotRequired[AlertObjectDriverResponseBodyTypedDict]
    r"""A driver associated with the alert"""
    trailer: NotRequired[AlertObjectTrailerResponseBodyTypedDict]
    r"""A trailer associated with the alert"""
    vehicle: NotRequired[AlertObjectVehicleResponseBodyTypedDict]
    r"""The vehicle associated with the alert."""


class CloudBackupUploadIssueResponseBody(BaseModel):
    r"""Details specific to Cloud Backup Upload Issue."""

    driver: Optional[AlertObjectDriverResponseBody] = None
    r"""A driver associated with the alert"""

    trailer: Optional[AlertObjectTrailerResponseBody] = None
    r"""A trailer associated with the alert"""

    vehicle: Optional[AlertObjectVehicleResponseBody] = None
    r"""The vehicle associated with the alert."""
