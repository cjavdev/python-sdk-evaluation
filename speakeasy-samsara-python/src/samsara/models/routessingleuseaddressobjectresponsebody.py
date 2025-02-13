"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class RoutesSingleUseAddressObjectResponseBodyTypedDict(TypedDict):
    r"""This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId."""

    latitude: float
    r"""The latitude of the location"""
    longitude: float
    r"""The longitude of the location"""
    address: NotRequired[str]
    r"""Address of the stop."""


class RoutesSingleUseAddressObjectResponseBody(BaseModel):
    r"""This field is used to indicate stops along the route for which an address has not been persisted. This field is mutually exclusive with addressId."""

    latitude: float
    r"""The latitude of the location"""

    longitude: float
    r"""The longitude of the location"""

    address: Optional[str] = None
    r"""Address of the stop."""
