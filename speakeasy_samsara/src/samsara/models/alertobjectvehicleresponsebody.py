"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .driverobjectresponsebody import (
    DriverObjectResponseBody,
    DriverObjectResponseBodyTypedDict,
)
from .goaattributetinyresponsebody import (
    GoaAttributeTinyResponseBody,
    GoaAttributeTinyResponseBodyTypedDict,
)
from .goatagtinyresponseresponsebody import (
    GoaTagTinyResponseResponseBody,
    GoaTagTinyResponseResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Dict, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AlertObjectVehicleResponseBodyTypedDict(TypedDict):
    r"""The vehicle associated with the alert."""

    id: str
    r"""The ID of the vehicle."""
    serial: str
    r"""The serial number of the gateway installed on the asset."""
    attributes: NotRequired[List[GoaAttributeTinyResponseBodyTypedDict]]
    r"""List of attributes associated with the entity"""
    external_ids: NotRequired[Dict[str, str]]
    r"""A map of external ids"""
    name: NotRequired[str]
    r"""The name of the vehicle."""
    static_assigned_driver: NotRequired[DriverObjectResponseBodyTypedDict]
    r"""Current driver of the vehicle. Note: this parameter includes all assignment sources, not just static assignments."""
    tags: NotRequired[List[GoaTagTinyResponseResponseBodyTypedDict]]
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the vehicle."""


class AlertObjectVehicleResponseBody(BaseModel):
    r"""The vehicle associated with the alert."""

    id: str
    r"""The ID of the vehicle."""

    serial: str
    r"""The serial number of the gateway installed on the asset."""

    attributes: Optional[List[GoaAttributeTinyResponseBody]] = None
    r"""List of attributes associated with the entity"""

    external_ids: Annotated[
        Optional[Dict[str, str]], pydantic.Field(alias="externalIds")
    ] = None
    r"""A map of external ids"""

    name: Optional[str] = None
    r"""The name of the vehicle."""

    static_assigned_driver: Annotated[
        Optional[DriverObjectResponseBody], pydantic.Field(alias="staticAssignedDriver")
    ] = None
    r"""Current driver of the vehicle. Note: this parameter includes all assignment sources, not just static assignments."""

    tags: Optional[List[GoaTagTinyResponseResponseBody]] = None
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the vehicle."""
