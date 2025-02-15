"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import pydantic
from samsara.types import BaseModel
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class UpdateDriverRequestHosSettingTypedDict(TypedDict):
    r"""Hos settings for a driver."""

    heavy_haul_exemption_toggle_enabled: NotRequired[bool]
    r"""Flag indicating this driver may use the Heavy Haul exemption in ELD logs."""


class UpdateDriverRequestHosSetting(BaseModel):
    r"""Hos settings for a driver."""

    heavy_haul_exemption_toggle_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="heavyHaulExemptionToggleEnabled")
    ] = False
    r"""Flag indicating this driver may use the Heavy Haul exemption in ELD logs."""
