"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectproductresponsebody import (
    AlertObjectProductResponseBody,
    AlertObjectProductResponseBodyTypedDict,
)
from .goatagtinyresponseresponsebody import (
    GoaTagTinyResponseResponseBody,
    GoaTagTinyResponseResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class AlertObjectSensorResponseBodyTypedDict(TypedDict):
    r"""A sensor associated with the alert."""

    id: str
    r"""Thye ID of the sensor associated with the alert"""
    name: NotRequired[str]
    r"""The name of the sensor."""
    pinned_device_id: NotRequired[str]
    r"""The Pinned Device ID associated with the alert"""
    product: NotRequired[AlertObjectProductResponseBodyTypedDict]
    r"""The product associated with the alert"""
    tags: NotRequired[List[GoaTagTinyResponseResponseBodyTypedDict]]
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the sensor."""


class AlertObjectSensorResponseBody(BaseModel):
    r"""A sensor associated with the alert."""

    id: str
    r"""Thye ID of the sensor associated with the alert"""

    name: Optional[str] = None
    r"""The name of the sensor."""

    pinned_device_id: Annotated[
        Optional[str], pydantic.Field(alias="pinnedDeviceId")
    ] = None
    r"""The Pinned Device ID associated with the alert"""

    product: Optional[AlertObjectProductResponseBody] = None
    r"""The product associated with the alert"""

    tags: Optional[List[GoaTagTinyResponseResponseBody]] = None
    r"""The list of [tags](https://kb.samsara.com/hc/en-us/articles/360026674631-Using-Tags-and-Tag-Nesting) associated with the sensor."""
