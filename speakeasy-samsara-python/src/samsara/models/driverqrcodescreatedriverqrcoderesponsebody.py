"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .qrcoderesponseobjectresponsebody import (
    QrCodeResponseObjectResponseBody,
    QrCodeResponseObjectResponseBodyTypedDict,
)
from samsara.types import BaseModel
from typing_extensions import TypedDict


class DriverQrCodesCreateDriverQrCodeResponseBodyTypedDict(TypedDict):
    data: QrCodeResponseObjectResponseBodyTypedDict
    r"""A single document."""


class DriverQrCodesCreateDriverQrCodeResponseBody(BaseModel):
    data: QrCodeResponseObjectResponseBody
    r"""A single document."""
