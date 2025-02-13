"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .alertobjectdriverresponsebody import (
    AlertObjectDriverResponseBody,
    AlertObjectDriverResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DriverAppSignOutResponseBodyTypedDict(TypedDict):
    r"""Details specific to Driver App Sign Out."""

    driver: NotRequired[AlertObjectDriverResponseBodyTypedDict]
    r"""A driver associated with the alert"""


class DriverAppSignOutResponseBody(BaseModel):
    r"""Details specific to Driver App Sign Out."""

    driver: Optional[AlertObjectDriverResponseBody] = None
    r"""A driver associated with the alert"""
