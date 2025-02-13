"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .gatewayresponseobjectresponsebody import (
    GatewayResponseObjectResponseBody,
    GatewayResponseObjectResponseBodyTypedDict,
)
from .goapaginationresponseresponsebody import (
    GoaPaginationResponseResponseBody,
    GoaPaginationResponseResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing import List
from typing_extensions import TypedDict


class GatewaysGetGatewaysResponseBodyTypedDict(TypedDict):
    data: List[GatewayResponseObjectResponseBodyTypedDict]
    r"""Activated gateways"""
    pagination: GoaPaginationResponseResponseBodyTypedDict
    r"""Pagination parameters."""


class GatewaysGetGatewaysResponseBody(BaseModel):
    data: List[GatewayResponseObjectResponseBody]
    r"""Activated gateways"""

    pagination: GoaPaginationResponseResponseBody
    r"""Pagination parameters."""
