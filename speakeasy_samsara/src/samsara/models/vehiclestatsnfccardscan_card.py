"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class VehicleStatsNfcCardScanCardTypedDict(TypedDict):
    r"""The card that was scanned."""

    id: NotRequired[str]
    r"""The id code of the card that was scanned."""


class VehicleStatsNfcCardScanCard(BaseModel):
    r"""The card that was scanned."""

    id: Optional[str] = None
    r"""The id code of the card that was scanned."""
