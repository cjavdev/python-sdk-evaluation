"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class QrCodeResponseObjectResponseBodyTypedDict(TypedDict):
    r"""A single document."""

    driver_id: int
    r"""ID for the driver the QR code belongs to."""
    qr_code_link: NotRequired[str]
    r"""URL link to the driver assignment QR code. Included if a QR code has been created for the driver."""


class QrCodeResponseObjectResponseBody(BaseModel):
    r"""A single document."""

    driver_id: Annotated[int, pydantic.Field(alias="driverId")]
    r"""ID for the driver the QR code belongs to."""

    qr_code_link: Annotated[Optional[str], pydantic.Field(alias="qrCodeLink")] = None
    r"""URL link to the driver assignment QR code. Included if a QR code has been created for the driver."""
