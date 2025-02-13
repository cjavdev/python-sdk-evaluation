"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .cameradetailsresponseresponsebody import (
    CameraDetailsResponseResponseBody,
    CameraDetailsResponseResponseBodyTypedDict,
)
from .gatewaydetailsresponseresponsebody import (
    GatewayDetailsResponseResponseBody,
    GatewayDetailsResponseResponseBodyTypedDict,
)
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class HealthDetailsResponseResponseBodyTypedDict(TypedDict):
    r"""Detailed health related metadata for the device."""

    camera_details: NotRequired[CameraDetailsResponseResponseBodyTypedDict]
    r"""Camera-specific health metadata details."""
    gateway_details: NotRequired[GatewayDetailsResponseResponseBodyTypedDict]
    r"""Gateway-specific health metadata."""


class HealthDetailsResponseResponseBody(BaseModel):
    r"""Detailed health related metadata for the device."""

    camera_details: Annotated[
        Optional[CameraDetailsResponseResponseBody],
        pydantic.Field(alias="cameraDetails"),
    ] = None
    r"""Camera-specific health metadata details."""

    gateway_details: Annotated[
        Optional[GatewayDetailsResponseResponseBody],
        pydantic.Field(alias="gatewayDetails"),
    ] = None
    r"""Gateway-specific health metadata."""
