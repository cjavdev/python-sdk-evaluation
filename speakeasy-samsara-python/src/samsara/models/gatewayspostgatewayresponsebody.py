"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .gatewayresponseobjectresponsebody import (
    GatewayResponseObjectResponseBody,
    GatewayResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class GatewaysPostGatewayResponseBodyTypedDict(TypedDict):
    data: GatewayResponseObjectResponseBodyTypedDict


class GatewaysPostGatewayResponseBody(BaseModel):
    data: GatewayResponseObjectResponseBody
