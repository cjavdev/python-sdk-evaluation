# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QrCodeCreateResponse", "Data"]


class Data(BaseModel):
    driver_id: int = FieldInfo(alias="driverId")
    """ID for the driver the QR code belongs to."""

    qr_code_link: Optional[str] = FieldInfo(alias="qrCodeLink", default=None)
    """URL link to the driver assignment QR code.

    Included if a QR code has been created for the driver.
    """


class QrCodeCreateResponse(BaseModel):
    data: Data
    """A single document."""
